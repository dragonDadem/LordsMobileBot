import sys
import time
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTableWidget, QTableWidgetItem, 
                             QLabel, QPushButton, QHeaderView, QFrame, QStatusBar)
from PyQt6.QtCore import QTimer, Qt, pyqtSignal, QObject

class BotSignals(QObject):
    status_changed = pyqtSignal(str)
    tasks_updated = pyqtSignal(list)
    log_message = pyqtSignal(str)

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
        main_layout = QHBoxLayout(central_widget)

        # Left Panel: Controls & Status
        left_panel = QFrame()
        left_panel.setFixedWidth(300)
        left_panel.setFrameShape(QFrame.Shape.StyledPanel)
        left_layout = QVBoxLayout(left_panel)

        self.status_label = QLabel("STATUS: IDLE")
        self.status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #7f8c8d; padding: 10px; border: 1px solid #bdc3c7;")
        left_layout.addWidget(self.status_label)

        # Action Buttons
        self.start_btn = QPushButton("▶ START BOT")
        self.start_btn.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold; padding: 15px;")
        
        self.pause_btn = QPushButton("⏸ PAUSE")
        self.pause_btn.setStyleSheet("background-color: #f39c12; color: white; font-weight: bold; padding: 15px;")
        
        self.stop_btn = QPushButton("⏹ STOP BOT")
        self.stop_btn.setStyleSheet("background-color: #c0392b; color: white; font-weight: bold; padding: 15px;")

        left_layout.addWidget(self.start_btn)
        left_layout.addWidget(self.pause_btn)
        left_layout.addWidget(self.stop_btn)
        left_layout.addStretch()

        # Quick Settings / Info
        info_label = QLabel("Quick Info:\n- Res: 1600x900\n- ADB: Connected\n- Map: Scanning...")
        info_label.setStyleSheet("color: #34495e; background: #ecf0f1; padding: 10px;")
        left_layout.addWidget(info_label)

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
        self.task_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
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

        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel)

        self.setStatusBar(QStatusBar())

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
