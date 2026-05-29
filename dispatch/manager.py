import time
import random

class ArmyDispatcher:
    """
    Module 5: Army Dispatch and UI Interaction
    Handles the sequence of clicks to send armies to resource tiles.
    """
    def __init__(self, emulator_manager):
        self.emulator = emulator_manager
        # Default coordinates (should be configured by user)
        self.coords = {
            'gather_button': (800, 450),
            'march_button': (1400, 800),
            'confirm_button': (1200, 700),
            'army_status_icon': (100, 50)
        }

    def set_custom_coords(self, key, x, y):
        """Allow the user to override button coordinates."""
        if key in self.coords:
            self.coords[key] = (x, y)

    def check_army_availability(self, detector, screen_img):
        """
        Check if there are available armies to dispatch.
        Uses the detector to look for the 'available' icon or text.
        """
        # Placeholder logic: in reality, this would use detector.match_template
        # to see if the 'available' slot is visible.
        return True 

    def dispatch_to_tile(self, tile_x, tile_y):
        """
        Executes the full click sequence to send an army.
        """
        try:
            # 1. Click the detected resource tile
            print(f"Clicking resource tile at ({tile_x}, {tile_y})")
            self.emulator.send_click(tile_x, tile_y)
            time.sleep(random.uniform(1.0, 1.5))

            # 2. Click 'Gather' button
            gx, gy = self.coords['gather_button']
            print(f"Clicking Gather button at ({gx}, {gy})")
            self.emulator.send_click(gx, gy)
            time.sleep(random.uniform(1.0, 1.5))

            # 3. Click 'March' button
            mx, my = self.coords['march_button']
            print(f"Clicking March button at ({mx}, {my})")
            self.emulator.send_click(mx, my)
            time.sleep(random.uniform(1.0, 1.5))

            # 4. Click 'Confirm' button
            cx, cy = self.coords['confirm_button']
            print(f"Clicking Confirm button at ({cx}, {cy})")
            self.emulator.send_click(cx, cy)
            
            return True
        except Exception as e:
            print(f"Dispatch Error: {e}")
            return False

if __name__ == "__main__":
    # Unit test for Module 5
    from emulator.manager import EmulatorManager
    manager = EmulatorManager()
    # manager.find_ldplayer_window()
    dispatcher = ArmyDispatcher(manager)
    # dispatcher.dispatch_to_tile(500, 500)
