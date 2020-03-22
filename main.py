# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

import load_data


class Ui_MainWindow(object):
    def __init__(self):
        self.word_list = load_data.load_list()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(791, 551))
        self.tabWidget.setMaximumSize(QtCore.QSize(791, 551))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabLocal = QtWidgets.QWidget()
        self.tabLocal.setObjectName("tabLocal")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tabLocal)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 83, 621, 431))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setAcceptRichText(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tabLocal)
        self.pushButton.setGeometry(QtCore.QRect(701, 31, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.tabLocal)
        self.label.setGeometry(QtCore.QRect(150, 10, 144, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tabLocal)
        self.label_2.setGeometry(QtCore.QRect(150, 60, 64, 16))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.tabLocal)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(9, 9, 131, 511))
        self.listWidget.setObjectName("listWidget")
        # 根据初始化的单词列表长度来决定要添加多少个item
        for i in range(len(self.word_list)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
        self.comboBox = QtWidgets.QComboBox(self.tabLocal)
        self.comboBox.setGeometry(QtCore.QRect(150, 30, 541, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        # 根据初始化的单词列表长度来决定要添加多少个comboBox的item
        for i in range(len(self.word_list)):
            self.comboBox.addItem("")
        self.tabWidget.addTab(self.tabLocal, "")
        self.tabAbout = QtWidgets.QWidget()
        self.tabAbout.setObjectName("tabAbout")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabAbout)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelAbout = QtWidgets.QLabel(self.tabAbout)
        self.labelAbout.setObjectName("labelAbout")
        self.gridLayout_2.addWidget(self.labelAbout, 0, 0, 1, 1)
        self.textAbout = QtWidgets.QTextBrowser(self.tabAbout)
        self.textAbout.setObjectName("textAbout")
        self.gridLayout_2.addWidget(self.textAbout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabAbout, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBarClicked['int'].connect(self.textAbout.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.listWidget.itemClicked.connect(self.list_check)
        self.comboBox.currentIndexChanged.connect(self.comba_check)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QIcon("source/dict.ico"))
        MainWindow.setWindowTitle(_translate("MainWindow", "网工专业名词字典"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "点击查询"))
        self.label.setText(_translate("MainWindow", "输入需要查询的单词"))
        self.label_2.setText(_translate("MainWindow", "查询结果"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        for i in range(len(self.word_list)):
            item = self.listWidget.item(i)
            item.setText(_translate("MainWindow", self.word_list[i]))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        for i in range(len(self.word_list)):
            self.comboBox.setItemText(i, _translate("MainWindow", self.word_list[i]))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLocal), _translate("MainWindow", "本地数据库查询"))
        self.labelAbout.setText(_translate("MainWindow", "关于本程序"))
        self.textAbout.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'宋体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">版本：1.0.0</p>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">作者：sean cheng</p>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">更新时间：2020年3月22日</p>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">中英文对照及释义的资料来源：<br />《网络工程师考试同步辅导（上午科目）（第4版）》第14章 计算机专业英语<br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAbout), _translate("MainWindow", "关于本程序"))

    def list_check(self):
        # 点击列表按钮的时间，先获得当前点击的列表的文本，再去查询该文本的对应词目内容。
        keyWord = self.listWidget.currentItem().text()
        self.show_detail(keyWord)

    def comba_check(self):
        # 点击列表按钮的时间，先获得当前点击的列表的文本，再去查询该文本的对应词目内容。
        keyWord = self.comboBox.currentText()
        self.show_detail(keyWord)

    def show_detail(self, keyWord):
        item = load_data.load_word_detail(keyWord)

        enName = str(item[0][0])
        # 英文简称存在空的情况
        if str(item[0][1]) == 'None':
            aliseName = '无'
        else:
            aliseName = str(item[0][1])
        # 中文名称存在空的情况
        if str(item[0][2]) == 'None':
            cnName = '无'
        else:
            cnName = str(item[0][2])
        cndetail = str(item[0][3])

        self.textEdit_2.setHtml("<div class=\"container-fluid\"><div class=\"row\"><div class=\"col-md-12\"><dl>\n"
                                "<dt>英文词语</dt><dd>" + enName + "</dd>\n<dt>英文简称缩写</dt><dd>" + aliseName + "</dd>\n"
                                "<dt>中文意思</dt><dd>" + cnName + "</dd>\n<dt>词语的含义</dt><dd>" + cndetail + "</dd>\n"
                                "</dl></div></div></div>")
