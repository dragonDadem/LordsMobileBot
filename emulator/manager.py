import os
import time
import win32gui
import win32process
import subprocess
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.adb_device import AdbDeviceTcp

class EmulatorManager:
    """
    Module 1: LDPlayer Detection and Control (Enhanced)
    Handles window finding, resolution setting, and ADB connection.
    """
    def __init__(self, window_title="LDPlayer", exe_path=None, adb_host='127.0.0.1', adb_port=5555):
        self.window_title = window_title
        self.exe_path = exe_path
        self.adb_host = adb_host
        self.adb_port = adb_port
        self.device = None
        self.window_handle = None
        self.client_rect = None

    def find_ldplayer_window(self):
        """Search for the emulator window by its title."""
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                if self.window_title in title:
                    hwnds.append(hwnd)
            return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        if hwnds:
            self.window_handle = hwnds[0]
            self.update_client_rect()
            return True
        return False

    def launch_emulator(self):
        """Launch the emulator if path is provided."""
        if self.exe_path and os.path.exists(self.exe_path):
            try:
                subprocess.Popen(self.exe_path)
                # Wait a bit for window to appear
                for _ in range(30):
                    if self.find_ldplayer_window():
                        return True
                    time.sleep(1)
            except Exception as e:
                print(f"Failed to launch emulator: {e}")
        return False

    def set_window_resolution(self, width=1600, height=900):
        """Force the emulator window resolution."""
        if self.window_handle:
            win32gui.MoveWindow(self.window_handle, 100, 100, width, height, True)
            self.update_client_rect()
            return True
        return False

    def update_client_rect(self):
        """Calculate accurate coordinate offsets for the client area."""
        if self.window_handle:
            left, top, right, bottom = win32gui.GetClientRect(self.window_handle)
            point = win32gui.ClientToScreen(self.window_handle, (left, top))
            self.client_rect = {
                'x': point[0],
                'y': point[1],
                'width': right - left,
                'height': bottom - top
            }

    def send_click(self, x, y):
        """Send a click via ADB if available, else Win32 (fallback)."""
        # Note: This is a placeholder for actual click logic
        # In a real scenario, you'd use self.device.shell(f'input tap {x} {y}')
        print(f"Clicking at ({x}, {y})")
        pass
