import sqlite3
import time
import os

class TimerSystem:
    def __init__(self, db_path='storage/bot_data.db'):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize the SQLite database."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Table for active gathering tasks
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS active_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                army_id INTEGER,
                resource_type TEXT,
                resource_level INTEGER,
                start_time REAL,
                duration REAL,
                end_time REAL,
                x INTEGER,
                y INTEGER
            )
        ''')
        
        # Table for resource cooldown configurations
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resource_configs (
                resource_type TEXT,
                resource_level INTEGER,
                cooldown_seconds INTEGER,
                PRIMARY KEY (resource_type, resource_level)
            )
        ''')
        
        conn.commit()
        conn.close()

    def save_task(self, task_data):
        """Save a new gathering task to the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO active_tasks (army_id, resource_type, resource_level, start_time, duration, end_time, x, y)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            task_data['army_id'],
            task_data['resource_type'],
            task_data['resource_level'],
            task_data['start_time'],
            task_data['duration'],
            task_data['start_time'] + task_data['duration'],
            task_data.get('x', 0),
            task_data.get('y', 0)
        ))
        conn.commit()
        conn.close()

    def get_active_tasks(self):
        """Retrieve all active tasks from the database."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM active_tasks WHERE end_time > ?', (time.time(),))
        tasks = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return tasks

    def clear_expired_tasks(self):
        """Remove tasks that have finished from the active list."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM active_tasks WHERE end_time <= ?', (time.time(),))
        conn.commit()
        conn.close()

    def set_resource_cooldown(self, res_type, level, seconds):
        """Set or update the cooldown for a specific resource type and level."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO resource_configs (resource_type, resource_level, cooldown_seconds)
            VALUES (?, ?, ?)
        ''', (res_type, level, seconds))
        conn.commit()
        conn.close()

    def get_resource_cooldown(self, res_type, level):
        """Get the configured cooldown for a resource."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT cooldown_seconds FROM resource_configs WHERE resource_type = ? AND resource_level = ?', (res_type, level))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else 3600 # Default 1 hour
