import sqlite3
import time
import os

class BotDatabase:
    """Manages persistent state for gathering armies and bot settings."""
    def __init__(self, db_path="storage/bot_state.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            # Table for active armies
            conn.execute('''CREATE TABLE IF NOT EXISTS active_armies (
                army_id INTEGER PRIMARY KEY,
                resource_type TEXT,
                resource_level INTEGER,
                end_timestamp REAL,
                map_x INTEGER,
                map_y INTEGER
            )''')
            
            # Table for resource cooldowns (custom timers)
            conn.execute('''CREATE TABLE IF NOT EXISTS resource_cooldowns (
                resource_type TEXT,
                resource_level INTEGER,
                duration_seconds INTEGER,
                PRIMARY KEY (resource_type, resource_level)
            )''')
            
            # Table for generic UI settings
            conn.execute('''CREATE TABLE IF NOT EXISTS ui_settings (
                setting_key TEXT PRIMARY KEY,
                setting_value TEXT
            )''')
            
            # Table for Map Memory (Discovering resources)
            conn.execute('''CREATE TABLE IF NOT EXISTS map_memory (
                x INTEGER,
                y INTEGER,
                resource_type TEXT,
                resource_level INTEGER,
                discovered_at REAL,
                PRIMARY KEY (x, y)
            )''')
            
            # Table for Collection Statistics
            conn.execute('''CREATE TABLE IF NOT EXISTS stats (
                resource_type TEXT PRIMARY KEY,
                total_collected INTEGER DEFAULT 0
            )''')
            
            # Initialize stats if empty
            for res in ['food', 'wood', 'stone', 'ore', 'gold']:
                conn.execute("INSERT OR IGNORE INTO stats (resource_type, total_collected) VALUES (?, 0)", (res,))

    def add_active_army(self, army_id, res_type, level, duration, x, y):
        end_time = time.time() + duration
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''INSERT OR REPLACE INTO active_armies 
                          VALUES (?, ?, ?, ?, ?, ?)''', 
                          (army_id, res_type, level, end_time, x, y))

    def get_all_active_tasks(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM active_armies")
            return [dict(row) for row in cursor.fetchall()]

    def get_expired_armies(self):
        now = time.time()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT army_id FROM active_armies WHERE end_timestamp <= ?", (now,))
            return [row[0] for row in cursor.fetchall()]

    def remove_army(self, army_id):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM active_armies WHERE army_id = ?", (army_id,))

    def update_cooldown(self, res_type, level, seconds):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''INSERT OR REPLACE INTO resource_cooldowns 
                          VALUES (?, ?, ?)''', (res_type, level, seconds))

    def get_all_cooldowns(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM resource_cooldowns")
            return [dict(row) for row in cursor.fetchall()]

    def update_ui_setting(self, key, value):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''INSERT OR REPLACE INTO ui_settings 
                          VALUES (?, ?)''', (key, str(value)))

    def get_ui_setting(self, key, default=None):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("SELECT setting_value FROM ui_settings WHERE setting_key = ?", (key,))
                row = cursor.fetchone()
                return row[0] if row else default
        except:
            return default

    def save_resource_to_memory(self, x, y, res_type, level):
        """Save a discovered resource location to memory."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''INSERT OR REPLACE INTO map_memory 
                          VALUES (?, ?, ?, ?, ?)''', (x, y, res_type, level, time.time()))

    def get_best_from_memory(self, preferred_types, min_level=1):
        """Find the best resource in memory that isn't too old."""
        now = time.time()
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            # Only consider resources found in the last 2 hours
            placeholders = ', '.join(['?'] * len(preferred_types))
            query = f"""SELECT * FROM map_memory 
                        WHERE resource_type IN ({placeholders}) 
                        AND resource_level >= ? 
                        AND discovered_at > ? 
                        ORDER BY resource_level DESC, discovered_at DESC LIMIT 1"""
            cursor = conn.execute(query, (*preferred_types, min_level, now - 7200))
            row = cursor.fetchone()
            return dict(row) if row else None

    def increment_stat(self, res_type, amount=1):
        """Increment the total collected count for a resource."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("UPDATE stats SET total_collected = total_collected + ? WHERE resource_type = ?", (amount, res_type))

    def get_all_stats(self):
        """Get all collection statistics."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT * FROM stats")
            return {row[0]: row[1] for row in cursor.fetchall()}
