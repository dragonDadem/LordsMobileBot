import subprocess
import time
import os
import win32gui
import win32con
from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from core.logger import logger

class EmulatorManager:
    """Module 1: LDPlayer Detection & Control (Enhanced with real ADB)"""
    def __init__(self, window_title="LDPlayer", exe_path=None):
        self.window_title = window_title
        self.exe_path = exe_path
        self.window_handle = None
        self.adb_device = None
        self.client_rect = (0, 0, 1600, 900)
        
    def find_ldplayer_window(self):
        """Find the LDPlayer window handle."""
        self.window_handle = win32gui.FindWindow(None, self.window_title)
        if not self.window_handle:
            # Try partial match
            def callback(hwnd, extra):
                if self.window_title in win32gui.GetWindowText(hwnd):
                    extra.append(hwnd)
            hwnds = []
            win32gui.EnumWindows(callback, hwnds)
            if hwnds:
                self.window_handle = hwnds[0]
        
        if self.window_handle:
            self.update_client_rect()
            self._connect_adb()
            return True
        return False

    def _connect_adb(self, host="127.0.0.1", port=5555):
        """Connect to LDPlayer via ADB."""
        try:
            # Ensure ADB server is running
            subprocess.run(["adb", "start-server"], capture_output=True)
            subprocess.run(["adb", "connect", f"{host}:{port}"], capture_output=True)
            
            self.adb_device = AdbDeviceTcp(host, port, default_transport_timeout_s=9.0)
            self.adb_device.connect()
            logger.info(f"Connected to ADB at {host}:{port}")
            return True
        except Exception as e:
            logger.error(f"ADB Connection failed: {e}")
            return False

    def launch_emulator(self):
        """Launch LDPlayer if not running."""
        if self.exe_path and os.path.exists(self.exe_path):
            subprocess.Popen([self.exe_path])
            logger.info(f"Launching LDPlayer from {self.exe_path}...")
            # Wait for window
            for _ in range(30):
                if self.find_ldplayer_window():
                    return True
                time.sleep(2)
        return False

    def set_window_resolution(self, width=1600, height=900):
        """Force emulator to specific resolution."""
        if self.window_handle:
            # Set window position and size (including borders)
            win32gui.SetWindowPos(self.window_handle, win32con.HWND_TOP, 100, 100, width + 16, height + 39, win32con.SWP_SHOWWINDOW)
            self.update_client_rect()

    def update_client_rect(self):
        """Get the actual game area coordinates."""
        if self.window_handle:
            rect = win32gui.GetClientRect(self.window_handle)
            point = win32gui.ClientToScreen(self.window_handle, (0, 0))
            self.client_rect = (point[0], point[1], rect[2], rect[3])

    def send_click(self, x, y):
        """Send a real ADB click command."""
        if self.adb_device:
            cmd = f"input tap {x} {y}"
            self.adb_device.shell(cmd)
            logger.debug(f"ADB Click: {x}, {y}")
        else:
            logger.warning("ADB not connected, click failed.")

    def send_swipe(self, x1, y1, x2, y2, duration=500):
        """Send a real ADB swipe command."""
        if self.adb_device:
            cmd = f"input swipe {x1} {y1} {x2} {y2} {duration}"
            self.adb_device.shell(cmd)
            logger.debug(f"ADB Swipe: ({x1},{y1}) to ({x2},{y2})")
