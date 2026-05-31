import sys
import time
import threading
import os
from PyQt6.QtWidgets import QApplication, QTableWidgetItem
from PyQt6.QtGui import QImage

# Project Modules
from emulator.manager import EmulatorManager
from vision.capture import ScreenCapture
from vision.detector import ResourceDetector
from scanner.spiral import SpiralScanner
from dispatch.manager import ArmyDispatcher
from storage.database import BotDatabase
from safety.humanizer import Humanizer
from ui.dashboard import LiveDashboard
from core.config import ConfigManager
from core.logger import logger

class LordsMobileBot:
    def __init__(self, ui):
        self.ui = ui
        self.config = ConfigManager()
        self.db = BotDatabase()
        self.running = False
        self.paused = False
        
        # Initialize Core Components with config
        self.emulator = EmulatorManager(
            window_title=self.config.get("emu_name"),
            exe_path=self.config.get("emu_path")
        )
        self.detector = ResourceDetector()
        self.scanner = SpiralScanner()
        
    def initialize(self):
        """Initial check for emulator."""
        logger.info("Initializing Bot...")
        if not self.emulator.find_ldplayer_window():
            logger.warning("LDPlayer not found. Attempting to launch...")
            if not self.emulator.launch_emulator():
                self.ui.add_log("CRITICAL: Could not find or launch LDPlayer.")
                return False
        
        self.emulator.set_window_resolution(1600, 900)
        self.ui.add_log("Bot Initialized. Ready to start.")
        return True

    def start(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.thread = threading.Thread(target=self.bot_loop, daemon=True)
            self.thread.start()
            self.ui.signals.status_changed.emit("Running")
            logger.info("Bot Started")

    def stop(self):
        self.running = False
        self.ui.signals.status_changed.emit("Stopped")
        logger.info("Bot Stopped")

    def bot_loop(self):
        """Main automation logic with robust error handling."""
        try:
            capturer = ScreenCapture(self.emulator.window_handle)
            dispatcher = ArmyDispatcher(self.emulator)
            startup_complete = False
            
            while self.running:
                if self.paused:
                    time.sleep(1)
                    continue

                # 1. Capture and Stream
                screen_img = capturer.capture_win32()
                if screen_img is not None:
                    h, w, ch = screen_img.shape
                    bytes_per_line = ch * w
                    q_img = QImage(screen_img.data, w, h, bytes_per_line, QImage.Format.Format_BGR888)
                    self.ui.signals.new_frame.emit(q_img)
                else:
                    logger.error("Failed to capture screen.")
                    time.sleep(2)
                    continue

                # 2. Auto-Startup Logic
                if not startup_complete:
                    match = self.detector.detect_ui_button(screen_img, 'base_to_map')
                    if match:
                        logger.info("Detected 'Go to Map' button.")
                        self.emulator.send_click(match['x'], match['y'])
                        time.sleep(5)
                        self.emulator.send_click(960, 537) # Go to center
                        startup_complete = True
                        self.ui.signals.status_changed.emit("Gathering Loop")
                    else:
                        time.sleep(2)
                        continue

                # 3. Gathering Logic
                active_tasks = self.db.get_all_active_tasks()
                self.ui.signals.tasks_updated.emit(active_tasks)

                if len(active_tasks) < 6:
                    selected_res = self.config.get("resources_to_gather", [])
                    match = self.detector.detect_best_resource(screen_img)
                    if match:
                        res_type = match['name'].split('_')[0]
                        if res_type in selected_res:
                            logger.info(f"Found {match['name']}. Dispatching...")
                            if dispatcher.dispatch_to_tile(match['x'], match['y'], self.detector, screen_img):
                                army_id = len(active_tasks) + 1
                                # Get duration from config timers
                                level = match['name'].split('_lv')[-1]
                                duration = self.config.get("timers", {}).get(res_type, {}).get(level, 60) * 60
                                self.db.add_active_army(army_id, res_type, int(level), duration, 0, 0)
                    else:
                        # Move map logic
                        pass

                Humanizer.sleep(2, 4)

        except Exception as e:
            logger.exception("Fatal error in bot loop")
            self.ui.add_log(f"FATAL ERROR: {str(e)}")
            self.running = False

def main():
    try:
        app = QApplication(sys.argv)
        dashboard = LiveDashboard()
        bot = LordsMobileBot(dashboard)
        
        # Connect UI
        dashboard.start_btn.clicked.connect(bot.start)
        dashboard.stop_btn.clicked.connect(bot.stop)
        dashboard.center_btn.clicked.connect(lambda: bot.emulator.send_click(960, 537))
        
        # Load Config into UI
        dashboard.emu_path_input.setText(bot.config.get("emu_path"))
        dashboard.emu_name_input.setText(bot.config.get("emu_name"))
        
        def save_emu_settings():
            bot.config.set("emu_path", dashboard.emu_path_input.text())
            bot.config.set("emu_name", dashboard.emu_name_input.text())
            bot.emulator.exe_path = bot.config.get("emu_path")
            bot.emulator.window_title = bot.config.get("emu_name")
            dashboard.add_log("Settings saved to config.json")
            logger.info("Config updated")

        dashboard.save_emu_settings_btn.clicked.connect(save_emu_settings)

        if bot.initialize():
            dashboard.show()
            sys.exit(app.exec())
    except Exception as e:
        logger.exception("Application failed to start")
        print(f"Application Error: {e}")

if __name__ == "__main__":
    main()
