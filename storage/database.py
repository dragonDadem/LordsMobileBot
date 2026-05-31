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
