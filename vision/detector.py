import cv2
import numpy as np
import os
import json
from core.logger import logger

class ResourceDetector:
    """
    Module 3: Resource Detection Engine (Dynamic)
    Uses metadata from TemplateEngine to detect resources and UI elements.
    """
    def __init__(self, metadata_path='assets/templates/templates.json'):
        self.metadata_path = metadata_path
        self.templates = {}    # { 'gold_lv5': [img], ... }
        self.ui_templates = {} # { 'boost_menu': img, ... }
        self.load_templates()
        
    def load_templates(self):
        """Load all templates based on the metadata JSON."""
        self.templates = {}
        self.ui_templates = {}
        
        if not os.path.exists(self.metadata_path):
            logger.warning("No template metadata found. Template Manager needs to save templates first.")
            return

        try:
            with open(self.metadata_path, 'r') as f:
                metadata = json.load(f)
                
            for entry in metadata:
                path = entry['path']
                key = entry['key']
                itype = entry['type']
                
                if not os.path.exists(path):
                    continue
                    
                img = cv2.imread(path)
                if img is None:
                    continue
                    
                if itype == "Resource":
                    if key not in self.templates:
                        self.templates[key] = []
                    self.templates[key].append(img)
                else:
                    self.ui_templates[key] = img
                    
            logger.info(f"Detector loaded {len(self.templates)} resources and {len(self.ui_templates)} UI elements.")
        except Exception as e:
            logger.error(f"Error loading templates in detector: {e}")

    def match_template_multi_scale(self, screen_img, template, threshold=0.8):
        """Multi-scale template matching to handle variations."""
        best_match = None
        gray_screen = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        t_h, t_w = gray_template.shape[:2]

        for scale in np.linspace(0.8, 1.2, 5):
            resized_w = int(t_w * scale)
            resized_h = int(t_h * scale)
            if resized_w > gray_screen.shape[1] or resized_h > gray_screen.shape[0]:
                continue
            resized_t = cv2.resize(gray_template, (resized_w, resized_h))
            res = cv2.matchTemplate(gray_screen, resized_t, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)

            if max_val >= threshold:
                if best_match is None or max_val > best_match['confidence']:
                    best_match = {
                        'x': max_loc[0] + resized_w // 2,
                        'y': max_loc[1] + resized_h // 2,
                        'confidence': max_val
                    }
        return best_match

    def detect_ui_button(self, screen_img, button_key):
        """Detect a specific UI button by its key."""
        if button_key in self.ui_templates:
            return self.match_template_multi_scale(screen_img, self.ui_templates[button_key])
        return None

    def detect_best_resource(self, screen_img, priority_list=None):
        """Scan for resources based on priority."""
        if priority_list is None:
            # Default priority if none provided
            priority_list = list(self.templates.keys())

        for res_name in priority_list:
            if res_name in self.templates:
                for template in self.templates[res_name]:
                    match = self.match_template_multi_scale(screen_img, template)
                    if match:
                        match['name'] = res_name
                        return match
        return None
