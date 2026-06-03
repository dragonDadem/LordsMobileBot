import sys
import time
import threading
import os
import cv2
from PyQt6.QtWidgets import QApplication, QTableWidgetItem
from PyQt6.QtGui import QImage

# Project Modules
from emulator.manager import EmulatorManager
from vision.capture import ScreenCapture
from vision.detector import ResourceDetector
from vision.scene_manager import SceneDetector
from scanner.spiral import SpiralScanner
from dispatch.manager import ArmyDispatcher
from storage.database import BotDatabase
from safety.humanizer import Humanizer
from ui.dashboard import LiveDashboard
from core.config import ConfigManager
from core.template_engine import TemplateEngine
from core.logger import logger
from guild.guild_manager import GuildManager
from combat.monster_hunter import MonsterHunter
from safety.protection import ProtectionSystem
from resources.resource_manager import ResourceManager
from core.stats import StatsManager
from core.scheduler import TaskScheduler

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
        self.template_engine = TemplateEngine()
        self.scanner = SpiralScanner()
        self.guild = GuildManager(self.emulator, self.detector)
        self.combat = MonsterHunter(self.emulator, self.detector)
        self.protection = ProtectionSystem(self.emulator, self.detector)
        self.resources = ResourceManager(self.emulator, self.detector)
        self.scene_detector = SceneDetector(self.detector)
        self.stats = StatsManager()
        self.scheduler = TaskScheduler()
        self._init_scheduler()
        self.last_gift_collection = 0
        
    def _init_scheduler(self):
        self.scheduler.add_task("guild_gifts", 10800) # 3 hours
        self.scheduler.add_task("shield_check", 60)    # 1 min
        self.scheduler.add_task("monster_hunt", 600)   # 10 mins

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
            self.capturer = capturer # Store for access if needed
            dispatcher = ArmyDispatcher(self.emulator)
            startup_complete = False
            consecutive_failures = 0
            last_ui_update = 0
            
            while self.running:
                if self.paused:
                    time.sleep(1)
                    continue

                # 1. Capture and Stream
                screen_img = capturer.capture_win32()

                # Periodic UI Update
                if time.time() - last_ui_update > 2:
                    self.ui.signals.stats_updated.emit(self.stats.get_summary())
                    last_ui_update = time.time()

                # Live Template Verification (Debug/Training mode)
                if self.ui.template_manager.live_preview_cb.isChecked() and screen_img is not None:
                    debug_img = screen_img.copy()
                    for t in self.detector.ui_templates:
                        match = self.detector.detect_ui_button(debug_img, t)
                        if match:
                            cv2.rectangle(debug_img,
                                          (match['x']-20, match['y']-20),
                                          (match['x']+20, match['y']+20),
                                          (0, 255, 0), 2)
                    screen_img = debug_img

                if screen_img is None:
                    consecutive_failures += 1
                    logger.warning(f"Screen capture failed ({consecutive_failures}/5)")
                    if consecutive_failures >= 5:
                        self.ui.add_log("CRITICAL: Emulator unresponsive. Restarting...")
                        self.emulator.restart_app()
                        consecutive_failures = 0
                        startup_complete = False
                        time.sleep(10)
                    time.sleep(2)
                    continue

                consecutive_failures = 0 # Reset on success

                # Stream to UI
                h, w, ch = screen_img.shape
                bytes_per_line = ch * w
                q_img = QImage(screen_img.data, w, h, bytes_per_line, QImage.Format.Format_BGR888)
                self.ui.signals.new_frame.emit(q_img)

                # 1.4 Security Check (Highest Priority)
                if self.ui.auto_shield_cb.isChecked():
                    if self.protection.check_for_threats(screen_img, capturer):
                        # Pause other tasks if under attack
                        continue

                # 1.5 Guild Tasks (Pro Feature)
                if self.ui.guild_help_cb.isChecked():
                    if self.guild.check_and_help(capturer):
                        self.stats.add_help()
                
                if self.ui.guild_gift_cb.isChecked() and self.scheduler.should_run("guild_gifts"):
                    if self.guild.collect_gifts(capturer):
                        self.scheduler.mark_run("guild_gifts")
                        self.stats.add_gift()

                # 1.6 Monster Hunting (Pro Feature)
                if self.ui.monster_hunt_cb.isChecked() and self.scheduler.should_run("monster_hunt"):
                    if self.combat.hunt_nearby_monster(capturer):
                        self.scheduler.mark_run("monster_hunt")
                        self.stats.add_hunt()
                
                # 1.7 Resource Management (Pro Feature)
                if self.ui.auto_resource_cb.isChecked():
                    # Check every 10 minutes or so
                    pass

                # 2. Scene-Aware Navigation & Startup
                scene = self.scene_detector.detect_current_scene(screen_img)
                if scene == "LOADING":
                    time.sleep(5)
                    continue
                elif scene == "AD":
                    match = self.detector.detect_ui_button(screen_img, 'close_panel')
                    if match: self.emulator.send_click(match['x'], match['y'])
                    continue
                elif scene == "BASE":
                    match = self.detector.detect_ui_button(screen_img, 'base_to_map')
                    if match:
                        self.emulator.send_click(match['x'], match['y'])
                        time.sleep(3)
                    continue
                elif scene == "UNKNOWN" and not startup_complete:
                    # Attempt to find any known button or wait
                    time.sleep(2)
                    continue

                if not startup_complete and scene == "MAP":
                    logger.info("On Map. Navigating to center.")
                    self.emulator.send_click(960, 537) # Go to center
                    startup_complete = True
                    self.ui.signals.status_changed.emit("Gathering Loop")

                # 3. Gathering Logic & Task Management
                expired_ids = self.db.get_expired_armies()
                for eid in expired_ids:
                    logger.info(f"Army {eid} has returned. Freeing slot.")
                    self.db.remove_army(eid)

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
                                # Assign next available army ID (1-6)
                                used_ids = [t['army_id'] for t in active_tasks]
                                army_id = 1
                                for i in range(1, 7):
                                    if i not in used_ids:
                                        army_id = i
                                        break

                                level = match['name'].split('_lv')[-1]
                                duration = self.config.get("timers", {}).get(res_type, {}).get(level, 60) * 60
                                self.db.add_active_army(army_id, res_type, int(level), duration, 0, 0)
                                self.scanner.reset() # Reset scanner on success
                    else:
                        # Move map logic using SpiralScanner
                        next_pos = self.scanner.get_next_grid_pos()
                        logger.info(f"No resources found. Navigating to coordinate: {next_pos}")

                        # Use coordinate entry (Simulated via ADB for precision)
                        # Sequence: Click Coordinate Button -> Input X -> Input Y -> Click Go
                        self.emulator.send_click(100, 850) # Coords button
                        time.sleep(1)
                        self.emulator.adb_device.shell(f"input text {next_pos[0]}")
                        time.sleep(0.5)
                        self.emulator.adb_device.shell(f"input text {next_pos[1]}")
                        self.emulator.adb_device.shell("input keyevent 66") # Enter
                        time.sleep(2)

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
        def go_to_center():
            bot.ui.add_log("Attempting to go to map center...")
            # Try to find map button first
            screen = bot.latest_frame if bot.latest_frame is not None else None
            if screen is not None:
                map_btn = bot.detector.detect_ui_button(screen, 'open_map')
                if map_btn:
                    bot.emulator.send_click(map_btn['x'], map_btn['y'])
                    time.sleep(1)
            
            # Click the coordinates (Center of screen in map view)
            bot.emulator.send_click(960, 537)
            bot.ui.add_log("Center command sent via ADB.")

        dashboard.center_btn.clicked.connect(go_to_center)
        
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

        # Connect Template Manager
        def load_templates_to_ui():
            for t in bot.template_engine.templates:
                bot.ui.template_manager.add_row(t['name'], t['path'], t['type'])
        
        def save_all_templates():
            ui_data = bot.ui.template_manager.get_ui_data()
            count = 0
            for item in ui_data:
                if item['path'] and os.path.exists(item['path']):
                    bot.template_engine.save_template(item['name'], item['type'], item['path'])
                    count += 1
            bot.detector.load_templates() # Reload in detector
            bot.ui.add_log(f"Saved {count} templates. Detector reloaded.")

        load_templates_to_ui()
        dashboard.template_manager.save_btn.clicked.connect(save_all_templates)

        if bot.initialize():
            dashboard.show()
            sys.exit(app.exec())
    except Exception as e:
        logger.exception("Application failed to start")
        print(f"Application Error: {e}")

if __name__ == "__main__":
    main()
