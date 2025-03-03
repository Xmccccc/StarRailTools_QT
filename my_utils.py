# utils 基础组件 - 可通用
import os
import sys
import time
import json
import ctypes
# import threading
import tkinter as tk
# from tkinter import ttk

# import psutil
import win32gui
import win32con
import numpy as np

import cv2
import pyautogui
from paddleocr import PaddleOCR
# import pygetwindow as gw
# import pywinauto
# from pywinauto import application


# from pywinauto import mouse


class InfoShow:  # InfoShow
    def __init__(self, parent):
        """
        信息显示
            - 左下角显示当前状态： 当前任务、位置、状态、、、
            - 空心框标记识别位置
        """
        self.parent = parent  # tk
        self.text = self.parent.text

        # 创建顶层窗口 - 独立子窗口 - 空心框创建
        self.canvas_window = tk.Toplevel()
        self._init_canvas_window()  # # 初始化空心框窗口

        # 创建顶层窗口 - 独立子窗口 - 信息显示窗口
        self.info_window = tk.Toplevel()
        self._init_info_window()  # # 初始化信息窗口

    def _init_canvas_window(self):
        self.canvas_window.geometry(f"{0}x{0}+{0}+{0}")  # 设置窗口尺寸位置
        self.canvas_window.overrideredirect(True)  # 去除标题栏及边框 - 无边框窗口
        self.canvas_window.attributes('-topmost', True)  # 窗口置顶显示 - 显示在其他窗口前面
        self.canvas_window.attributes('-transparentcolor', 'white')  # 设置窗口白色部分透明 - 空心效果

        self.canvas = tk.Canvas(self.canvas_window, bg='white', highlightthickness=0)  # white

        # 设置鼠标穿透 - 空心框穿透
        if sys.platform == 'win32':  # 判断是否为windows系统
            self._set_click_through_win()

    def _init_info_window(self):
        """初始化信息显示窗口"""
        info_width = 200  # 信息窗口宽度
        info_height = 400  # 信息窗口高度
        label_bg = '#404040'  # 深灰色背景-2C2C2C  404040  white

        # 获取屏幕尺寸
        # screen_width = self.info_window.winfo_screenwidth()
        screen_height = self.info_window.winfo_screenheight()

        # 定位到左下角
        self.info_window.geometry(f"{info_width}x{info_height}+20+{screen_height - info_height - 50}")  # 设置窗口尺寸位置
        self.info_window.overrideredirect(True)  # 去除标题栏及边框 - 无边框窗口
        self.info_window.attributes('-topmost', True)  # 窗口置顶显示 - 显示在其他窗口前面
        self.info_window.attributes('-transparentcolor', 'white')  # 设置窗口白色部分透明 - 空心效果
        # self.info_window.attributes('-alpha', 0.8)  # 设置窗口透明度（0.0 完全透明，1.0 完全不透明）
        self.info_window.configure(bg='white')  # 深灰色背景 - 2C2C2C

        # 信息标签容器
        self.info_frame = tk.Frame(
            self.info_window,
            bg='white',
            padx=10,
            pady=10
        )
        self.info_frame.pack(expand=True, fill='both')

        # 初始化信息标签
        self.info_labels = []
        self.labels = {
            'current_task': tk.Label(
                self.info_frame,
                text=f"[{self.text['current_task']}]: None",  # 当前任务
                fg='#A0DCF2',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
            'current_sub_task': tk.Label(
                self.info_frame,
                text=f"[{self.text['current_sub_task']}]: None",  # 当前子任务
                fg='#A0DCF2',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
            'last_intf': tk.Label(
                self.info_frame,
                text=f"[{self.text['last'] + self.text['intf']}]: None",  # 上一个界面
                fg='#00FF00',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
            'last_independent_intf': tk.Label(
                self.info_frame,
                text=f"[{self.text['last'] + self.text['independent'] + self.text['intf']}]: None",  # 上一个独立界面
                fg='#00FF00',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
            'current_intf': tk.Label(
                self.info_frame,
                text=f"[{self.text['current'] + self.text['intf']}]: None",  # 当前界面
                fg='#00FF00',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
            'action': tk.Label(
                self.info_frame,
                text=f"[{self.text['action']}]: None",  # 点击、按下键盘
                fg='#00FF00',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
            'log_info': tk.Label(
                self.info_frame,
                text="运行信息:",
                fg='#CC6600',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            ),
        }

        for ind in range(len(self.parent.character.log_info)):
            label = tk.Label(
                self.info_frame,
                text=f"    默认消息{ind + 1}",  # 切换地图中、战斗中、、、
                fg='#FFA500',
                bg=label_bg,
                font=('微软雅黑', 9),
                anchor='w'
            )
            label_name = f'log{ind + 1}'
            self.labels[label_name] = label
            self.info_labels.append(label)
        # 布局标签
        for label in self.labels.values():
            label.pack(fill='x', pady=1)

    def _set_click_through_win(self):
        """
        Windows系统设置鼠标穿透
        :return:
        """
        try:
            import ctypes
            hwnd = ctypes.windll.user32.GetParent(self.canvas_window.winfo_id())
            ex_style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
            ex_style |= 0x00000020  # WS_EX_TRANSPARENT
            ex_style |= 0x00080000  # WS_EX_LAYERED
            ctypes.windll.user32.SetWindowLongW(hwnd, -20, ex_style)
        except Exception as e:
            print(f"鼠标穿透设置失败: {e}")

    def update_info(self):

        current_task = self.parent.character.current_task if self.parent.character.current_task else 'empty'
        current_sub_task = self.parent.character.current_sub_task if self.parent.character.current_sub_task else 'empty'
        last_intf = self.parent.character.last_intf if self.parent.character.last_intf else 'empty'
        last_independent_intf = self.parent.character.last_independent_intf if self.parent.character.last_independent_intf else 'empty'
        current_intf = self.parent.character.current_intf if self.parent.character.current_intf else 'empty'
        action = self.parent.character.action if self.parent.character.action else 'empty'

        self.labels['current_task'].config(text=f"[{self.text['current_task']}]: {self.text[current_task]}")
        self.labels['current_sub_task'].config(text=f"[{self.text['current_sub_task']}]: {self.text[current_sub_task]}")
        self.labels['last_intf'].config(text=f"[{self.text['last_intf']}]: {self.text[last_intf] + self.text['intf']}")
        self.labels['last_independent_intf'].config(
            text=f"[{self.text['last_independent_intf']}]: {self.text[last_independent_intf] + self.text['intf']}")
        self.labels['current_intf'].config(text=f"[{self.text['current_intf']}]: {self.text[current_intf] + self.text['intf']}")
        self.labels['action'].config(text=f"[{self.text['action']}]: {self.text[action]}")
        # log info update
        for ind, text in enumerate(self.parent.character.log_info):
            self.info_labels[ind]['text'] = '    ' + text
        self.parent.after(200, self.update_info)  # 每200毫秒更新一次

    def canvas_setting(self, box_loc, border_color='red', border_width=1):
        """
        空心框设置
        :param box_loc:空心框左上角x、y坐标; 空心框宽度width、高度height
        :param border_color: 空心框颜色（默认红色）
        :param border_width: 空心框线框宽度（默认1像素）
        :return:
        """
        x, y, width, height = box_loc
        self.canvas_window.geometry(f"{width}x{height}+{x}+{y}")
        self.canvas.delete('all')  # 清除原有图形
        self.canvas.create_rectangle(
            0, 0,
            width - border_width,
            height - border_width,
            outline=border_color,
            width=border_width
        )
        self.canvas.pack(fill='both', expand=True)


def save_json_file(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=5)


def load_json_file(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"文件未找到:\n\t{path}\n")
    except json.JSONDecodeError:
        print(f"读取JSON文件时发生错误，文件内容可能无效:\n\t{path}\n")


def text_save_to_file(path, text, time_stamp=True):
    if time_stamp:  # 显示时间戳
        current_time = time.strftime("%H:%M:%S", time.localtime())
        text = f"[{current_time}]\t{text}"
    print(text)
    with open(path, 'a') as file:
        file.write(text + '\n')
    return text


def require_admin():
    """
    获取管理员权限
    :return:
    """
    admin = ctypes.windll.shell32.IsUserAnAdmin()
    if not admin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0)
    print("以管理员权限运行成功！")
    # sys.exit()
    return


def is_running(window_title):
    """
    判断程序是否运行
    :param window_title:
    :return:
    """
    hwnd = win32gui.FindWindow(None, window_title)
    return hwnd != 0


def program_launch(exe_path):
    """
    启动路径程序
    :param exe_path:
    :return:
    """
    os.startfile(exe_path)


def get_window_info(window_title):
    hwnd = win32gui.FindWindow(None, window_title)  # 窗口不存在则返回0
    rect = None
    if hwnd != 0:
        rect = win32gui.GetWindowRect(hwnd)
    else:
        time.sleep(2)
        get_window_info(window_title)
    return hwnd, rect


def window_front(hwnd):

    in_front = (hwnd == win32gui.GetForegroundWindow())

    if in_front:
        return in_front
    else:
        # 从最小化恢复到前台
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 恢复窗口
        else:
            ctypes.windll.user32.ShowWindow(hwnd, 6)
            ctypes.windll.user32.ShowWindow(hwnd, 9)

    in_front = (hwnd == win32gui.GetForegroundWindow())
    return in_front


def capture_window(window_rect=None, full_screen=False):
    """
    截取窗口、全屏
    :param window_rect: 窗口尺寸位置信息四元组  left, top, width, height
    :param full_screen: 是否截取全屏
    :return:
    """
    if full_screen:
        screenshot = pyautogui.screenshot()  # 截取全屏
    else:
        screenshot = pyautogui.screenshot(region=window_rect)  # 截取全屏
    img = np.array(screenshot)  # 转为numpy数组
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)  # 转换为BGR格式
    return img


def get_img(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)  # 转换为BGR格式
    return img


def img_match(screenshot, template, gray=True):
    """
    将截图与现有图像对比
    :param screenshot: 截图
    :param template: 模板图片
    :param gray: 是否转化为灰度图
    :return: location, value  # 最佳匹配位置及匹配度
    """
    if gray:
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    height, width = template.shape[:2]  # 匹配区域宽高

    location = (max_loc[0], max_loc[1], width, height)  # 匹配区域左上角在截图的坐标及宽高
    value = max_val
    return location, value  # 最佳匹配位置及匹配度


def text_match(ocr, screenshot, text, threshold=0.8, cls=False):
    """
    将截图与现有图像对比
    :param ocr: OCR模型
    :param screenshot: 截图
    :param text: 模板文字
    :param threshold: 匹配度
    :param cls: 是否启用文本方向分类器（Text Line Classifier）
    :return:
    """
    location = None
    value = 0.0
    result = ocr.ocr(screenshot, cls=cls)
    for line in result[0]:
        matched_text, confidence = line[1]  # 文字、置信度
        # print(matched_text)
        if text in matched_text and confidence >= threshold:
            (x1, y1) = line[0][0]  # 左上角坐标
            (x2, y2) = line[0][2]  # 右下角坐标
            location = (x1, y1, x2 - x1, y2 - y1)  # x, y, width, height
            value = confidence
    return location, value  # 第一个匹配位置及匹配度


def get_center_loc(location, offset=(0, 0)):
    x, y, width, height = location
    x_center = x + width / 2 + offset[0]
    y_center = y + height / 2 + offset[1]
    return x_center, y_center


def click_area_center(loc, offset=(0, 0), click='left'):
    x, y = get_center_loc(loc, offset=offset)
    time.sleep(0.1)
    if click == 'left':  # 左键点击
        pyautogui.moveTo(x, y)
        pyautogui.click()
    elif click == 'right':  # 右键点击
        pyautogui.moveTo(x, y)
        pyautogui.rightClick()


def mouse_scroll(scroll, x=None, y=None):
    time.sleep(0.1)
    if x:
        pyautogui.scroll(scroll, x=x, y=y)
    else:
        pyautogui.scroll(scroll)


def key_input(key):
    if key == 'esc' or 'ESC':
        pyautogui.press('Esc')
    elif isinstance(key, str) and len(key) == 1:
        pyautogui.press(key)


def end_sign():
    pass


if __name__ == '__main__':
    # require_admin()
    # orc = PaddleOCR(use_angle_cls=False, lang='ch')
    # screenshot = capture_window(full_screen=True)
    # location, value = text_match(orc, screenshot, text='点击进入')
    pass
