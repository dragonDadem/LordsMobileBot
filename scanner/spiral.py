import math

class SpiralScanner:
    """
    Module 4: World Map Navigation
    Implements an adaptive spiral scanning algorithm to search for resources.
    """
    def __init__(self, start_x=512, start_y=512, step_size=1):
        self.center_x = start_x
        self.center_y = start_y
        self.step_size = step_size
        self.current_step = 0
        self.max_map_size = 1024 # Typical Lords Mobile map size

    def get_next_grid_pos(self):
        """
        Calculate the next (X, Y) coordinate in a square spiral pattern.
        """
        n = self.current_step
        
        # Calculate layer (k)
        k = math.ceil((math.sqrt(n + 1) - 1) / 2)
        if k == 0:
            x, y = 0, 0
        else:
            t = 2 * k - 1
            m = t * t
            p = n - m
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
        
        # Scale to map coordinates
        map_x = self.center_x + x * self.step_size
        map_y = self.center_y + y * self.step_size
        
        # Wrap or clamp within map bounds
        map_x = max(0, min(self.max_map_size - 1, map_x))
        map_y = max(0, min(self.max_map_size - 1, map_y))
        
        return (map_x, map_y)

    def calculate_swipe_vector(self, current_pos, target_pos, pixels_per_tile=100):
        """
        Convert map coordinate difference to screen swipe vector.
        This depends on the zoom level (pixels_per_tile).
        """
        dx = target_pos[0] - current_pos[0]
        dy = target_pos[1] - current_pos[1]
        
        # Swiping direction is opposite to map movement
        swipe_x = -dx * pixels_per_tile
        swipe_y = -dy * pixels_per_tile
        
        return (swipe_x, swipe_y)

    def reset(self):
        """Restart scanning from the center."""
        self.current_step = 0

if __name__ == "__main__":
    # Unit test for Module 4
    scanner = SpiralScanner()
    print("First 10 spiral coordinates:")
    for _ in range(10):
        print(scanner.get_next_grid_pos())
