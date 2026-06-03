import cv2
import numpy as np
from core.logger import logger

class SceneDetector:
    """Identifies the current game state/scene."""
    def __init__(self, detector):
        self.detector = detector
        self.scenes = {
            'BASE': ['base_to_map', 'guild_icon'],
            'MAP': ['exit_to_map', 'open_map'],
            'LOADING': ['loading_indicator'],
            'AD': ['close_panel']
        }

    def detect_current_scene(self, screen_img):
        """Returns the detected scene name."""
        for scene, keys in self.scenes.items():
            for key in keys:
                if self.detector.detect_ui_button(screen_img, key):
                    return scene
        return "UNKNOWN"

    def is_on_map(self, screen_img):
        return self.detect_current_scene(screen_img) == "MAP"

    def is_in_base(self, screen_img):
        return self.detect_current_scene(screen_img) == "BASE"
