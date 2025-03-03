"""
界面管理
"""
import my_utils

from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class EleBase:
    """界面元素基类"""
    name: str = None  # 元素名
    type: str = None  # 元素类型button、key、text  界面按钮、键盘指令、界面文字

    # img和text可同时共存 - 匹配时先匹配img再匹配文字
    img: List[str] = None  # 界面按钮图片名列表 - 可能需要点击多次才能进入下一个界面
    is_gray: Optional[bool] = False  # 是否采用灰度图片匹配截图 - 默认不采用
    offset: Optional[tuple] = None  # 点击位置偏移 - 默认中心
    key: Optional[str] = None  # 按键名
    text: Optional[str] = None  # 界面按钮文本

    # 记忆截图及点击位置，列表是因为可能点击多个位置，需要匹配多个位置
    wnd_area_rect: Optional[List[tuple]] = None  # 软件为窗口时的记忆截图坐标位置  [(x, y, width,height), ]
    full_area_rect: Optional[List[tuple]] = None  # 软件为全屏时的记忆截图位置  [(x, y, width,height), ]
    wnd_clk_loc: Optional[List[tuple]] = None  # 软件为窗口时的记忆点击坐标位置  [(x, y), ]
    full_clk_loc: Optional[List[tuple]] = None  # 软件为全屏时的记忆点击坐标位置   [(x, y), ]


@dataclass
class IntfBase:
    """界面基类"""
    name: str = None
    indep: bool = True  # 是否独立界面 - 判断esc返回的上一个界面是什么等
    is_active: Optional[bool] = True  # 是否可用 - 活动界面等 - 过期即不可用 - 默认可用
    img: List[str] = None  # 界面验证图片 - 一张
    is_gray: Optional[bool] = False  # 是否采用灰度图片匹配截图 - 默认不采用
    text: Optional[str] = None  # 界面验证文本 - 一段字符串

    # 界面动作/元素 - 元素与界面分开，只用元素字典关联   element_name: target_intf
    actions: Dict[str, str] = None  # 界面动作字典   {元素名name: 下一个界面name, }   li_intf、l_intf - 上一个独立界面、上一个界面

    # 记忆验证位置 - 一个，对应图片和文本的一个
    wnd_area_rect: Optional[tuple] = None  # 软件为窗口时的记忆截图坐标位置  [(x, y, width,height), ]
    full_area_rect: Optional[tuple] = None  # 软件为全屏时的记忆截图位置  [(x, y, width,height), ]


class IntfManage:
    def __init__(self):
        self.intf_list_path = r"config\intf\intf_list.json"
        self.ele_list_path = r"config\intf\ele_list.json"
        self.intf_list = my_utils.load_json_file(self.intf_list_path)  # 导入-保存配置
        self.ele_list = my_utils.load_json_file(self.ele_list_path)  # 导入-保存配置

        self.intf = {}  # interface dict   key: intf name  value:intf class instance
        self.ele = {}  # element dict   key: ele name  value:ele class instance
        self.c_intf = None  # current interface
        self.l_intf = None  # last interface
        self.li_intf = None  # last independent interface

        self._load_intf()
        pass

    def _load_intf(self):
        for ele in self.ele_list:
            self.ele[ele['name']] = EleBase(
                name=ele['name'],
                type=ele['name'],
                img=ele['name'],  # 必定给出图片
                is_gray=ele['is_gray'] if 'is_gray' in ele else False,
                offset=ele['offset'] if 'offset' in ele else (0, 0),
                key=ele['key'] if 'key' in ele else None,
                text=ele['text'] if 'text' in ele else None,

                wnd_area_rect=ele['wnd_area_rect'] if 'wnd_area_rect' in ele else None,
                full_area_rect=ele['full_area_rect'] if 'full_area_rect' in ele else None,
                wnd_clk_loc=ele['wnd_clk_loc'] if 'wnd_clk_loc' in ele else None,
                full_clk_loc=ele['full_clk_loc'] if 'full_clk_loc' in ele else None,

            )

        for intf in self.intf_list:
            self.intf[intf['name']] = IntfBase(
                name=intf['name'],
                indep=intf['indep'],
                is_active=intf['is_active'] if 'is_active' in intf else True,
                img=intf['img'],
                is_gray=intf['is_gray'] if 'is_gray' in intf else False,
                text=intf['text'] if 'text' in intf else None,
                actions=intf['actions'],

                wnd_area_rect=intf['wnd_area_rect'] if 'wnd_area_rect' in intf else None,
                full_area_rect=intf['full_area_rect'] if 'full_area_rect' in intf else None,

            )
            pass
        pass

    def intf_info_turn(self, target_intf):
        """界面信息转到目标界面"""
        pass

    def find_path(self, intf_a, intf_b):
        """寻找A界面到B界面的最短路径"""
        pass

    def intf_switch(self, target_intf):
        """界面转到目标界面动作"""
        pass


if __name__ == '__main__':
    pass
