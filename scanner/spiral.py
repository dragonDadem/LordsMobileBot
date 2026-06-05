import time
import math
from core.logger import logger

class GridScanner:
    """
    Module 4: Optimized Grid-based World Map Scanner.
    Implements a spiral pattern with swipe control for map navigation.
    """
    def __init__(self, emulator, start_x=512, start_y=512):
        self.emu = emulator
        self.current_x = start_x
        self.current_y = start_y
        self.step_size = 5 # How many game tiles to move per swipe
        self.direction = 0 # 0: Right, 1: Down, 2: Left, 3: Up
        self.steps_in_direction = 1
        self.current_step_count = 0
        self.change_direction_count = 0
        self.max_map_size = 1024

    def move_next(self):
        """Move to the next grid position in a spiral pattern."""
        dx, dy = 0, 0
        if self.direction == 0: dx = self.step_size # Right
        elif self.direction == 1: dy = self.step_size # Down
        elif self.direction == 2: dx = -self.step_size # Left
        elif self.direction == 3: dy = -self.step_size # Up

        # Convert tile movement to swipe pixels (Rough estimation for 1600x900)
        # Center of the screen
        center_x, center_y = 800, 450
        # Invert dx/dy for map dragging (pull map to move camera)
        # 20 pixels per tile is a rough estimate for standard zoom
        swipe_x = center_x - (dx * 20) 
        swipe_y = center_y - (dy * 20)

        self.emu.send_swipe(center_x, center_y, swipe_x, swipe_y, duration=600)
        self.current_x += dx
        self.current_y += dy
        
        # Spiral logic
        self.current_step_count += 1
        if self.current_step_count >= self.steps_in_direction:
            self.current_step_count = 0
            self.direction = (self.direction + 1) % 4
            self.change_direction_count += 1
            if self.change_direction_count % 2 == 0:
                self.steps_in_direction += 1
        
        # Keep within map bounds
        self.current_x = max(0, min(self.max_map_size - 1, self.current_x))
        self.current_y = max(0, min(self.max_map_size - 1, self.current_y))
        
        logger.info(f"Scanner moved to approx Map Coord: ({self.current_x}, {self.current_y})")
        time.sleep(1.5) # Wait for map to settle

    def reset(self):
        """Restart scanning from the center."""
        self.current_x = 512
        self.current_y = 512
        self.direction = 0
        self.steps_in_direction = 1
        self.current_step_count = 0
        self.change_direction_count = 0
