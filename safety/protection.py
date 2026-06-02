import time
import random
from core.logger import logger

class ProtectionSystem:
    """Handles automated shielding and anti-rally alerts."""
    def __init__(self, emulator_manager, detector):
        self.emulator = emulator_manager
        self.detector = detector
        self.shield_active = False

    def check_for_threats(self, screen_img):
        """Detect incoming rallies or solo attacks."""
        match = self.detector.detect_ui_button(screen_img, 'attack_alert')
        if match:
            logger.warning("ATTACK DETECTED! Initiating emergency protection...")
            self.activate_24h_shield(screen_img)
            return True
        return False

    def activate_24h_shield(self, current_screen):
        """
        Full sequence to activate a 24h shield.
        Steps: Open Boosts -> Scroll -> Find Shield -> Select 24h -> Confirm.
        """
        logger.info("Starting 24h Shield activation sequence...")
        
        # 1. Click Boosts/Menu button
        match = self.detector.detect_ui_button(current_screen, 'boost_menu')
        if match:
            self.emulator.send_click(match['x'], match['y'])
            time.sleep(1.5)
            
            # 2. Scroll Up (if needed)
            # self.emulator.send_swipe(960, 700, 960, 300) 
            
            # 3. Detect Shield Icon
            # This would continue using the dynamic templates
            logger.info("Sequence initiated. Please ensure 'boost_menu' and 'shield_24h' templates are uploaded.")
            return True
        
        logger.error("Failed to find Boost Menu button.")
        return False
