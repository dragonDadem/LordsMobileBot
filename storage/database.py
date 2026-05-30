import sqlite3
import time
import os

class BotDatabase:
    """
    Module 6: Persistence and Timer System
    Manages persistent storage for active tasks, resource timers, and bot state.
    """
    def __init__(self, db_path='storage/bot_state.db'):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        """Create tables if they don't exist."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Table for active gathering armies
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS active_armies (
                army_id INTEGER PRIMARY KEY,
                resource_type TEXT,
                resource_level INTEGER,
                end_timestamp REAL,
                map_x INTEGER,
                map_y INTEGER
            )
        ''')
        
        # Table for resource cooldown configurations
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cooldown_configs (
                resource_type TEXT,
                resource_level INTEGER,
                duration_seconds INTEGER,
                PRIMARY KEY (resource_type, resource_level)
            )
        ''')
        
        # Table for button/UI settings (paths or coordinates)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ui_settings (
                setting_key TEXT PRIMARY KEY,
                setting_value TEXT
            )
        ''')
        
        conn.commit()
        conn.close()

    def add_active_army(self, army_id, res_type, res_level, duration, x, y):
        """Record a newly dispatched army."""
        end_time = time.time() + duration
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO active_armies 
            (army_id, resource_type, resource_level, end_timestamp, map_x, map_y)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (army_id, res_type, res_level, end_time, x, y))
        conn.commit()
        conn.close()

    def get_expired_armies(self):
        """Retrieve armies that have finished gathering."""
        now = time.time()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT army_id FROM active_armies WHERE end_timestamp <= ?', (now,))
        expired = [row[0] for row in cursor.fetchall()]
        conn.close()
        return expired

    def remove_army(self, army_id):
        """Remove an army from the active list."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM active_armies WHERE army_id = ?', (army_id,))
        conn.commit()
        conn.close()

    def get_all_active_tasks(self):
        """Get all currently active gathering tasks for the dashboard."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM active_armies')
        tasks = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return tasks

if __name__ == "__main__":
    # Unit test for Module 6
    db = BotDatabase()
    db.add_active_army(1, 'Gold', 5, 3600, 233, 812)
    print(f"Active Tasks: {db.get_all_active_tasks()}")

    def update_cooldown(self, res_type, level, seconds):
        """Update the cooldown for a specific resource and level."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO cooldown_configs (resource_type, resource_level, duration_seconds)
            VALUES (?, ?, ?)
        ''', (res_type, level, seconds))
        conn.commit()
        conn.close()

    def get_all_cooldowns(self):
        """Retrieve all cooldown settings."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cooldown_configs')
        configs = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return configs

    def update_ui_setting(self, key, value):
        """Update a general UI/Button setting."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO ui_settings (setting_key, setting_value) VALUES (?, ?)', (key, value))
        conn.commit()
        conn.close()

    def get_ui_setting(self, key):
        """Retrieve a specific UI setting."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT setting_value FROM ui_settings WHERE setting_key = ?', (key,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
