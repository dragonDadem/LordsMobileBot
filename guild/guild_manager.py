import time
import random
from core.logger import logger

class GuildManager:
    """Handles automated guild tasks: help and gift collection."""
    def __init__(self, emulator_manager, detector):
        self.emulator = emulator_manager
        self.detector = detector

    def check_and_help(self, screen_img):
        """Detect and click the guild help icon if visible."""
        match = self.detector.detect_ui_button(screen_img, 'guild_help')
        if match:
            logger.info(f"Guild help detected at ({match['x']}, {match['y']}). Clicking...")
            self.emulator.send_click(match['x'], match['y'])
            return True
        return False

    def collect_gifts(self, screen_img):
        """
        Sequence to collect guild gifts.
        Requires several UI button templates: 'guild_icon', 'gift_tab', 'claim_all'.
        """
        # 1. Click Guild Icon
        match = self.detector.detect_ui_button(screen_img, 'guild_icon')
        if match:
            logger.info("Opening Guild menu...")
            self.emulator.send_click(match['x'], match['y'])
            time.sleep(random.uniform(1.5, 2.0))
            
            # Note: This logic would continue with more steps:
            # - Detect and click Gift Tab
            # - Detect and click Claim All
            # - Close Guild menu
            return True
        return False
