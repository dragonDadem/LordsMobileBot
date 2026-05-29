import time
import random

class Humanizer:
    """
    Module 7: Humanization and Safety
    Implements anti-detection behavior to make the bot appear more human-like.
    """
    
    @staticmethod
    def sleep(min_s=1.0, max_s=3.0):
        """Randomized sleep interval."""
        time.sleep(random.uniform(min_s, max_s))

    @staticmethod
    def randomize_point(x, y, radius=5):
        """Add a small random offset to a click coordinate."""
        nx = x + random.randint(-radius, radius)
        ny = y + random.randint(-radius, radius)
        return nx, ny

    @staticmethod
    def get_human_delay(base_delay):
        """Add variance to a base delay (e.g., 20% variation)."""
        variation = base_delay * 0.2
        return base_delay + random.uniform(-variation, variation)

    @staticmethod
    def jitter_swipe(x1, y1, x2, y2):
        """Add slight variations to swipe start/end points."""
        rx1, ry1 = Humanizer.randomize_point(x1, y1, radius=10)
        rx2, ry2 = Humanizer.randomize_point(x2, y2, radius=10)
        return rx1, ry1, rx2, ry2

    @staticmethod
    def random_pause():
        """Occasionally take a longer 'human-like' break."""
        if random.random() < 0.05: # 5% chance
            pause_time = random.uniform(30, 120) # 30s to 2min
            print(f"Safety: Taking a human-like break for {pause_time:.1f} seconds...")
            time.sleep(pause_time)
