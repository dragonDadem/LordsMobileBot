import unittest
from unittest.mock import MagicMock, patch
import numpy as np

# Import modules to test
from guild.guild_manager import GuildManager
from combat.monster_hunter import MonsterHunter
from safety.protection import ProtectionSystem

class TestBotLogic(unittest.TestCase):
    def setUp(self):
        self.mock_emulator = MagicMock()
        self.mock_detector = MagicMock()
        self.mock_capturer = MagicMock()

        # Mock screen capture to return a dummy image
        self.mock_capturer.capture_win32.return_value = np.zeros((900, 1600, 3), dtype=np.uint8)

    def test_guild_collect_gifts_sequence(self):
        gm = GuildManager(self.mock_emulator, self.mock_detector)

        # Define detector responses for the sequence
        self.mock_detector.detect_ui_button.side_effect = [
            {'x': 100, 'y': 100}, # guild_icon
            {'x': 200, 'y': 200}, # gift_tab
            {'x': 300, 'y': 300}, # claim_all
            {'x': 400, 'y': 400}  # close_panel
        ]

        result = gm.collect_gifts(self.mock_capturer)

        self.assertTrue(result)
        self.assertEqual(self.mock_emulator.send_click.call_count, 4)
        self.mock_emulator.send_click.assert_any_call(100, 100)
        self.mock_emulator.send_click.assert_any_call(400, 400)

    def test_guild_check_and_help(self):
        gm = GuildManager(self.mock_emulator, self.mock_detector)
        self.mock_detector.detect_ui_button.return_value = {'x': 150, 'y': 150}

        result = gm.check_and_help(self.mock_capturer)

        self.assertTrue(result)
        self.mock_emulator.send_click.assert_called_with(150, 150)

    def test_monster_hunt_sequence(self):
        mh = MonsterHunter(self.mock_emulator, self.mock_detector)

        self.mock_detector.detect_ui_button.side_effect = [
            {'x': 500, 'y': 500}, # monster_template
            {'x': 600, 'y': 600}, # hunt_button
            {'x': 700, 'y': 700}  # attack_button
        ]

        result = mh.hunt_nearby_monster(self.mock_capturer)

        self.assertTrue(result)
        self.assertEqual(self.mock_emulator.send_click.call_count, 3)

    def test_shield_activation_sequence(self):
        ps = ProtectionSystem(self.mock_emulator, self.mock_detector)

        self.mock_detector.detect_ui_button.side_effect = [
            {'x': 10, 'y': 10},  # boost_menu
            {'x': 20, 'y': 20},  # shield_24h_item
            {'x': 30, 'y': 30}   # confirm_shield
        ]

        result = ps.activate_24h_shield(self.mock_capturer)

        self.assertTrue(result)
        self.assertTrue(ps.shield_active)
        self.assertEqual(self.mock_emulator.send_click.call_count, 3)

    def test_threat_detection(self):
        ps = ProtectionSystem(self.mock_emulator, self.mock_detector)
        dummy_screen = np.zeros((900, 1600, 3), dtype=np.uint8)

        # 1. Attack alert detected -> triggers shield
        self.mock_detector.detect_ui_button.side_effect = [
            {'x': 50, 'y': 50},  # attack_alert
            {'x': 10, 'y': 10},  # boost_menu
            {'x': 20, 'y': 20},  # shield_24h_item
            {'x': 30, 'y': 30}   # confirm_shield
        ]

        result = ps.check_for_threats(dummy_screen, self.mock_capturer)
        self.assertTrue(result)
        self.assertTrue(ps.shield_active)

if __name__ == '__main__':
    unittest.main()
