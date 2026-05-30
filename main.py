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
        
        while self.running:
            if self.paused:
                time.sleep(1)
                continue

            try:
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
                    # Scan logic placeholder
                    self.ui.signals.log_message.emit("Searching for new resource tiles...")
                    # target_pos = self.scanner.get_next_grid_pos()
                    # ... vision detection ...
                
                # Human-like safety delay
                Humanizer.sleep(3, 7)
                Humanizer.random_pause()

            except Exception as e:
                self.ui.signals.log_message.emit(f"Runtime Error: {str(e)}")
                time.sleep(10) # Wait longer on error

def main():
    app = QApplication(sys.argv)
    dashboard = LiveDashboard()
    bot = LordsMobileBot(dashboard)
    
    # Connect UI buttons to bot logic
    dashboard.start_btn.clicked.connect(bot.start)
    dashboard.stop_btn.clicked.connect(bot.stop)
    
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

    if bot.initialize():
        dashboard.show()
        sys.exit(app.exec())
    else:
        print("Bot failed to initialize.")

if __name__ == "__main__":
    main()
