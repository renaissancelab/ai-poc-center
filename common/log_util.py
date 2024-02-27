# -*- coding: utf-8 -*-
import os
from loguru import logger


LOG_DIR = os.path.expanduser("/data/logs")
LOG_FILE = os.path.join(LOG_DIR, "common.log")
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

# console
# logger.add(sys.stderr)

logger.add(LOG_FILE,  # 可以带有路径 没路径的logger会自己创建
               rotation='100MB',  # 按文件大小切割日志
               retention='30 days', # 只保留30天的日志
               #encoding='utf-8',  # 编码
               enqueue=True,     # 这使得进程安全
               colorize=True,    # 彩色显示 只要系统支持
               #format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>',
               level='DEBUG')  # 这个级别以上的才会被写入文件，包含这个级别的



