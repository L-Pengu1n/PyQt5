import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QWidget,QPushButton

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(600,400)
        self.setWindowTitle('退出应用程序')

        # 添加Button

        self.button1 = QPushButton('退出应用程序')

        # 将按钮单机事件与onClick_Button函数相链接
        self.button1.clicked.connect(self.onClick_Button)

        # 创建布局，并在布局上放置button控件
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        # 创建窗口
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)


        # 按钮单机事件的方法（自定义的槽）
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()

        # 退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()


    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec())