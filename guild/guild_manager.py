import time
import random
from core.logger import logger

class GuildManager:
    """Handles automated guild tasks: help and gift collection."""
    def __init__(self, emulator_manager, detector):
        self.emulator = emulator_manager
        self.detector = detector

    def check_and_help(self, capturer):
        """Detect and click the guild help icon if visible."""
        screen_img = capturer.capture_win32()
        if screen_img is None: return False
        match = self.detector.detect_ui_button(screen_img, 'guild_help')
        if match:
            logger.info(f"Guild help detected at ({match['x']}, {match['y']}). Clicking...")
            self.emulator.send_click(match['x'], match['y'])
            return True
        return False

    def collect_gifts(self, capturer):
        """
        Sequence to collect guild gifts.
        Requires several UI button templates: 'guild_icon', 'gift_tab', 'claim_all', 'close_panel'.
        """
        screen_img = capturer.capture_win32()
        if screen_img is None: return False

        # 1. Click Guild Icon
        match = self.detector.detect_ui_button(screen_img, 'guild_icon')
        if match:
            logger.info("Opening Guild menu...")
            self.emulator.send_click(match['x'], match['y'])
            time.sleep(random.uniform(2.0, 3.0))
            
            # 2. Click Gift Tab
            screen_img = capturer.capture_win32()
            if screen_img is None: return False
            match = self.detector.detect_ui_button(screen_img, 'gift_tab')
            if match:
                logger.info("Clicking Gift tab...")
                self.emulator.send_click(match['x'], match['y'])
                time.sleep(random.uniform(1.5, 2.5))

                # 3. Click Claim All
                screen_img = capturer.capture_win32()
                if screen_img is None: return False
                match = self.detector.detect_ui_button(screen_img, 'claim_all')
                if match:
                    logger.info("Claiming all gifts...")
                    self.emulator.send_click(match['x'], match['y'])
                    time.sleep(random.uniform(2.0, 3.0))

                # 4. Close Guild menu
                screen_img = capturer.capture_win32()
                if screen_img is None: return False
                match = self.detector.detect_ui_button(screen_img, 'close_panel')
                if match:
                    self.emulator.send_click(match['x'], match['y'])
                    time.sleep(random.uniform(1.0, 1.5))

                return True
        return False
