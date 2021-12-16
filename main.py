import time

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QStandardItemModel
import pyautogui

UI_path = "ui.ui"

INIT_ROW_NUM = 20
INIT_COL_NUM = 2

DOSE = "dose.png"
EFFECT = "effect.png"


def locate(image_path):
    location = pyautogui.locateOnScreen(image_path)
    if location is not None:
        center = pyautogui.center(location)
        return center
    else:
        return None, None


def click_input(x, y, content):
    if isinstance(content, int) or isinstance(content, float):
        content = str(content)
    pyautogui.click(x, y)
    pyautogui.typewrite(content)


def locate_input(image_path, content):
    """
    找到屏幕中的输入截图，令鼠标点击截图中点，令键盘输入内容content
    :param image_path:str, 输入截图的路径
    :param content: str, 键盘输入的内容
    :return:
    """
    if isinstance(content, int) or isinstance(content, float):
        content = str(content)

    location = pyautogui.locateOnScreen(image_path)
    if location is not None:
        center = pyautogui.center(location)
        print(center)
        pyautogui.click(center.x, center.y)
        pyautogui.typewrite(content)


class MainWindow:

    def __init__(self):
        # 加载UI
        self.ui = uic.loadUi(UI_path)
        model = QStandardItemModel(INIT_ROW_NUM, INIT_COL_NUM)
        self.ui.tableView.setModel(model)
        # 连接信号
        self.ui.run.clicked.connect(self._run)

    def _run(self):
        # 数据获取
        data = self._get_data()  # list,[[d0,e0],[d1,e1],...]
        # 查找位置
        dose_x, dose_y = locate(DOSE)
        effect_x, effect_y = locate(EFFECT)
        # 界面操作
        for d in data:
            click_input(dose_x, dose_y, d[0])
            click_input(effect_x, effect_y, d[1])
            pyautogui.press("enter")
            time.sleep(0.1)

    def _get_data(self):
        """获取表格内容"""
        datas = []
        model = self.ui.tableView.model()
        flag = False
        for row in range(model.rowCount()):
            datas.append([])
            for col in range(model.columnCount()):
                index = model.index(row, col)
                data = model.data(index)
                if data is not None:
                    datas[row].append(data)
                else:  # 第一个空行就退出
                    flag = True
                    break
            if flag:
                datas.pop()
                break
        return datas


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.ui.show()
    app.exec_()
