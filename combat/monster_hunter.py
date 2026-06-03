import time
import random
from core.logger import logger

class MonsterHunter:
    """Handles basic monster hunting: finding monsters and attacking."""
    def __init__(self, emulator_manager, detector):
        self.emulator = emulator_manager
        self.detector = detector

    def hunt_nearby_monster(self, capturer):
        """
        Scan for monsters on the screen and initiate attack.
        Requires monster templates and 'hunt_button', 'attack_button'.
        """
        screen_img = capturer.capture_win32()
        if screen_img is None: return False

        # 1. Detect any monster on screen
        match = self.detector.detect_ui_button(screen_img, 'monster_template')
        if match:
            logger.info(f"Monster detected at ({match['x']}, {match['y']}).")
            self.emulator.send_click(match['x'], match['y'])
            time.sleep(random.uniform(2.0, 2.5))
            
            # 2. Click Hunt button
            screen_img = capturer.capture_win32()
            if screen_img is None: return False
            match = self.detector.detect_ui_button(screen_img, 'hunt_button')
            if match:
                logger.info("Clicking Hunt button...")
                self.emulator.send_click(match['x'], match['y'])
                time.sleep(random.uniform(1.5, 2.0))

                # 3. Click Attack button
                screen_img = capturer.capture_win32()
                if screen_img is None: return False
                match = self.detector.detect_ui_button(screen_img, 'attack_button')
                if match:
                    logger.info("Executing Monster Attack!")
                    self.emulator.send_click(match['x'], match['y'])
                    time.sleep(random.uniform(1.0, 1.5))
                    return True
        return False

    def check_energy(self, screen_img):
        """Check if there's enough energy to hunt."""
        # Detect energy bar or value
        return True
