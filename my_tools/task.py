"""
任务执行
"""


import time


class TaskManage:
    def __init__(self, log):
        self.log = log
        self.st = 2  # stop time
        self.current_task = None  # 当前任务
        self.current_sub_task = None  # 当前子任务

    def start_task(self, task_list):
        self.log.info("开始任务")
        pass

    def game_launch(self):
        """
        启动游戏
        :return:
        """
        if not self.is_running():
            self.program_launch()
            self._intf_info_turn('launch')
        self.get_window_info()

        count = 0
        while count <= self.count:
            if self.current_intf == 'launch':
                intf_match, ele_match, do_act = self.do_action('launch', 'launch')
                if do_act:
                    self._intf_info_turn('main_intf')
                    break
                else:
                    count += 1
                    time.sleep(self.st)
            else:
                continue

    def dig(self):
        pass

    def daily(self):
        pass


def end_sign():
    pass


if __name__ == '__main__':
    pass
