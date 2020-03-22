'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2020/3/21
@Program      : 一个简单的词典用于查询网络工程的专业名词的中英文对比
'''

import sys
import main
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())