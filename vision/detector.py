import cv2
import numpy as np
import os

class ResourceDetector:
    """
    Module 3: Resource Detection Engine
    Detects resource tiles using image-based detection (OpenCV).
    Prioritizes higher levels and supports multi-scale matching.
    """
    def __init__(self, templates_dir='assets/templates'):
        self.templates_dir = templates_dir
        self.templates = {} # Format: { 'Gold_lv5': [img1, img2], ... }
        
    def load_templates(self):
        """
        Load all template images from the assets directory.
        Supports multiple templates per resource for better robustness.
        """
        if not os.path.exists(self.templates_dir):
            os.makedirs(self.templates_dir)
            print(f"Created templates directory at {self.templates_dir}. Please add template images.")
            return

        for filename in os.listdir(self.templates_dir):
            if filename.endswith(".png"):
                # Expecting format: ResourceName_lvX_vY.png (e.g., Gold_lv5_1.png)
                name_parts = filename.replace(".png", "").split("_")
                base_name = "_".join(name_parts[:2]) # e.g., Gold_lv5
                
                path = os.path.join(self.templates_dir, filename)
                template = cv2.imread(path)
                if template is not None:
                    if base_name not in self.templates:
                        self.templates[base_name] = []
                    self.templates[base_name].append(template)
        
        print(f"Loaded {len(self.templates)} resource types/levels.")

    def match_template_multi_scale(self, screen_img, template, threshold=0.8):
        """
        Perform multi-scale template matching to handle zoom/resolution variations.
        """
        best_match = None
        gray_screen = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        t_h, t_w = gray_template.shape[:2]

        # Scales to check (from 80% to 120% of original size)
        for scale in np.linspace(0.8, 1.2, 5):
            resized_w = int(t_w * scale)
            resized_h = int(t_h * scale)
            
            # Skip if template becomes larger than screen
            if resized_w > gray_screen.shape[1] or resized_h > gray_screen.shape[0]:
                continue
                
            resized_t = cv2.resize(gray_template, (resized_w, resized_h))
            res = cv2.matchTemplate(gray_screen, resized_t, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            if max_val >= threshold:
                if best_match is None or max_val > best_match['confidence']:
                    best_match = {
                        'x': max_loc[0] + resized_w // 2,
                        'y': max_loc[1] + resized_h // 2,
                        'confidence': max_val,
                        'width': resized_w,
                        'height': resized_h
                    }
        
        return best_match

    def detect_best_resource(self, screen_img, priority_list=None):
        """
        Scan for resources based on priority.
        Default Priority: Level 5 -> 4 -> 3 -> 2 -> 1
        """
        if priority_list is None:
            # Default priority logic: check Lv5 first, then Lv4, etc.
            types = ['Gold', 'Ore', 'Wood', 'Stone', 'Food']
            levels = [5, 4, 3, 2, 1]
            priority_list = [f"{t}_lv{l}" for l in levels for t in types]

        for res_name in priority_list:
            if res_name in self.templates:
                for template in self.templates[res_name]:
                    match = self.match_template_multi_scale(screen_img, template)
                    if match:
                        # Found a high-priority resource, return it immediately
                        match['name'] = res_name
                        return match
        
        return None

if __name__ == "__main__":
    # Unit test for Module 3
    detector = ResourceDetector()
    detector.load_templates()
    # test_img = cv2.imread('test_screen.png')
    # if test_img is not None:
    #     result = detector.detect_best_resource(test_img)
    #     print(f"Detected: {result}")
