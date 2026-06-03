import os
import json
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLabel, QScrollArea, QFileDialog, QLineEdit, 
                             QComboBox, QFrame, QGridLayout)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap, QFont

class TemplateRow(QFrame):
    deleted = pyqtSignal(object)
    
    def __init__(self, item_name="", image_path="", item_type="UI Button", item_key=""):
        super().__init__()
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setStyleSheet("""
            TemplateRow {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 5px;
                margin-bottom: 5px;
            }
            TemplateRow:hover {
                background-color: #e9ecef;
            }
        """)
        self.image_path = image_path
        self.item_key = item_key
        self._init_ui(item_name, item_type)

    def _init_ui(self, name, itype):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        
        # Label/Name (Fixed for pre-populated items)
        self.name_label = QLabel(name)
        self.name_label.setFixedWidth(180)
        self.name_label.setStyleSheet("font-weight: bold; color: #34495e;")
        layout.addWidget(self.name_label)
        
        # Type Label
        type_label = QLabel(f"[{itype}]")
        type_label.setFixedWidth(100)
        type_label.setStyleSheet("color: #7f8c8d; font-style: italic;")
        layout.addWidget(type_label)
        
        # Preview Label
        self.preview_label = QLabel("No Image")
        self.preview_label.setFixedSize(60, 60)
        self.preview_label.setStyleSheet("background-color: white; border: 1px dashed #bdc3c7; border-radius: 3px;")
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if self.image_path and os.path.exists(self.image_path):
            self._update_preview(self.image_path)
        layout.addWidget(self.preview_label)
        
        # Spacer
        layout.addStretch()
        
        # Upload Button
        self.upload_btn = QPushButton("Upload Image")
        self.upload_btn.setFixedWidth(120)
        self.upload_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 3px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.upload_btn.clicked.connect(self._handle_upload)
        layout.addWidget(self.upload_btn)
        
        # Status Icon
        self.status_icon = QLabel("⚪") # White for missing, Green for loaded
        if self.image_path and os.path.exists(self.image_path):
            self.status_icon.setText("🟢")
        layout.addWidget(self.status_icon)

    def _handle_upload(self):
        file_path, _ = QFileDialog.getOpenFileName(self, f"Select Image for {self.name_label.text()}", "", "Images (*.png *.jpg)")
        if file_path:
            self.image_path = file_path
            self._update_preview(file_path)
            self.status_icon.setText("🟢")

    def _update_preview(self, path):
        pixmap = QPixmap(path)
        self.preview_label.setPixmap(pixmap.scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def set_active(self, active=True):
        if active:
            self.setStyleSheet("TemplateRow { background-color: #2c3e50; border: 2px solid #3498db; }")
        else:
            self.setStyleSheet("TemplateRow { background-color: #f8f9fa; border: 1px solid #dee2e6; }")

class TemplateManagerTab(QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        
        # Title and Description
        title = QLabel("Elite Template Manager & Trainer")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setStyleSheet("color: #2c3e50; margin-top: 10px;")
        main_layout.addWidget(title)
        
        desc = QLabel("Upload images for each item below. The bot uses these to 'see' and control the game.")
        desc.setStyleSheet("color: #7f8c8d; margin-bottom: 10px;")
        main_layout.addWidget(desc)
        
        # Scroll Area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        
        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll.setWidget(self.container)
        main_layout.addWidget(self.scroll)
        
        # Pre-populate all required items
        self._populate_required_items()
        
        # Live Preview Mode
        self.live_preview_cb = QCheckBox("ENABLE LIVE TEMPLATE VERIFICATION (Highlights matches on Dashboard)")
        self.live_preview_cb.setStyleSheet("font-weight: bold; color: #e67e22; margin: 10px;")
        main_layout.addWidget(self.live_preview_cb)

        # Footer Actions
        footer = QHBoxLayout()
        self.save_btn = QPushButton("💾 SAVE & APPLY ALL TEMPLATES")
        self.save_btn.setFixedHeight(50)
        self.save_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #219150;
            }
        """)
        footer.addWidget(self.save_btn)
        main_layout.addLayout(footer)

    def _populate_required_items(self):
        # Category: Resources
        self._add_section_header("💎 RESOURCE TILES (Levels 1-5)")
        resources = ["Food", "Wood", "Stone", "Ore", "Gold"]
        for res in resources:
            for lv in range(5, 0, -1):
                name = f"{res} Mine Lv {lv}"
                key = f"{res.lower()}_lv{lv}"
                self.add_row(name, "", "Resource", key)

        # Category: Essential UI Buttons
        self._add_section_header("🎮 ESSENTIAL UI BUTTONS")
        buttons = [
            ("Exit to World Map", "exit_to_map"),
            ("Base to Map Button", "base_to_map"),
            ("Open Map Search", "open_map"),
            ("Close Map/Panel", "close_panel"),
            ("Auto-Select Army", "auto_select"),
            ("Deploy/Gather Button", "deploy_btn"),
            ("Lowest Tier Button", "lowest_tier"),
            ("Collect Resources", "collect_btn")
        ]
        for name, key in buttons:
            self.add_row(name, "", "UI Button", key)

        # Category: Guild & Gifts
        self._add_section_header("🤝 GUILD & GIFTS")
        guild_items = [
            ("Guild Icon", "guild_icon"),
            ("Guild Help Icon", "guild_help"),
            ("Gift Tab", "gift_tab"),
            ("Claim All Gifts", "claim_all")
        ]
        for name, key in guild_items:
            self.add_row(name, "", "Guild Task", key)

        # Category: Monster Hunting
        self._add_section_header("⚔️ MONSTER HUNTING")
        hunt_items = [
            ("Monster Template", "monster_template"),
            ("Hunt Button", "hunt_button"),
            ("Attack Button", "attack_button"),
            ("Attack Alert (Red)", "attack_alert")
        ]
        for name, key in hunt_items:
            self.add_row(name, "", "Combat Task", key)

        # Category: Shield System
        self._add_section_header("🛡️ SHIELD SYSTEM (24h)")
        shields = [
            ("Boost Menu Icon", "boost_menu"),
            ("24h Shield Item", "shield_24h_item"),
            ("Confirm Shield Button", "confirm_shield")
        ]
        for name, key in shields:
            self.add_row(name, "", "Shield Sequence", key)

    def _add_section_header(self, title):
        header = QLabel(title)
        header.setStyleSheet("""
            background-color: #34495e;
            color: white;
            padding: 8px;
            font-weight: bold;
            border-radius: 3px;
            margin-top: 15px;
        """)
        self.container_layout.addWidget(header)

    def add_row(self, name, path, itype, key):
        row = TemplateRow(name, path, itype, key)
        self.container_layout.addWidget(row)
        return row

    def get_all_data(self):
        data = []
        for i in range(self.container_layout.count()):
            widget = self.container_layout.itemAt(i).widget()
            if isinstance(widget, TemplateRow):
                if widget.image_path:
                    data.append({
                        "name": widget.name_label.text(),
                        "type": widget.type_combo_label_text() if hasattr(widget, 'type_combo') else "UI Button", # Simplified
                        "path": widget.image_path,
                        "key": widget.item_key
                    })
        return data

    # Helper for data extraction
    def get_ui_data(self):
        data = []
        for i in range(self.container_layout.count()):
            widget = self.container_layout.itemAt(i).widget()
            if isinstance(widget, TemplateRow):
                # We extract info even if path is empty to maintain the list, 
                # but TemplateEngine will handle the actual saving
                data.append({
                    "name": widget.name_label.text(),
                    "path": widget.image_path,
                    "key": widget.item_key,
                    "type": "Resource" if "Lv" in widget.name_label.text() else ("Shield Sequence" if "Shield" in widget.name_label.text() or "Boost" in widget.name_label.text() else "UI Button")
                })
        return data
