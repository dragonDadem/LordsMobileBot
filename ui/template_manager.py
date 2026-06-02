import os
import shutil
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLabel, QScrollArea, QFileDialog, QLineEdit, 
                             QComboBox, QFrame)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

class TemplateRow(QFrame):
    deleted = pyqtSignal(object)
    
    def __init__(self, item_name="", image_path="", item_type="UI Button"):
        super().__init__()
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_path = image_path
        self._init_ui(item_name, item_type)

    def _init_ui(self, name, itype):
        layout = QHBoxLayout(self)
        
        # Name Input
        self.name_input = QLineEdit(name)
        self.name_input.setPlaceholderText("Item Name (e.g. Gold Lv5)")
        layout.addWidget(self.name_input, 2)
        
        # Type Selection
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Resource", "UI Button", "Shield Sequence"])
        self.type_combo.setCurrentText(itype)
        layout.addWidget(self.type_combo, 1)
        
        # Preview Label
        self.preview_label = QLabel("No Image")
        self.preview_label.setFixedSize(50, 50)
        self.preview_label.setStyleSheet("border: 1px solid gray;")
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if self.image_path and os.path.exists(self.image_path):
            self._update_preview(self.image_path)
        layout.addWidget(self.preview_label)
        
        # Upload Button
        self.upload_btn = QPushButton("Upload")
        self.upload_btn.clicked.connect(self._handle_upload)
        layout.addWidget(self.upload_btn)
        
        # Delete Button
        self.delete_btn = QPushButton("🗑")
        self.delete_btn.setStyleSheet("color: red;")
        self.delete_btn.clicked.connect(lambda: self.deleted.emit(self))
        layout.addWidget(self.delete_btn)

    def _handle_upload(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Template Image", "", "Images (*.png *.jpg)")
        if file_path:
            # Logic for saving will be handled by parent, but update preview now
            self.image_path = file_path
            self._update_preview(file_path)

    def _update_preview(self, path):
        pixmap = QPixmap(path)
        self.preview_label.setPixmap(pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))

class TemplateManagerTab(QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        
        # Header
        header = QLabel("Dynamic Template Manager")
        header.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(header)
        
        # Scroll Area for Rows
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll.setWidget(self.container)
        layout.addWidget(self.scroll)
        
        # Bottom Controls
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("+ Add New Template")
        self.add_btn.clicked.connect(self.add_row)
        
        self.save_btn = QPushButton("💾 SAVE ALL TEMPLATES")
        self.save_btn.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold; height: 40px;")
        
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.save_btn)
        layout.addLayout(btn_layout)

    def add_row(self, name="", path="", itype="UI Button"):
        row = TemplateRow(name, path, itype)
        row.deleted.connect(self._remove_row)
        self.container_layout.addWidget(row)
        return row

    def _remove_row(self, row):
        self.container_layout.removeWidget(row)
        row.deleteLater()

    def get_all_data(self):
        data = []
        for i in range(self.container_layout.count()):
            widget = self.container_layout.itemAt(i).widget()
            if isinstance(widget, TemplateRow):
                data.append({
                    "name": widget.name_input.text(),
                    "type": widget.type_combo.currentText(),
                    "path": widget.image_path
                })
        return data
