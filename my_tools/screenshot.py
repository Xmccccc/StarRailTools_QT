"""
屏幕截图 - 匹配
    优先只截取软件窗口界面 - 而非全屏
"""
import my_utils

import time
# import threading
from dataclasses import dataclass
from typing import Optional, List, Dict
from paddleocr import PaddleOCR


class Screenshot:
    def __init__(self):
        self.cfg_run_path = r"..\config\cfg\cfg_run.json"
        self.cfg_run = my_utils.load_json_file(self.cfg_run_path)

        self.ocr = PaddleOCR(use_angle_cls=False, lang='ch')  # 文字识别 中文（'ch'）
        # 窗口信息
        self.window_rect = self.cfg_run['window_rect']  # (x, y, width, height)
        self.window_mode = self.cfg_run['window_mode']
        self.hwnd = None

        # img path
        self.computer = self.cfg_run['computer']
        self.img_com_path = f"../images/intf/{self.computer}"

        pass

    pass


def end_sign():
    pass


if __name__ == '__main__':
    pass
