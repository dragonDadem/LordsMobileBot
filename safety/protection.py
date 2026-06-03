import time
import random
from core.logger import logger

class ProtectionSystem:
    """Handles automated shielding and anti-rally alerts."""
    def __init__(self, emulator_manager, detector):
        self.emulator = emulator_manager
        self.detector = detector
        self.shield_active = False

    def check_for_threats(self, screen_img, capturer):
        """Detect incoming rallies or solo attacks using current frame."""
        if screen_img is None: return False

        match = self.detector.detect_ui_button(screen_img, 'attack_alert')
        if match:
            logger.warning("ATTACK DETECTED! Initiating emergency protection...")
            self.activate_24h_shield(capturer)
            return True
        return False

    def activate_24h_shield(self, capturer):
        """
        Full sequence to activate a 24h shield.
        Steps: Open Boosts -> Find Shield -> Select 24h -> Confirm.
        """
        logger.info("Starting 24h Shield activation sequence...")
        
        screen_img = capturer.capture_win32()
        if screen_img is None: return False

        # 1. Click Boosts/Menu button
        match = self.detector.detect_ui_button(screen_img, 'boost_menu')
        if not match:
            logger.error("Failed to find Boost Menu button.")
            return False

        self.emulator.send_click(match['x'], match['y'])
        time.sleep(random.uniform(1.5, 2.0))

        # 2. Find and click 24h Shield item
        screen_img = capturer.capture_win32()
        if screen_img is None: return False
        match = self.detector.detect_ui_button(screen_img, 'shield_24h_item')
        if not match:
            # Try a small scroll down just in case
            logger.info("Shield not visible, attempting to scroll...")
            self.emulator.send_swipe(800, 700, 800, 400, 500)
            time.sleep(1.0)
            screen_img = capturer.capture_win32()
            match = self.detector.detect_ui_button(screen_img, 'shield_24h_item')

        if match:
            self.emulator.send_click(match['x'], match['y'])
            time.sleep(random.uniform(1.0, 1.5))
            
            # 3. Confirm Shield
            screen_img = capturer.capture_win32()
            if screen_img is None: return False
            match = self.detector.detect_ui_button(screen_img, 'confirm_shield')
            if match:
                self.emulator.send_click(match['x'], match['y'])
                logger.info("24h Shield activated successfully!")
                self.shield_active = True
                return True
        
        logger.error("Could not complete shield activation sequence.")
        return False
