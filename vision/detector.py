import cv2
import numpy as np
import os

class ResourceDetector:
    """
    Module 3: Resource Detection Engine (Enhanced)
    Detects resource tiles and UI buttons using image-based detection.
    """
    def __init__(self, templates_dir='assets/templates', ui_dir='assets/ui'):
        self.templates_dir = templates_dir
        self.ui_dir = ui_dir
        self.templates = {}    # { 'Gold_lv5': [img1, img2], ... }
        self.ui_templates = {} # { 'auto_select': img, ... }
        
    def load_templates(self):
        """Load all resource and UI templates from their respective directories."""
        self.templates = {}
        self.ui_templates = {}

        # Load Resource Templates
        if os.path.exists(self.templates_dir):
            for filename in os.listdir(self.templates_dir):
                if filename.endswith(".png") and "_" in filename:
                    name_parts = filename.replace(".png", "").split("_")
                    base_name = "_".join(name_parts[:2]) # e.g., Gold_lv5
                    path = os.path.join(self.templates_dir, filename)
                    template = cv2.imread(path)
                    if template is not None:
                        if base_name not in self.templates:
                            self.templates[base_name] = []
                        self.templates[base_name].append(template)

        # Load UI Button Templates
        if os.path.exists(self.ui_dir):
            for filename in os.listdir(self.ui_dir):
                if filename.endswith(".png"):
                    key = filename.replace(".png", "")
                    path = os.path.join(self.ui_dir, filename)
                    img = cv2.imread(path)
                    if img is not None:
                        self.ui_templates[key] = img
        
        print(f"Loaded {len(self.templates)} resources and {len(self.ui_templates)} UI buttons.")

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
            types = ['Gold', 'Ore', 'Wood', 'Stone', 'Food']
            levels = [5, 4, 3, 2, 1]
            priority_list = [f"{t}_lv{l}" for l in levels for t in types]

        for res_name in priority_list:
            if res_name in self.templates:
                for template in self.templates[res_name]:
                    match = self.match_template_multi_scale(screen_img, template)
                    if match:
                        match['name'] = res_name
                        return match
        return None
