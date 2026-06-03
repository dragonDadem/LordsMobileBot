import time

class StatsManager:
    """Tracks bot performance statistics."""
    def __init__(self):
        self.resources = {
            "Food": 0,
            "Wood": 0,
            "Stone": 0,
            "Ore": 0,
            "Gold": 0
        }
        self.monsters_hunted = 0
        self.guild_helps = 0
        self.gifts_collected = 0
        self.start_time = time.time()

    def add_resource(self, res_type, amount):
        if res_type in self.resources:
            self.resources[res_type] += amount

    def add_hunt(self):
        self.monsters_hunted += 1

    def add_help(self):
        self.guild_helps += 1

    def add_gift(self):
        self.gifts_collected += 1

    def get_uptime_str(self):
        uptime = int(time.time() - self.start_time)
        hours, rem = divmod(uptime, 3600)
        minutes, seconds = divmod(rem, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def get_summary(self):
        return {
            "uptime": self.get_uptime_str(),
            "resources": self.resources,
            "monsters": self.monsters_hunted,
            "helps": self.guild_helps,
            "gifts": self.gifts_collected
        }
