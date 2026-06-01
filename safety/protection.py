import time
from core.logger import logger

class ProtectionSystem:
    """Handles automated shielding and anti-rally alerts."""
    def __init__(self, emulator_manager, detector):
        self.emulator = emulator_manager
        self.detector = detector
        self.shield_active = False

    def check_for_threats(self, screen_img):
        """Detect incoming rallies or solo attacks."""
        # 1. Detect Rally/Attack Alert Icon (usually a red flashing border or icon)
        match = self.detector.detect_ui_button(screen_img, 'attack_alert')
        if match:
            logger.warning("ATTACK DETECTED! Initiating emergency protection...")
            self.activate_shield()
            return True
        return False

    def activate_shield(self):
        """
        Sequence to use a shield from the bag.
        Requires templates for 'bag_icon', 'shield_item', 'use_button'.
        """
        logger.info("Activating shield...")
        # 1. Open Bag
        # 2. Search for Shield
        # 3. Click Use
        self.shield_active = True
        return True
