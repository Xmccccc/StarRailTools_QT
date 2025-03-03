"""
各种配置的导入
"""

import my_utils

cfg_software = {  # 软件窗口设置
    "title": 'StarRailTools_QT V0.1',
    "language": 'zh',
    "x": 100,  # 窗口距屏幕左上角距离
    "y": 100,
    "width": 800,  # 窗口宽高
    "height": 600,
    "resizable_w": None,  # 窗口宽高是否固定
    "resizable_h": None,
    "font": "微软雅黑",  # 字体
    "font_size": 14,  # 字体大小
}

cfg_run = {  # 游戏信息
    "exe_path": r'C:\Program Files\miHoYo Launcher\games\Star Rail Game\StarRail.exe',
    "exe_name": 'StarRail.exe',
    "window_title": '崩坏：星穹铁道',
    # 运行设置
    # "log_info_num": 6,  # 信息显示数量
    "threshold": 0.8,
    # 加载信息
    "computer": "computer01",
    # 信息记录
    "window_rect": None,  # (x, y, width, height)
    "window_mode": 'window',  # 游戏窗口是否全屏  window  full

    "finish_time_entrust": None,  # 最后派遣时间



}

zh = {  # 左菜单
    "function": '功能',
    "theme": '主题',
    "setting": '设置',
    "about": '关于',
    # 功能
    "daily": '日常',
    "dig": '锄地',
    "story": '剧情',
    "simulated_universe": '模拟宇宙',
    "forgotten_hall": '忘却之庭',
    "run_selected": '选择执行',
    "run_all": '全部执行',
    # intf界面
    "main_map": '主地图',
    "continue": '点击空白处关闭、继续',
    "prompt01": '提示',
    "phone": '手机',
    "entrust01": '委托-专属材料',
    "entrust02": '委托-委托报告',
    "friends01": '好友-我的好友',
    "friends0101": '好友-我的好友-好友申请',
    "email": '邮箱',
    "roam_visa01": '漫游签证-角色展示',
    "achievement01": '成就主页',
    "achievement02": '成就详情',
    "guide01": '星际和平指南-每日实训',
    # element
    "confirm": '确认',
    "cancel": '取消',
    "esc_main_map": 'esc键',
    "esc_phone": 'esc键',
    "esc_li": 'esc键',  # last interface
    "esc_lii": 'esc键',  # last independent interface
    "key_c": 'c键',
    "key_b": 'b键',
    "key_v": 'v键',
    "collect01": '领取',
    "collect02": '领取',
    "one_click_collect01": '一键领取',
    "one_click_collect02": '一键领取',
    "all_collect01": '全部领取',
    "all_collect02": '全部领取',
    "agree01": '同意-添加好友',
    "red_dot_tips01": '小红点',
    "entrust": '委托',
    "dispatched_again": '再次派遣',
    "friends": '好友',
    "friend_request": '好友申请',
    "delete_read": '邮件-删除已读',
    "roam_visa": '漫游签证',
    "achievement": '成就',
    "guide": '指南',
    "daily_reward": '每日奖励',

    # log信息

}

en = {}

