import sys
import os
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QTableWidget, QTableWidgetItem, 
                             QHeaderView, QTabWidget, QGroupBox, QGridLayout, 
                             QCheckBox, QLineEdit, QFileDialog, QStatusBar)
from ui.template_manager import TemplateManagerTab
from PyQt6.QtCore import Qt, pyqtSignal, QObject
from PyQt6.QtGui import QImage, QPixmap

class DashboardSignals(QObject):
    new_frame = pyqtSignal(QImage)
    status_changed = pyqtSignal(str)
    tasks_updated = pyqtSignal(list)

class LiveDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lords Mobile Bot - Pro Version")
        self.setMinimumSize(1000, 700)
        self.signals = DashboardSignals()
        self._init_ui()
        self._connect_signals()

    def _init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Top Control Bar
        control_bar = QWidget()
        control_bar_layout = QHBoxLayout(control_bar)
        
        self.status_label = QLabel("Status: Idle")
        self.status_label.setStyleSheet("font-weight: bold; color: #2c3e50; font-size: 14px;")
        
        self.start_btn = QPushButton("▶ START")
        self.start_btn.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold; width: 100px;")
        
        self.pause_btn = QPushButton("⏸ PAUSE")
        self.pause_btn.setStyleSheet("background-color: #f39c12; color: white; font-weight: bold; width: 100px;")
        
        self.stop_btn = QPushButton("⏹ STOP")
        self.stop_btn.setStyleSheet("background-color: #c0392b; color: white; font-weight: bold; width: 100px;")
        
        self.center_btn = QPushButton("📍 CENTER")
        self.center_btn.setStyleSheet("background-color: #8e44ad; color: white; font-weight: bold; width: 100px;")

        control_bar_layout.addWidget(self.status_label)
        control_bar_layout.addStretch()
        control_bar_layout.addWidget(self.center_btn)
        control_bar_layout.addStretch()
        control_bar_layout.addWidget(self.start_btn)
        control_bar_layout.addWidget(self.pause_btn)
        control_bar_layout.addWidget(self.stop_btn)
        
        main_layout.addWidget(control_bar)

        # Main Section: Tabs
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # Tab 1: Dashboard
        self.dashboard_tab = QWidget()
        self._setup_dashboard_tab()
        self.tabs.addTab(self.dashboard_tab, "Dashboard")

        # Tab 2: Template Manager (New Dynamic System)
        self.template_manager = TemplateManagerTab()
        self.tabs.addTab(self.template_manager, "Template Manager")

        # Tab 3: Timer Settings
        self.timer_tab = QWidget()
        self._setup_timer_tab()
        self.tabs.addTab(self.timer_tab, "Resource Timers")

        # Tab 4: Emulator Settings
        self.emu_tab = QWidget()
        self._setup_emu_tab()
        self.tabs.addTab(self.emu_tab, "Emulator Settings")

        self.setStatusBar(QStatusBar())

    def _setup_dashboard_tab(self):
        layout = QHBoxLayout(self.dashboard_tab)
        
        # Left Panel: Live Stream & Selection
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # 1. Screen Stream
        self.screen_label = QLabel("Waiting for LDPlayer...")
        self.screen_label.setFixedSize(480, 270) # 16:9 scaled down
        self.screen_label.setStyleSheet("background-color: black; color: white; border: 2px solid #34495e;")
        self.screen_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(self.screen_label)
        
        # 2. Automation Tasks (Pro)
        task_group = QGroupBox("Automation Tasks (Pro)")
        task_layout = QVBoxLayout()
        
        # Resource Selection
        res_label = QLabel("Gathering Priorities:")
        res_label.setStyleSheet("font-weight: bold;")
        task_layout.addWidget(res_label)
        res_grid = QGridLayout()
        self.res_checks = {}
        resources = ["Food", "Gold", "Wood", "Stone", "Ore"]
        for i, res in enumerate(resources):
            cb = QCheckBox(res)
            cb.setChecked(True)
            self.res_checks[res] = cb
            res_grid.addWidget(cb, i // 3, i % 3)
        task_layout.addLayout(res_grid)
        
        # Guild Tasks
        guild_label = QLabel("Guild Tasks:")
        guild_label.setStyleSheet("font-weight: bold;")
        task_layout.addWidget(guild_label)
        self.guild_help_cb = QCheckBox("Auto Guild Help")
        self.guild_help_cb.setChecked(True)
        self.guild_gift_cb = QCheckBox("Auto Collect Gifts")
        self.guild_gift_cb.setChecked(True)
        self.monster_hunt_cb = QCheckBox("Auto Monster Hunt")
        self.monster_hunt_cb.setChecked(False)
        self.auto_shield_cb = QCheckBox("Auto Shield on Attack")
        self.auto_shield_cb.setChecked(True)
        self.auto_resource_cb = QCheckBox("Auto Use Resources from Bag")
        self.auto_resource_cb.setChecked(False)
        task_layout.addWidget(self.guild_help_cb)
        task_layout.addWidget(self.guild_gift_cb)
        task_layout.addWidget(self.monster_hunt_cb)
        task_layout.addWidget(self.auto_shield_cb)
        task_layout.addWidget(self.auto_resource_cb)
        
        task_group.setLayout(task_layout)
        left_layout.addWidget(task_group)
        left_layout.addStretch()
        
        layout.addWidget(left_panel)

        # Right Panel: Data & Logs
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        # Task Table
        table_label = QLabel("ACTIVE GATHERING TASKS")
        table_label.setStyleSheet("font-weight: bold; color: #2980b9;")
        right_layout.addWidget(table_label)
        
        self.task_table = QTableWidget(0, 5)
        self.task_table.setHorizontalHeaderLabels(["Army", "Resource", "Level", "Location", "Time Left"])
        self.task_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        right_layout.addWidget(self.task_table)

        # Simple Log Console
        log_label = QLabel("EVENT LOG")
        log_label.setStyleSheet("font-weight: bold; color: #2980b9;")
        right_layout.addWidget(log_label)
        
        self.log_console = QTableWidget(0, 1)
        self.log_console.setHorizontalHeaderLabels(["Message"])
        self.log_console.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.log_console.setFixedHeight(150)
        right_layout.addWidget(self.log_console)
        
        layout.addWidget(right_panel)

    def _setup_image_tab(self):
        layout = QVBoxLayout(self.image_tab)
        info = QLabel("Upload images for resources and buttons. Save them as .png in assets/templates/ or assets/ui/")
        layout.addWidget(info)
        
        # Button to open asset folder
        open_btn = QPushButton("Open Assets Folder")
        open_btn.clicked.connect(lambda: os.startfile(os.path.abspath("assets")))
        layout.addWidget(open_btn)
        layout.addStretch()

    def _setup_timer_tab(self):
        layout = QVBoxLayout(self.timer_tab)
        
        self.timer_table = QTableWidget(25, 3)
        self.timer_table.setHorizontalHeaderLabels(["Resource Type", "Level", "Time (Minutes)"])
        self.timer_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        resources = ["Food", "Gold", "Wood", "Stone", "Ore"]
        row = 0
        for res in resources:
            for lv in range(5, 0, -1):
                self.timer_table.setItem(row, 0, QTableWidgetItem(res))
                self.timer_table.setItem(row, 1, QTableWidgetItem(str(lv)))
                self.timer_table.setItem(row, 2, QTableWidgetItem("60"))
                row += 1
        
        layout.addWidget(self.timer_table)
        
        self.save_timers_btn = QPushButton("SAVE ALL TIMER SETTINGS")
        self.save_timers_btn.setStyleSheet("background-color: #2980b9; color: white; font-weight: bold; height: 40px;")
        layout.addWidget(self.save_timers_btn)

    def _setup_emu_tab(self):
        layout = QVBoxLayout(self.emu_tab)
        grid = QGridLayout()
        
        grid.addWidget(QLabel("<b>Emulator Executable Path:</b>"), 0, 0)
        self.emu_path_input = QLineEdit()
        self.emu_path_input.setText("C:/LDPlayer/LDPlayer9/ldplayer.exe")
        grid.addWidget(self.emu_path_input, 0, 1)
        
        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self._browse_emu_path)
        grid.addWidget(browse_btn, 0, 2)
        
        grid.addWidget(QLabel("<b>Emulator Window Name:</b>"), 1, 0)
        self.emu_name_input = QLineEdit()
        self.emu_name_input.setText("LDPlayer")
        grid.addWidget(self.emu_name_input, 1, 1)
        
        layout.addLayout(grid)
        
        self.save_emu_settings_btn = QPushButton("SAVE EMULATOR SETTINGS")
        self.save_emu_settings_btn.setStyleSheet("background-color: #2980b9; color: white; font-weight: bold; height: 40px;")
        layout.addWidget(self.save_emu_settings_btn)
        layout.addStretch()

    def _browse_emu_path(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select LDPlayer Executable", "", "Executable (*.exe)")
        if path:
            self.emu_path_input.setText(path)

    def _connect_signals(self):
        self.signals.new_frame.connect(self._update_screen)
        self.signals.status_changed.connect(self._update_status)
        self.signals.tasks_updated.connect(self._update_tasks)

    def _update_screen(self, q_img):
        pixmap = QPixmap.fromImage(q_img)
        self.screen_label.setPixmap(pixmap.scaled(self.screen_label.size(), Qt.AspectRatioMode.KeepAspectRatio))

    def _update_status(self, status):
        self.status_label.setText(f"Status: {status}")

    def _update_tasks(self, tasks):
        self.task_table.setRowCount(len(tasks))
        for i, task in enumerate(tasks):
            self.task_table.setItem(i, 0, QTableWidgetItem(str(task['army_id'])))
            self.task_table.setItem(i, 1, QTableWidgetItem(task['resource_type']))
            self.task_table.setItem(i, 2, QTableWidgetItem(str(task['resource_level'])))
            self.task_table.setItem(i, 3, QTableWidgetItem(f"{task['map_x']}, {task['map_y']}"))
            self.task_table.setItem(i, 4, QTableWidgetItem("Active"))

    def add_log(self, message):
        row = self.log_console.rowCount()
        self.log_console.insertRow(row)
        self.log_console.setItem(row, 0, QTableWidgetItem(message))
        self.log_console.scrollToBottom()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LiveDashboard()
    window.show()
    sys.exit(app.exec())
