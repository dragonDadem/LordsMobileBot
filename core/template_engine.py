import os
import json
import shutil
from core.logger import logger

class TemplateEngine:
    """Manages the saving, loading, and metadata of templates."""
    def __init__(self, base_dir="assets/templates"):
        self.base_dir = base_dir
        self.metadata_path = os.path.join(self.base_dir, "templates.json")
        self._ensure_dirs()
        self.templates = self.load_metadata()

    def _ensure_dirs(self):
        os.makedirs(self.base_dir, exist_ok=True)
        for sub in ["resources", "ui", "shield"]:
            os.makedirs(os.path.join(self.base_dir, sub), exist_ok=True)

    def load_metadata(self):
        if os.path.exists(self.metadata_path):
            try:
                with open(self.metadata_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load template metadata: {e}")
        
        # If file missing or error, return defaults but don't save yet 
        # (waiting for user to upload images)
        return self._get_default_metadata()

    def _get_default_metadata(self):
        """Returns a list of default template entries that the user needs to provide images for."""
        defaults = []
        
        # 1. Resources (Lv 1-5)
        for res in ["Food", "Wood", "Stone", "Ore", "Gold"]:
            for lv in range(1, 6):
                name = f"{res} Lv {lv}"
                defaults.append({
                    "name": name,
                    "type": "Resources",
                    "path": "", # No image yet
                    "key": name.lower().replace(" ", "_")
                })
        
        # 2. UI Buttons
        ui_buttons = [
            "Base to World", "Open Map", "Close Panel", 
            "Auto Select", "Deploy Army", "Lowest Tier", 
            "Gather Button"
        ]
        for btn in ui_buttons:
            defaults.append({
                "name": btn,
                "type": "UI Buttons",
                "path": "",
                "key": btn.lower().replace(" ", "_")
            })
            
        # 3. Shield System
        shield_elements = ["Boost Menu", "24h Shield", "Confirm Button"]
        for item in shield_elements:
            defaults.append({
                "name": item,
                "type": "Shield System",
                "path": "",
                "key": item.lower().replace(" ", "_")
            })
            
        return defaults

    def save_template(self, name, category, source_path):
        """Copies the image to the local assets and updates metadata."""
        if not source_path or not os.path.exists(source_path):
            return None
            
        sub_folder = category.lower().replace(" ", "_")
        target_filename = f"{name.lower().replace(' ', '_')}.png"
        target_path = os.path.join(self.base_dir, sub_folder, target_filename)
        
        try:
            # Avoid copying if it's already in the target location
            if os.path.abspath(source_path) != os.path.abspath(target_path):
                shutil.copy2(source_path, target_path)
            
            # Update metadata
            entry = {
                "name": name,
                "type": category,
                "path": target_path,
                "key": name.lower().replace(' ', '_')
            }
            
            # Update existing or append new
            found = False
            for i, t in enumerate(self.templates):
                if t['name'] == name:
                    self.templates[i] = entry
                    found = True
                    break
            if not found:
                self.templates.append(entry)
                
            self._save_metadata()
            return target_path
        except Exception as e:
            logger.error(f"Failed to save template {name}: {e}")
            return None

    def _save_metadata(self):
        with open(self.metadata_path, 'w') as f:
            json.dump(self.templates, f, indent=4)

    def get_templates_by_type(self, itype):
        return [t for t in self.templates if t['type'] == itype]
