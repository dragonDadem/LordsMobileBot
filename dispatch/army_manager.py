import time

class ArmyManager:
    def __init__(self, emulator_manager, max_armies=6):
        self.emulator = emulator_manager
        self.max_armies = max_armies
        self.active_armies = [] # List of dicts: {'id': 1, 'resource': 'Gold', 'level': 5, 'timer': 123456789}
        self.config_coords = {
            'gather_btn': (800, 450),
            'march_btn': (900, 800),
            'confirm_btn': (800, 600),
            'army_available_check': (100, 50) # Region to check for available armies
        }

    def set_coordinates(self, key, x, y):
        """Allow manual configuration of button coordinates."""
        if key in self.config_coords:
            self.config_coords[key] = (x, y)

    def is_army_available(self):
        """
        Check if there's an available army to send.
        This would typically involve checking a specific region of the screen for an icon or text.
        """
        # Placeholder: In a real scenario, we'd use vision.detector to check the UI
        return len(self.active_armies) < self.max_armies

    def dispatch_army(self, resource_x, resource_y, resource_info):
        """
        Execute the sequence of clicks to send an army to a resource.
        resource_info: {'type': 'Gold', 'level': 5}
        """
        if not self.is_army_available():
            return False

        # 1. Click on the resource tile
        self.emulator.send_click(resource_x, resource_y)
        time.sleep(1)

        # 2. Click Gather button
        gx, gy = self.config_coords['gather_btn']
        self.emulator.send_click(gx, gy)
        time.sleep(1)

        # 3. Click March button (to select troops)
        mx, my = self.config_coords['march_btn']
        self.emulator.send_click(mx, my)
        time.sleep(1)

        # 4. Click Confirmation/March button (to actually send)
        cx, cy = self.config_coords['confirm_btn']
        self.emulator.send_click(cx, cy)
        
        # Add to active armies (timer will be managed by TimerSystem)
        army_id = len(self.active_armies) + 1
        dispatch_data = {
            'id': army_id,
            'resource': resource_info['type'],
            'level': resource_info['level'],
            'start_time': time.time()
        }
        self.active_armies.append(dispatch_data)
        return True

    def update_active_armies(self, expired_ids):
        """Remove armies that have finished gathering."""
        self.active_armies = [a for a in self.active_armies if a['id'] not in expired_ids]
