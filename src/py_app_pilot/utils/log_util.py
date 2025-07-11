import os
import time
import uuid

from loguru import logger

log_path = os.path.join(os.getcwd(), 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_error = os.path.join(log_path, f'app_manager.log')

logger.add(log_path_error, rotation='50MB', encoding='utf-8', enqueue=True, compression='zip')
