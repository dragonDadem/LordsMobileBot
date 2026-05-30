import sys
import time
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTableWidget, QTableWidgetItem, 
                             QLabel, QPushButton, QHeaderView, QFrame, QStatusBar,
                             QTabWidget, QFileDialog, QGridLayout, QLineEdit, QScrollArea,
                             QCheckBox, QGroupBox)
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer, Qt, pyqtSignal, QObject, QSize
import shutil
import os
from PyQt6.QtCore import QTimer, Qt, pyqtSignal, QObject

class BotSignals(QObject):
    status_changed = pyqtSignal(str)
    tasks_updated = pyqtSignal(list)
    log_message = pyqtSignal(str)
    new_frame = pyqtSignal(QImage)

class LiveDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lords Mobile Bot - Control Center")
        self.resize(1000, 600)
        self.signals = BotSignals()
        self._init_ui()
        
        # Connect signals
        self.signals.status_changed.connect(self.update_status_label)
        self.signals.tasks_updated.connect(self.refresh_task_table)
        self.signals.log_message.connect(self.add_log)

    def _init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Top Section: Control Bar
        control_bar = QFrame()
        control_bar.setFixedHeight(80)
        control_bar_layout = QHBoxLayout(control_bar)
        
        self.status_label = QLabel("STATUS: IDLE")
        self.status_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #7f8c8d; padding: 5px;")
        
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

        # Tab 1: Dashboard (Existing Logic)
        self.dashboard_tab = QWidget()
        self._setup_dashboard_tab()
        self.tabs.addTab(self.dashboard_tab, "Dashboard")

        # Tab 2: Image Management
        self.image_tab = QWidget()
        self._setup_image_tab()
        self.tabs.addTab(self.image_tab, "Images & Templates")

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
        
        # 2. Resource Selection
        res_group = QGroupBox("Select Resources to Gather")
        res_layout = QGridLayout()
        self.res_checks = {}
        resources = ["Food", "Gold", "Wood", "Stone", "Ore"]
        for i, res in enumerate(resources):
            cb = QCheckBox(res)
            cb.setChecked(True)
            self.res_checks[res] = cb
            res_layout.addWidget(cb, i // 2, i % 2)
        res_group.setLayout(res_layout)
        left_layout.addWidget(res_group)
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
        
        # Connect new_frame signal
        self.signals.new_frame.connect(self.update_screen)

    def update_screen(self, q_img):
        pixmap = QPixmap.fromImage(q_img)
        self.screen_label.setPixmap(pixmap.scaled(self.screen_label.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def _setup_image_tab(self):
        layout = QVBoxLayout(self.image_tab)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        grid = QGridLayout(content)
        
        # Resource Templates Section
        row = 0
        grid.addWidget(QLabel("<b>RESOURCE TEMPLATES (Levels 5 to 1)</b>"), row, 0, 1, 3)
        row += 1
        
        resources = ["Food", "Gold", "Wood", "Stone", "Ore"]
        for res in resources:
            grid.addWidget(QLabel(f"<b>{res}</b>"), row, 0)
            for lv in range(5, 0, -1):
                btn = QPushButton(f"Upload Lv{lv}")
                btn.clicked.connect(lambda checked, r=res, l=lv: self._upload_template(r, l))
                grid.addWidget(btn, row, 6 - lv)
            row += 1
            
        # UI Buttons Section
        row += 1
        grid.addWidget(QLabel("<b>UI CONTROL BUTTONS</b>"), row, 0, 1, 3)
        row += 1
        
        ui_buttons = [
            ("Base to Map", "base_to_map"),
            ("Exit Panel", "exit_panel"),
            ("Auto-Select", "auto_select"),
            ("Deploy/Gather", "deploy_gather")
        ]
        
        for label, key in ui_buttons:
            grid.addWidget(QLabel(label), row, 0)
            btn = QPushButton("Upload Image")
            btn.clicked.connect(lambda checked, k=key: self._upload_ui_button(k))
            grid.addWidget(btn, row, 1)
            row += 1
            
        scroll.setWidget(content)
        layout.addWidget(scroll)

    def _setup_timer_tab(self):
        layout = QVBoxLayout(self.timer_tab)
        self.timer_table = QTableWidget(25, 3)
        self.timer_table.setHorizontalHeaderLabels(["Resource", "Level", "Time (Minutes)"])
        self.timer_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        resources = ["Food", "Gold", "Wood", "Stone", "Ore"]
        row = 0
        for res in resources:
            for lv in range(5, 0, -1):
                self.timer_table.setItem(row, 0, QTableWidgetItem(res))
                self.timer_table.setItem(row, 1, QTableWidgetItem(str(lv)))
                self.timer_table.setItem(row, 2, QTableWidgetItem("60")) # Default
                row += 1
        
        layout.addWidget(self.timer_table)
        self.save_timers_btn = QPushButton("SAVE ALL TIMER SETTINGS")
        self.save_timers_btn.setStyleSheet("background-color: #2980b9; color: white; padding: 10px;")
        layout.addWidget(self.save_timers_btn)

    def _setup_emu_tab(self):
        layout = QVBoxLayout(self.emu_tab)
        grid = QGridLayout()
        
        grid.addWidget(QLabel("<b>Emulator Executable Path:</b>"), 0, 0)
        self.emu_path_input = QLineEdit()
        self.emu_path_input.setPlaceholderText("C:/LDPlayer/LDPlayer9/dnplayer.exe")
        grid.addWidget(self.emu_path_input, 0, 1)
        
        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self._browse_emu_path)
        grid.addWidget(browse_btn, 0, 2)
        
        grid.addWidget(QLabel("<b>Emulator Window Name:</b>"), 1, 0)
        self.emu_name_input = QLineEdit()
        self.emu_name_input.setText("LDPlayer")
        grid.addWidget(self.emu_name_input, 1, 1)
        
        layout.addLayout(grid)
        layout.addStretch()
        
        self.save_emu_settings_btn = QPushButton("SAVE EMULATOR SETTINGS")
        self.save_emu_settings_btn.setStyleSheet("background-color: #8e44ad; color: white; padding: 10px;")
        layout.addWidget(self.save_emu_settings_btn)

    def _browse_emu_path(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select LDPlayer Executable", "", "Executable Files (*.exe)")
        if file_path:
            self.emu_path_input.setText(file_path)

    def _upload_template(self, res_type, level):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Template Image", "", "Image Files (*.png *.jpg)")
        if file_path:
            dest = f"assets/templates/{res_type}_lv{level}.png"
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy(file_path, dest)
            self.add_log(f"Updated template: {res_type} Level {level}")

    def _upload_ui_button(self, key):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Button Image", "", "Image Files (*.png *.jpg)")
        if file_path:
            dest = f"assets/ui/{key}.png"
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy(file_path, dest)
            self.add_log(f"Updated UI button: {key}")

    def update_status_label(self, status):
        self.status_label.setText(f"STATUS: {status.upper()}")
        if "running" in status.lower():
            self.status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #27ae60; padding: 10px; border: 2px solid #27ae60;")
        elif "error" in status.lower():
            self.status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #c0392b; padding: 10px; border: 2px solid #c0392b;")
        else:
            self.status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #7f8c8d; padding: 10px; border: 1px solid #bdc3c7;")

    def refresh_task_table(self, tasks):
        self.task_table.setRowCount(len(tasks))
        for i, task in enumerate(tasks):
            self.task_table.setItem(i, 0, QTableWidgetItem(f"Army {task['army_id']}"))
            self.task_table.setItem(i, 1, QTableWidgetItem(task['resource_type']))
            self.task_table.setItem(i, 2, QTableWidgetItem(str(task['resource_level'])))
            self.task_table.setItem(i, 3, QTableWidgetItem(f"({task['map_x']}, {task['map_y']})"))
            
            remaining = max(0, int(task['end_timestamp'] - time.time()))
            mins, secs = divmod(remaining, 60)
            self.task_table.setItem(i, 4, QTableWidgetItem(f"{mins}m {secs}s"))

    def add_log(self, message):
        row = self.log_console.rowCount()
        self.log_console.insertRow(row)
        timestamp = time.strftime("%H:%M:%S")
        self.log_console.setItem(row, 0, QTableWidgetItem(f"[{timestamp}] {message}"))
        self.log_console.scrollToBottom()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LiveDashboard()
    window.show()
    sys.exit(app.exec())
