import time
from core.logger import logger

class TaskScheduler:
    """Manages periodic tasks for the bot."""
    def __init__(self):
        self.tasks = {} # { 'task_name': { 'interval': seconds, 'last_run': timestamp } }

    def add_task(self, name, interval_seconds):
        self.tasks[name] = {
            'interval': interval_seconds,
            'last_run': 0
        }

    def should_run(self, name):
        if name not in self.tasks:
            return False

        now = time.time()
        task = self.tasks[name]
        if now - task['last_run'] >= task['interval']:
            return True
        return False

    def mark_run(self, name):
        if name in self.tasks:
            self.tasks[name]['last_run'] = time.time()
            logger.debug(f"Task {name} marked as run at {self.tasks[name]['last_run']}")
