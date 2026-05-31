import logging
import os
from datetime import datetime

def setup_logger():
    """Sets up a robust logging system that writes to both file and console."""
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    log_filename = f"logs/bot_{datetime.now().strftime('%Y%m%d')}.log"
    
    # Create logger
    logger = logging.getLogger('LordsMobileBot')
    logger.setLevel(logging.DEBUG)
    
    # Create file handler
    fh = logging.FileHandler(log_filename, encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    
    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    # Add handlers
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)
        
    return logger

# Global logger instance
logger = setup_logger()
