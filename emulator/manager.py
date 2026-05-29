import os
import time
import win32gui
import win32process
import subprocess
from adb_shell.auth.sign_python_rsa import PythonRSASigner
from adb_shell.adb_device import AdbDeviceTcp

class EmulatorManager:
    """
    Module 1: LDPlayer Detection and Control
    This module handles finding the LDPlayer window, managing its resolution, 
    and establishing an ADB connection for low-level control.
    """
    def __init__(self, adb_host='127.0.0.1', adb_port=5555):
        self.adb_host = adb_host
        self.adb_port = adb_port
        self.device = None
        self.window_handle = None
        self.client_rect = None

    def find_ldplayer_window(self):
        """
        Automatically detect running LDPlayer windows.
        Requirement: Track the emulator window precisely even if moved.
        """
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                # LDPlayer windows usually contain "LDPlayer" in the title
                if "LDPlayer" in title:
                    hwnds.append(hwnd)
            return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        if hwnds:
            # For now, we select the first instance found
            self.window_handle = hwnds[0]
            print(f"Detected LDPlayer Window: {win32gui.GetWindowText(self.window_handle)}")
            self.update_client_rect()
            return True
        return False

    def set_window_resolution(self, width=1600, height=900):
        """
        Force the emulator window resolution to exactly 1600x900.
        Note: This resizes the window frame. Internal game resolution 
        should also be set to 1600x900 in LDPlayer settings for consistency.
        """
        if self.window_handle:
            # Move window to (100, 100) and resize
            win32gui.MoveWindow(self.window_handle, 100, 100, width, height, True)
            self.update_client_rect()
            print(f"Window resolution set to {width}x{height}")
            return True
        return False

    def update_client_rect(self):
        """
        Calculate accurate coordinate offsets for the client area.
        Restrict actions strictly inside the emulator client area.
        """
        if self.window_handle:
            # GetClientRect returns (0, 0, width, height) of the inner area
            left, top, right, bottom = win32gui.GetClientRect(self.window_handle)
            # ClientToScreen converts (0,0) of client area to screen coordinates
            point = win32gui.ClientToScreen(self.window_handle, (left, top))
            self.client_rect = {
                'x': point[0],
                'y': point[1],
                'width': right - left,
                'height': bottom - top
            }
            print(f"Updated Client Rect: {self.client_rect}")

    def connect_adb(self):
        """
        Establish ADB connection to the LDPlayer instance.
        Uses adb-shell for pure-python communication.
        """
        try:
            # ADB Key handling
            adb_key_path = os.path.expanduser('~/.android/adbkey')
            if not os.path.exists(adb_key_path):
                # Ensure keys exist
                subprocess.run(['adb', 'start-server'], capture_output=True)
            
            with open(adb_key_path) as f:
                priv = f.read()
            with open(adb_key_path + '.pub') as f:
                pub = f.read()
            signer = PythonRSASigner(pub, priv)
            
            self.device = AdbDeviceTcp(self.adb_host, self.adb_port, default_transport_timeout_s=9.)
            self.device.connect(rsa_keys=[signer], auth_timeout_s=5)
            print(f"Connected to ADB at {self.adb_host}:{self.adb_port}")
            return True
        except Exception as e:
            print(f"ADB Connection Error: {e}")
            return False

    def get_relative_coords(self, screen_x, screen_y):
        """Convert screen coordinates to client-area relative coordinates."""
        if self.client_rect:
            return (screen_x - self.client_rect['x'], screen_y - self.client_rect['y'])
        return None

    def get_screen_coords(self, client_x, client_y):
        """Convert client-area coordinates to global screen coordinates."""
        if self.client_rect:
            return (self.client_rect['x'] + client_x, self.client_rect['y'] + client_y)
        return None

if __name__ == "__main__":
    # Unit test for Module 1
    manager = EmulatorManager()
    if manager.find_ldplayer_window():
        manager.set_window_resolution(1600, 900)
        # manager.connect_adb() # Uncomment to test ADB connection
    else:
        print("LDPlayer not found. Please ensure it is running.")
