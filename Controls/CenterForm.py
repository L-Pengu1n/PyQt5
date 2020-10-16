# QDesktopWidget
import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()

        # 设置主窗口标题
        self.setWindowTitle('让窗口居中')

        # 设置窗口的尺寸
        self.resize(400,300)

    def Center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()

        # 获取窗口坐标系
        size = self.geometry()

        # 获取居中的坐标
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2

        # 移动窗口到居中坐标
        self.move(newLeft+400, newTop)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterForm()
    main.show()
    main2 = CenterForm()
    main2.setWindowTitle('函数窗口')
    main2.Center()

    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec())