import win32gui
import win32con
import time

import my_utils

hwnd = win32gui.FindWindow(None, 'Aseprite v1.3.7-dev')

time.sleep(2)
print('start')

if hwnd != 0:
    my_utils.window_front(hwnd)
    print('right01')
    time.sleep(2)
    win32gui.SetWindowPos(
        hwnd, win32con.HWND_TOP,
        10, 10, 0, 0,
        win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE
    )
    print('right02')
else:
    print('none hwnd')
