import sys
import threading
import time
from PyQt6.QtWidgets import QApplication

# Import all modules
from emulator.manager import EmulatorManager
from vision.capture import ScreenCapture
from vision.detector import ResourceDetector
from scanner.spiral import SpiralScanner
from dispatch.manager import ArmyDispatcher
from storage.database import BotDatabase
from safety.humanizer import Humanizer
from ui.dashboard import LiveDashboard

class LordsMobileBot:
    """
    Main Bot Orchestrator
    Integrates all modules into a functional automation framework.
    """
    def __init__(self, ui):
        self.ui = ui
        self.emulator = EmulatorManager()
        self.db = BotDatabase()
        self.detector = ResourceDetector()
        self.scanner = SpiralScanner()
        self.running = False
        self.paused = False

    def initialize(self):
        self.ui.signals.status_changed.emit("Initializing...")
        self.ui.signals.log_message.emit("Bot initialization started.")
        
        try:
            # 1. Find LDPlayer
            if not self.emulator.find_ldplayer_window():
                self.ui.signals.status_changed.emit("Error: LDPlayer Not Found")
                self.ui.signals.log_message.emit("CRITICAL: LDPlayer window not detected.")
                return False
            
            self.ui.signals.log_message.emit("LDPlayer window found.")
            
            # 2. Connect ADB
            # Note: User needs to ensure ADB is enabled in LDPlayer settings
            # self.emulator.connect_adb()
            
            # 3. Load Vision Templates
            self.detector.load_templates()
            self.ui.signals.log_message.emit(f"Loaded {len(self.detector.templates)} resource templates.")
            
            self.ui.signals.status_changed.emit("Ready")
            self.ui.signals.log_message.emit("Bot is ready to start.")
            return True
        except Exception as e:
            self.ui.signals.status_changed.emit("Init Error")
            self.ui.signals.log_message.emit(f"ERROR during init: {str(e)}")
            return False

    def start(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.thread = threading.Thread(target=self.bot_loop, daemon=True)
            self.thread.start()
            self.ui.signals.status_changed.emit("Running")

    def stop(self):
        self.running = False
        self.ui.signals.status_changed.emit("Stopped")

    def bot_loop(self):
        """Main automation logic."""
        capturer = ScreenCapture(self.emulator.window_handle)
        dispatcher = ArmyDispatcher(self.emulator)
        
        # 1. Wait for Game & Auto-Startup
        self.ui.signals.log_message.emit("Starting Auto-Boot sequence...")
        startup_complete = False
        
        while self.running:
            if self.paused:
                time.sleep(1)
                continue

            try:
                # --- LIVE STREAM UPDATE ---
                screen_img = capturer.capture_win32()
                if screen_img is not None:
                    h, w, ch = screen_img.shape
                    bytes_per_line = ch * w
                    q_img = QImage(screen_img.data, w, h, bytes_per_line, QImage.Format.Format_BGR888)
                    self.ui.signals.new_frame.emit(q_img)
                else:
                    time.sleep(1)
                    continue

                # --- AUTO-STARTUP LOGIC ---
                if not startup_complete:
                    # Check for "Base to Map" button
                    match = self.detector.detect_ui_button(screen_img, 'base_to_map')
                    if match:
                        self.ui.signals.log_message.emit("Detected 'Go to Map' button. Clicking...")
                        self.emulator.send_click(match['x'], match['y'])
                        time.sleep(5)
                        
                        # Go to Center (960, 537)
                        self.ui.signals.log_message.emit("Opening Mini-Map to go to center...")
                        # Assume mini-map button is at a fixed location or detected
                        # Then click the center coordinates specified by user
                        self.emulator.send_click(960, 537)
                        self.ui.signals.log_message.emit("Navigated to world center (960, 537).")
                        startup_complete = True
                        self.ui.signals.status_changed.emit("Gathering Loop")
                    else:
                        self.ui.signals.log_message.emit("Waiting for game to load or 'Go to Map' button...")
                        time.sleep(3)
                        continue

                # --- GATHERING LOOP ---
                # 1. Update Dashboard with current tasks
                active_tasks = self.db.get_all_active_tasks()
                self.ui.signals.tasks_updated.emit(active_tasks)

                # 2. Check for and clean up expired tasks
                expired = self.db.get_expired_armies()
                if expired:
                    for army_id in expired:
                        self.db.remove_army(army_id)
                        self.ui.signals.log_message.emit(f"Army {army_id} finished gathering.")

                # 3. Check for available army slots (max 6)
                if len(active_tasks) < 6:
                    # Get selected resources from UI
                    selected_res = [res for res, cb in self.ui.res_checks.items() if cb.isChecked()]
                    self.ui.signals.log_message.emit(f"Searching for: {', '.join(selected_res)}")
                    
                    # Detection & Dispatch
                    match = self.detector.detect_best_resource(screen_img) # Priority logic inside
                    if match:
                        res_type = match['name'].split('_')[0]
                        if res_type in selected_res:
                            self.ui.signals.log_message.emit(f"Found {match['name']}! Dispatching army...")
                            if dispatcher.dispatch_to_tile(match['x'], match['y'], self.detector, screen_img):
                                army_id = len(active_tasks) + 1
                                # Get custom duration from DB or default
                                duration = 3600 # 1 hour default
                                self.db.add_active_army(army_id, res_type, 5, duration, 0, 0)
                                self.ui.signals.log_message.emit(f"Army {army_id} sent to {match['name']}.")
                    else:
                        # Move map if nothing found
                        self.ui.signals.log_message.emit("No resources found. Moving map...")
                        # scanner logic here
                
                # Human-like safety delay
                Humanizer.sleep(2, 4)

            except Exception as e:
                self.ui.signals.log_message.emit(f"Runtime Error: {str(e)}")
                time.sleep(5)

def main():
    app = QApplication(sys.argv)
    dashboard = LiveDashboard()
    bot = LordsMobileBot(dashboard)
    
    # Connect UI buttons to bot logic
    dashboard.start_btn.clicked.connect(bot.start)
    dashboard.stop_btn.clicked.connect(bot.stop)
    dashboard.center_btn.clicked.connect(lambda: bot.emulator.send_click(960, 537))
    
    def save_timers():
        for row in range(dashboard.timer_table.rowCount()):
            res_type = dashboard.timer_table.item(row, 0).text()
            level = int(dashboard.timer_table.item(row, 1).text())
            minutes = int(dashboard.timer_table.item(row, 2).text())
            bot.db.update_cooldown(res_type, level, minutes * 60)
        dashboard.add_log("All timer settings saved to database.")

    dashboard.save_timers_btn.clicked.connect(save_timers)
    
    # Load existing timers into UI
    existing_timers = bot.db.get_all_cooldowns()
    if existing_timers:
        for row_data in existing_timers:
            for row in range(dashboard.timer_table.rowCount()):
                if (dashboard.timer_table.item(row, 0).text() == row_data['resource_type'] and 
                    dashboard.timer_table.item(row, 1).text() == str(row_data['resource_level'])):
                    dashboard.timer_table.setItem(row, 2, QTableWidgetItem(str(row_data['duration_seconds'] // 60)))

    # Load Emulator Settings
    saved_path = bot.db.get_ui_setting('emu_path')
    saved_name = bot.db.get_ui_setting('emu_name')
    if saved_path: dashboard.emu_path_input.setText(saved_path)
    if saved_name: dashboard.emu_name_input.setText(saved_name)
    
    def save_emu_settings():
        path = dashboard.emu_path_input.text()
        name = dashboard.emu_name_input.text()
        bot.db.update_ui_setting('emu_path', path)
        bot.db.update_ui_setting('emu_name', name)
        bot.emulator.exe_path = path
        bot.emulator.window_title = name
        dashboard.add_log("Emulator settings saved.")

    dashboard.save_emu_settings_btn.clicked.connect(save_emu_settings)

    if bot.initialize():
        dashboard.show()
        sys.exit(app.exec())
    else:
        print("Bot failed to initialize.")

if __name__ == "__main__":
    main()
