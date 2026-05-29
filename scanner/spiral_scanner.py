import math

class SpiralScanner:
    def __init__(self, start_x=512, start_y=512, step_size=1):
        """
        Initialize the spiral scanner.
        start_x, start_y: Initial coordinates (center of the world map).
        step_size: The distance to move in each step of the spiral.
        """
        self.center_x = start_x
        self.center_y = start_y
        self.step_size = step_size
        self.current_step = 0
        self.visited_points = set()

    def get_next_coordinates(self):
        """
        Calculate the next set of coordinates in the spiral pattern.
        Using a square spiral algorithm.
        """
        # Square spiral algorithm
        # (0,0), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (2,-1) ...
        
        # Determine the ring number (n)
        # The number of steps in each ring increases: 1, 1, 2, 2, 3, 3, 4, 4...
        # Ring 0: (0,0) - 1 step
        # Ring 1: (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1) - 8 steps
        
        # Alternatively, use a simpler step-based approach:
        n = self.current_step
        
        # Layer (k) is the square layer we are in
        k = math.ceil((math.sqrt(n + 1) - 1) / 2)
        if k == 0:
            x, y = 0, 0
        else:
            # Max steps in previous layers
            t = 2 * k - 1
            m = t * t
            # Current position in the current layer
            p = n - m
            # Side length of the current layer
            s = 2 * k
            
            if p < s:
                x, y = k, p - k + 1
            elif p < 2 * s:
                x, y = k - (p - s) - 1, k
            elif p < 3 * s:
                x, y = -k, k - (p - 2 * s) - 1
            else:
                x, y = -k + (p - 3 * s) + 1, -k
        
        self.current_step += 1
        
        # Scale and offset to map coordinates
        map_x = self.center_x + x * self.step_size
        map_y = self.center_y + y * self.step_size
        
        # Ensure coordinates are within map bounds (typically 0-1023 in Lords Mobile)
        map_x = max(0, min(1023, map_x))
        map_y = max(0, min(1023, map_y))
        
        return (map_x, map_y)

    def reset(self):
        """Reset the scanner to the center."""
        self.current_step = 0
        self.visited_points.clear()

    def calculate_swipe(self, current_map_pos, target_map_pos, screen_width, screen_height):
        """
        Calculate the swipe coordinates on the screen to move from current to target map position.
        This depends on the zoom level and map scale.
        """
        # This is a simplified calculation and needs tuning based on actual game behavior.
        # map_diff_x = target_map_pos[0] - current_map_pos[0]
        # map_diff_y = target_map_pos[1] - current_map_pos[1]
        
        # In Lords Mobile, swiping left moves the map right (positive X direction).
        # We'll need to calibrate how many pixels on screen correspond to 1 map unit.
        pixels_per_unit = 100 # Placeholder value
        
        # Center of the screen
        start_x, start_y = screen_width // 2, screen_height // 2
        
        # Calculate end point for swipe (opposite direction of movement)
        # end_x = start_x - map_diff_x * pixels_per_unit
        # end_y = start_y - map_diff_y * pixels_per_unit
        
        # return (start_x, start_y, end_x, end_y)
        pass # To be implemented with actual calibration
