"""
log日志信息
"""
import logging
import os
from datetime import datetime


class SimpleLogger:
    """简洁易用的日志记录器"""

    def __init__(self):
        """初始化日志记录器 """
        # 日志存储目录
        self.log_dir = r"..\logs"
        os.makedirs(self.log_dir, exist_ok=True)

        # 生成带时间的日志文件名（示例：2023-10-25_14_30_00.log）
        timestamp = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
        self.log_path = os.path.join(self.log_dir, f"{timestamp}.log")

        # 配置带前导零的时间格式
        formatter = logging.Formatter(
            fmt='[%(asctime)s] - %(levelname)s - %(message)s',
            datefmt='%Y/%m/%d %H:%M:%S'
        )

        # 初始化日志记录器
        self.logger = logging.getLogger("SimpleLogger")
        self.logger.setLevel(logging.INFO)

        # 清除旧处理器
        self.logger.handlers.clear()

        # 控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # 文件处理器
        file_handler = logging.FileHandler(self.log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


# 使用示例
if __name__ == "__main__":
    pass