intf_list = [{'name': 'launch',  # 启动
              'independent': False,
              'img': 'launch_game',
              'text': '点击进入',
              'actions': {"launch": 'main_intf',
                          },
              },

             {
                 'name': 'main_map',  # 主地图
                 'independent': True,
                 'img': 'i_main_map',
                 # 'text': 'xxx',
                 'actions': {"esc": 'phone',
                             },
             },

             {
                 'name': 'continue',  # 点击空白处关闭/继续
                 'independent': False,
                 'img': 'i_continue',
                 'text': '空白',
                 'actions': {"continue": 'l_intf',
                             },
             },

             {
                 'name': 'prompt',  # 提示
                 'independent': False,
                 'img': 'i_prompt',
                 'text': '提示',
                 'actions': {"confirm": 'l_intf',
                             "cancel": 'l_intf',
                             },
             },

             {
                 'name': 'phone',  # 手机
                 'independent': True,
                 'img': 'i_phone',
                 # 'text': 'xxx',
                 'actions': {"esc": 'main_map',
                             "entrust": 'entrust01',
                             },
             },

             {
                 'name': 'phone',  # 手机
                 'img': ['i_phone01', 'i_phone02', ],
                 'independent': True,
                 'target_intf': [],
                 'element_name': ['esc01', 'entrust', 'friends', 'email',
                                  'roam_visa', 'achievement', 'guide',
                                  ],
             },

             {
                 'name': 'entrust01',  # 委托-专属材料
                 'img': ['i_entrust', 'i_entrust01', ],
                 'independent': False,
                 'target_intf': ['phone', 'entrust02', ],
                 'element_name': ['esc04', 'one_click_collect02', ]
             },

             {
                 'name': 'entrust02',  # 委托-委托报告
                 'img': ['i_entrust02', ],
                 'independent': False,
                 'target_intf': ['entrust01', ],
                 'element_name': ['dispatched_again', ]
             },

             {
                 'name': 'friends01',  # 好友-我的好友
                 'img': ['i_friends01', ],
                 'independent': False,
                 'target_intf': ['phone', 'friends0101', ],
                 'element_name': ['esc04', 'friend_request', ]
             },

             {
                 'name': 'friends0101',  # 好友-我的好友-好友申请
                 'img': ['i_friends0101', ],
                 'independent': False,
                 'target_intf': ['friends01', ],
                 'element_name': ['esc02', 'agree01', ]
             },

             {
                 'name': 'email',  # 邮箱
                 'img': ['i_email', ],
                 'independent': True,
                 'target_intf': ['phone', 'continue', 'prompt01', ],
                 'element_name': ['esc04', 'all_collect02', 'delete_read']
             },

             {
                 'name': 'roam_visa01',  # 漫游签证-角色展示
                 'img': ['i_roam_visa01', ],
                 'independent': False,
                 'target_intf': ['phone', ],
                 'element_name': ['esc04', ]
             },

             {
                 'name': 'achievement01',  # 成就主页
                 'img': ['i_achievement01', ],
                 'independent': True,
                 'target_intf': ['phone', 'achievement02'],
                 'element_name': ['esc04', 'red_dot_tips01']
             },

             {
                 'name': 'achievement02',  # 成就详情
                 'img': ['i_achievement02', ],
                 'independent': True,
                 'target_intf': ['achievement01', 'continue', ],
                 'element_name': ['esc03', 'collect02', ]
             },

             {
                 'name': 'guide01',  # 星际和平指南-每日实训
                 'img': ['i_guide01', ],
                 'independent': False,
                 'target_intf': ['last_independent_intf', 'continue'],
                 'element_name': ['esc03', 'collect01', 'daily_reward', ]
             },

             # {
             #  'name': 'herta_sr01',  # 导航-空间站黑塔-星穹列车派对车厢
             #  'img': ['i_herta', 'i_sr', 'i_sr01', ],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta_sr02',  # 导航-空间站黑塔-星穹列车观景车厢
             #  'img': ['i_herta', 'i_sr', 'i_sr02', ],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta_sr03',  # 导航-空间站黑塔-星穹列车客房车厢
             #  'img': ['i_herta', 'i_sr', 'i_sr02', ],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta01',  # 导航-空间站黑塔-主控舱段
             #  'img': ['i_herta', 'i_herta01', ],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta02',  # 导航-空间站黑塔-基座舱段
             #  'img': ['i_herta', 'i_herta02', ],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta0302',  # 导航-空间站黑塔-收容舱段2层
             #  'img': ['i_herta', 'i_herta03', 'i_floor02'],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta0301',  # 导航-空间站黑塔-收容舱段1层
             #  'img': ['i_herta', 'i_herta03', 'i_floor01'],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta03-1',  # 导航-空间站黑塔-收容舱段-1层
             #  'img': ['i_herta', 'i_herta03', 'i_floor-1'],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta0402',  # 导航-空间站黑塔-支援舱段2层
             #  'img': ['i_herta', 'i_herta04', 'i_floor02'],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta0401',  # 导航-空间站黑塔-支援舱段1层
             #  'img': ['i_herta', 'i_herta04', 'i_floor01'],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta0503',  # 导航-空间站黑塔-禁闭舱段3层界面
             #  'img': ['i_herta', 'i_herta05', 'i_floor03'],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta0502',  # 导航-空间站黑塔-禁闭舱段2层界面
             #  'img': ['i_herta', 'i_herta05', 'i_floor02'],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },
             #
             # {
             #  'name': 'herta0501',  # 导航-空间站黑塔-禁闭舱段1层界面
             #  'img': ['i_herta', 'i_herta05', 'i_floor01'],
             #  'independent': False,
             #  'target_intf': [],
             #  'element_name': []
             #  },

             ]

# "paths": {"ico": r'cfg\img\appicon.ico',
#                     "zh": r'cfg\language\zh.json',
#                     "en": r'cfg\language\en.json',
#                     "intf": r'cfg\intf\intf.json',
#                     "element": r'cfg\intf\element.json',
#                     "img": r'cfg\img',
#                     "intf_img": r'cfg\img\zh\intf',
#
#                     "task": r'user_cfg\task\task.json',
#                     "dig_maps": r'cfg\task\dig_maps.json',
#                     "daily_task": r'cfg\task\daily_task.json',
#
#                     },

ele_list = []

task = []

dig_maps = {}

daily_task = {}


def end_sign():
    pass


if __name__ == '__main__':
    paths = [(cfg_software, r"config\cfg\cfg_software.json"),
             (cfg_run, r"config\cfg\cfg_run.json"),
             (zh, r"config\language\zh.json"),
             (en, r"config\language\en.json"),
             (intf_list, r"config\intf\intf_list.json"),
             (ele_list, r"config\intf\ele_list.json"),
             (task, r"config\task\task.json"),
             (dig_maps, r"config\task\dig_maps.json"),
             (daily_task, r"config\task\daily_task.json"),

             ]

    for file, path in paths:
        my_utils.save_json_file(path, file)
