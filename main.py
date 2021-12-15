from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QStandardItemModel

UI_path = "ui.ui"

INIT_ROW_NUM = 20
INIT_COL_NUM = 2


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
        # 界面操作
        pass


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.ui.show()
    app.exec_()
