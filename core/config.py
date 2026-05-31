import json
import os

class ConfigManager:
    """Manages bot settings in a JSON file for stability and ease of editing."""
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.defaults = {
            "emu_path": "C:/LDPlayer/LDPlayer9/ldplayer.exe",
            "emu_name": "LDPlayer",
            "timers": {
                "Food": {"5": 60, "4": 60, "3": 60, "2": 60, "1": 60},
                "Gold": {"5": 60, "4": 60, "3": 60, "2": 60, "1": 60},
                "Wood": {"5": 60, "4": 60, "3": 60, "2": 60, "1": 60},
                "Stone": {"5": 60, "4": 60, "3": 60, "2": 60, "1": 60},
                "Ore": {"5": 60, "4": 60, "3": 60, "2": 60, "1": 60}
            },
            "resources_to_gather": ["Food", "Gold", "Wood", "Stone", "Ore"]
        }
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    return {**self.defaults, **json.load(f)}
            except Exception as e:
                print(f"Error loading config: {e}")
        return self.defaults.copy()

    def save_config(self):
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()
