import cv2
import numpy as np
import win32gui
import win32ui
import win32con

class ScreenCapture:
    """
    Module 2: Screen Capture System
    This module handles capturing ONLY the emulator game region with high performance.
    """
    def __init__(self, window_handle):
        self.window_handle = window_handle

    def capture_win32(self):
        """
        Capture the client area of the window using Windows API.
        This is generally faster than ADB screencap for real-time analysis.
        """
        if not self.window_handle:
            return None

        # Get client area dimensions
        left, top, right, bottom = win32gui.GetClientRect(self.window_handle)
        w = right - left
        h = bottom - top

        # Create device contexts
        hwnd_dc = win32gui.GetWindowDC(self.window_handle)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()

        # Create bitmap object
        save_bit_map = win32ui.CreateBitmap()
        save_bit_map.CreateCompatibleBitmap(mfc_dc, w, h)
        save_dc.SelectObject(save_bit_map)

        # Copy screen to bitmap
        # PW_RENDERFULLCONTENT = 2 (Captures even if window is partially obscured)
        result = save_dc.BitBlt((0, 0), (w, h), mfc_dc, (0, 0), win32con.SRCCOPY)
        
        # Convert to numpy array for OpenCV
        signed_ints_array = save_bit_map.GetBitmapBits(True)
        img = np.frombuffer(signed_ints_array, dtype='uint8')
        img.shape = (h, w, 4)

        # Cleanup
        win32gui.DeleteObject(save_bit_map.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(self.window_handle, hwnd_dc)

        # Drop alpha channel and return BGR
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    def capture_adb(self, device):
        """
        Fallback/Alternative: Capture screen using ADB.
        Useful if Win32 capture fails or for cross-platform stability.
        """
        if not device:
            return None
            
        raw_data = device.screencap()
        if raw_data:
            nparr = np.frombuffer(raw_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            return img
        return None

if __name__ == "__main__":
    # Unit test for Module 2
    from emulator.manager import EmulatorManager
    
    manager = EmulatorManager()
    if manager.find_ldplayer_window():
        capturer = ScreenCapture(manager.window_handle)
        screenshot = capturer.capture_win32()
        if screenshot is not None:
            print(f"Successfully captured image: {screenshot.shape}")
            # cv2.imwrite('debug_capture.png', screenshot)
        else:
            print("Failed to capture screen.")
    else:
        print("LDPlayer not found.")
