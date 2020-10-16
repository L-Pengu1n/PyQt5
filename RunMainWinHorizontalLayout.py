import sys
import MainWinHorizontalLayout

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    # 创建对象表示应用程序
    app = QApplication(sys.argv)

    # 创建一个窗口
    mainWindow = QMainWindow()

    # 创建一个对象
    ui = MainWinHorizontalLayout.Ui_MainWindow()

    #运用类中的函数往主窗口添加控件，需要接受主窗口参数
    ui.setupUi(mainWindow)

    # 显示窗口
    mainWindow.show()

    # 进入主循环
    sys.exit(app.exec())