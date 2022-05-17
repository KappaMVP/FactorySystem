# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model1_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: #2D3142;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 50, 931, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #F5CB5C;")
        self.label.setObjectName("label")
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(1420, 80, 141, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setStyleSheet("background-color: rgb(229, 229, 229);\n"
                                     "")
        self.close_btn.setObjectName("close_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1420, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAcceptDrops(False)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: #E5E5E5;")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1580, 40, 161, 91))
        self.lcdNumber.setStyleSheet("color: #e5e5e5;\n"
                                     "border-style: solid;\n"
                                     "border-width: 1px;\n"
                                     "border-color: #e5e5e5;")
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(150, 110, 1621, 900))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tabWidget.setStyleSheet("border: none")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.tabBar().setStyleSheet(
            "QTabBar::tab{height: 50px; width: 200px;color: #768895;border-top-left-radius: 5px;border-top-right-radius: 5px}"
            "QTabBar::tab:selected{color: #E5E5E5;background-color: #546A7B;}")
        self.face_reg_tab = QtWidgets.QWidget()
        self.face_reg_tab.setStyleSheet(
            "border: none;background-color: #546A7B")
        self.face_reg_tab.setObjectName("face_reg_tab")
        self.face_reg_scr = QtWidgets.QLabel(self.face_reg_tab)
        self.face_reg_scr.setGeometry(QtCore.QRect(480, 30, 1024, 768))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.face_reg_scr.setFont(font)
        self.face_reg_scr.setStyleSheet("border-style: solid;\n"
                                        "border-width: 1px;\n"
                                        "border-color: #768895;\n"
                                        "")
        self.face_reg_scr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.face_reg_scr.setAlignment(QtCore.Qt.AlignCenter)
        self.face_reg_scr.setObjectName("face_reg_scr")
        self.gen_features_btn = QtWidgets.QPushButton(self.face_reg_tab)
        self.gen_features_btn.setGeometry(QtCore.QRect(110, 710, 301, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.gen_features_btn.setFont(font)
        self.gen_features_btn.setStyleSheet("background-color: rgb(229, 229, 229);\n"
                                            "")
        self.gen_features_btn.setObjectName("gen_features_btn")
        self.face_reg_area = QtWidgets.QScrollArea(self.face_reg_tab)
        self.face_reg_area.setGeometry(QtCore.QRect(120, 39, 281, 651))
        self.face_reg_area.setMinimumSize(QtCore.QSize(0, 0))
        self.face_reg_area.setStyleSheet("background-color: #768895;")
        self.face_reg_area.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.face_reg_area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.face_reg_area.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.face_reg_area.setWidgetResizable(True)
        self.face_reg_area.setObjectName("face_reg_area")
        self.face_reg_area.verticalScrollBar().setStyleSheet("QScrollBar:vertical"
                                                             "{width:12px;}"
                                                             "QScrollBar::handle:vertical"
                                                             "{width:12px;background:rgba(0,0,0,25%);min-height:20;}"
                                                             "QScrollBar::handle:vertical:hover"
                                                             "{width:12px;background:rgba(0,0,0,50%);min-height:20;}"
                                                             "QScrollBar::sub-line:vertical"
                                                             "{border: none;}"
                                                             "QScrollBar::add-line:vertical"
                                                             "{border: none;}"
                                                             "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical"
                                                             "{background:rgba(0,0,0,10%);}"
                                                             )
        self.face_reg_contents = QtWidgets.QWidget()
        self.face_reg_contents.setGeometry(QtCore.QRect(0, 0, 281, 651))
        self.face_reg_contents.setMinimumSize(QtCore.QSize(0, 0))
        self.face_reg_contents.setObjectName("face_reg_contents")
        self.face_reg_layout = QtWidgets.QVBoxLayout(self.face_reg_contents)
        self.face_reg_layout.setObjectName("face_reg_layout")
        self.face_reg_area.setWidget(self.face_reg_contents)
        self.tabWidget.addTab(self.face_reg_tab, "")
        self.face_tab = QtWidgets.QWidget()
        self.face_tab.setStyleSheet("border: none;background-color: #546A7B")
        self.face_tab.setObjectName("face_tab")
        self.face_scr = QtWidgets.QLabel(self.face_tab)
        self.face_scr.setGeometry(QtCore.QRect(480, 30, 1024, 768))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.face_scr.setFont(font)
        self.face_scr.setStyleSheet("border-style: solid;\n"
                                    "border-width: 1px;\n"
                                    "border-color: #768895;\n"
                                    "")
        self.face_scr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.face_scr.setAlignment(QtCore.Qt.AlignCenter)
        self.face_scr.setObjectName("face_scr")
        self.face_rec_label = QtWidgets.QLabel(self.face_tab)
        self.face_rec_label.setGeometry(QtCore.QRect(108, 50, 300, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.face_rec_label.setFont(font)
        self.face_rec_label.setStyleSheet(
            "color: #E5E5E5;margin-bottom:5px;border-bottom: 1px solid;border-bottom-color: #E5E5E5;")
        self.face_rec_label.setAlignment(QtCore.Qt.AlignCenter)
        self.face_rec_label.setObjectName("face_rec_label")
        self.face_area = QtWidgets.QScrollArea(self.face_tab)
        self.face_area.setGeometry(QtCore.QRect(130, 110, 261, 650))
        self.face_area.setMinimumSize(QtCore.QSize(0, 0))
        self.face_area.setStyleSheet("background-color: #768895;")
        self.face_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.face_area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.face_area.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.face_area.setWidgetResizable(True)
        self.face_area.setObjectName("face_area")
        self.face_area.verticalScrollBar().setStyleSheet("QScrollBar:vertical"
                                                         "{width:12px;}"
                                                         "QScrollBar::handle:vertical"
                                                         "{width:12px;background:rgba(0,0,0,25%);min-height:20;}"
                                                         "QScrollBar::handle:vertical:hover"
                                                         "{width:12px;background:rgba(0,0,0,50%);min-height:20;}"
                                                         "QScrollBar::sub-line:vertical"
                                                         "{border: none;}"
                                                         "QScrollBar::add-line:vertical"
                                                         "{border: none;}"
                                                         "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical"
                                                         "{background:rgba(0,0,0,10%);}"
                                                         )
        self.face_area_contents = QtWidgets.QWidget()
        self.face_area_contents.setGeometry(QtCore.QRect(0, 0, 261, 681))
        self.face_area_contents.setMinimumSize(QtCore.QSize(0, 0))
        self.face_area_contents.setObjectName("face_area_contents")
        self.face_layout = QtWidgets.QVBoxLayout(self.face_area_contents)
        self.face_layout.setObjectName("face_layout")
        self.face_area.setWidget(self.face_area_contents)
        self.tabWidget.addTab(self.face_tab, "")
        self.factory_tab = QtWidgets.QWidget()
        self.factory_tab.setStyleSheet(
            "border: none;background-color: #546A7B")
        self.factory_tab.setObjectName("factory_tab")
        self.factory_scr = QtWidgets.QLabel(self.factory_tab)
        self.factory_scr.setGeometry(QtCore.QRect(480, 30, 1024, 768))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.factory_scr.setFont(font)
        self.factory_scr.setStyleSheet("border-style: solid;\n"
                                       "border-width: 1px;\n"
                                       "border-color: #768895;\n"
                                       "")
        self.factory_scr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.factory_scr.setAlignment(QtCore.Qt.AlignCenter)
        self.factory_scr.setObjectName("factory_scr")
        self.factory_rec_label = QtWidgets.QLabel(self.factory_tab)
        self.factory_rec_label.setGeometry(QtCore.QRect(108, 50, 300, 50))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.factory_rec_label.setFont(font)
        self.factory_rec_label.setStyleSheet(
            "color: #E5E5E5;margin-bottom:5px;border-bottom: 1px solid;border-bottom-color: #E5E5E5;")
        self.factory_rec_label.setAlignment(QtCore.Qt.AlignCenter)
        self.factory_rec_label.setObjectName("factory_rec_label")
        self.factory_area = QtWidgets.QScrollArea(self.factory_tab)
        self.factory_area.setGeometry(QtCore.QRect(130, 110, 261, 650))
        self.factory_area.setMinimumSize(QtCore.QSize(0, 0))
        self.factory_area.setStyleSheet("background-color: #768895;")
        self.factory_area.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.factory_area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.factory_area.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.factory_area.setWidgetResizable(True)
        self.factory_area.setObjectName("factory_area")
        self.factory_area.verticalScrollBar().setStyleSheet("QScrollBar:vertical"
                                                            "{width:12px;}"
                                                            "QScrollBar::handle:vertical"
                                                            "{width:12px;background:rgba(0,0,0,25%);min-height:20;}"
                                                            "QScrollBar::handle:vertical:hover"
                                                            "{width:12px;background:rgba(0,0,0,50%);min-height:20;}"
                                                            "QScrollBar::sub-line:vertical"
                                                            "{border: none;}"
                                                            "QScrollBar::add-line:vertical"
                                                            "{border: none;}"
                                                            "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical"
                                                            "{background:rgba(0,0,0,10%);}"
                                                            )
        self.fatory_contents = QtWidgets.QWidget()
        self.fatory_contents.setGeometry(QtCore.QRect(0, 0, 261, 681))
        self.fatory_contents.setMinimumSize(QtCore.QSize(0, 0))
        self.fatory_contents.setObjectName("fatory_contents")
        self.factory_layout = QtWidgets.QVBoxLayout(self.fatory_contents)
        self.factory_layout.setObjectName("factory_layout")
        self.factory_area.setWidget(self.fatory_contents)
        self.tabWidget.addTab(self.factory_tab, "")
        self.score_tab = QtWidgets.QWidget()
        self.score_tab.setStyleSheet("border: none;background-color: #546A7B")
        self.score_tab.setObjectName("score_tab")
        self.score_table = QtWidgets.QTableWidget(self.score_tab)
        self.score_table.setGeometry(QtCore.QRect(310, 40, 1021, 671))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.score_table.setFont(font)
        self.score_table.setStyleSheet("background: #768895;")
        self.score_table.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.score_table.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.score_table.setAutoScroll(True)
        self.score_table.setAutoScrollMargin(16)
        self.score_table.setTabKeyNavigation(True)
        self.score_table.setProperty("showDropIndicator", True)
        self.score_table.setGridStyle(QtCore.Qt.SolidLine)
        self.score_table.setWordWrap(True)
        self.score_table.setCornerButtonEnabled(True)
        self.score_table.setRowCount(30)
        self.score_table.setObjectName("score_table")
        self.score_table.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.score_table.setHorizontalHeaderItem(4, item)
        self.score_table.horizontalHeader().setVisible(True)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        font.setBold(True)
        self.score_table.horizontalHeader().setFont(font)
        self.score_table.horizontalHeader().setFixedHeight(40)
        self.score_table.horizontalHeader().setDefaultSectionSize(200)
        self.score_table.horizontalHeader().setHighlightSections(True)
        self.score_table.horizontalHeader().setMinimumSectionSize(20)
        self.score_table.horizontalHeader().setSortIndicatorShown(False)
        self.score_table.horizontalHeader().setStretchLastSection(False)
        self.score_table.verticalHeader().setVisible(False)
        self.score_table.verticalHeader().setDefaultSectionSize(40)
        self.score_table.verticalHeader().setMinimumSectionSize(25)
        self.score_delete_btn = QtWidgets.QPushButton(self.score_tab)
        self.score_delete_btn.setGeometry(QtCore.QRect(1170, 740, 141, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.score_delete_btn.setFont(font)
        self.score_delete_btn.setStyleSheet("background-color: rgb(229, 229, 229);\n"
                                            "")
        self.score_delete_btn.setObjectName("score_delete_btn")
        self.tabWidget.addTab(self.score_tab, "")
        self.io_tab = QtWidgets.QWidget()
        self.io_tab.setStyleSheet("border: none;background-color: #546A7B")
        self.io_tab.setObjectName("io_tab")
        self.io_table = QtWidgets.QTableWidget(self.io_tab)
        self.io_table.setGeometry(QtCore.QRect(310, 40, 1021, 671))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.io_table.setFont(font)
        self.io_table.setStyleSheet("background: #768895;")
        self.io_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.io_table.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.io_table.setAutoScroll(True)
        self.io_table.setAutoScrollMargin(16)
        self.io_table.setTabKeyNavigation(True)
        self.io_table.setProperty("showDropIndicator", True)
        self.io_table.setGridStyle(QtCore.Qt.SolidLine)
        self.io_table.setWordWrap(True)
        self.io_table.setCornerButtonEnabled(True)
        self.io_table.setRowCount(30)
        self.io_table.setObjectName("io_table")
        self.io_table.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.io_table.setHorizontalHeaderItem(4, item)
        self.io_table.horizontalHeader().setVisible(True)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        font.setBold(True)
        self.io_table.horizontalHeader().setFont(font)
        self.io_table.horizontalHeader().setFixedHeight(40)
        self.io_table.horizontalHeader().setCascadingSectionResizes(False)
        self.io_table.horizontalHeader().setDefaultSectionSize(200)
        self.io_table.horizontalHeader().setHighlightSections(True)
        self.io_table.horizontalHeader().setMinimumSectionSize(20)
        self.io_table.horizontalHeader().setSortIndicatorShown(False)
        self.io_table.horizontalHeader().setStretchLastSection(False)
        self.io_table.verticalHeader().setVisible(False)
        self.io_table.verticalHeader().setCascadingSectionResizes(False)
        self.io_table.verticalHeader().setDefaultSectionSize(40)
        self.io_table.verticalHeader().setMinimumSectionSize(25)
        self.io_delete_btn = QtWidgets.QPushButton(self.io_tab)
        self.io_delete_btn.setGeometry(QtCore.QRect(1170, 740, 141, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.io_delete_btn.setFont(font)
        self.io_delete_btn.setStyleSheet("background-color: rgb(229, 229, 229);\n"
                                         "")
        self.io_delete_btn.setObjectName("io_delete_btn")
        self.tabWidget.addTab(self.io_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        main_widget = QtWidgets.QWidget() # 例項化一個widget控制元件
        main_layout = QtWidgets.QHBoxLayout() # 例項化一個水平佈局層
        main_widget.setLayout(main_layout) # 設定widget控制元件佈局為水平佈局
        # 例項化3個按鈕
        
        
        #人臉註冊訊息
        for i in range(10):
            widget = QtWidgets.QWidget()
            widget.setFixedSize(250, 100)
            widget.setStyleSheet("background-color: #91A0AA")
            layout = QtWidgets.QGridLayout()
            label1 = QtWidgets.QLabel("辨識項目")
            label1.setStyleSheet(
                "color: #000000; font-size:20px; font-weight:bold; font-family: 微軟正黑體;")
            layout.addWidget(label1, 0, 0)
            label2 = QtWidgets.QLabel("員工編號")
            label2.setStyleSheet(
                "color: #000000; background-color: #768895;padding-left: 5; font-size:16px; font-weight:bold; font-family: 微軟正黑體;")
            layout.addWidget(label2, 0, 1)
            label3 = QtWidgets.QLabel("日期\n時間")
            label3.setStyleSheet(
                "color: #000000; font-size: 14px; font-weight:bold; font-family: 微軟正黑體;")
            layout.addWidget(label3, 1, 0)
            label4 = QtWidgets.QLabel("員工姓名")
            label4.setStyleSheet(
                "color: #000000; background-color: #768895;padding-left: 5; font-size:16px; font-weight:bold; font-family: 微軟正黑體;")
            layout.addWidget(label4, 1, 1)
            widget.setLayout(layout)
            self.face_reg_layout.addWidget(widget)
        # 人臉辨識訊息
        for i in range(10):
            label = QtWidgets.QLabel("label")
            label.setFixedSize(230, 100)
            label.setStyleSheet("background-color: #91A0AA"
                                )
            self.face_layout.addWidget(label)

        # 工廠辨識訊息
        for i in range(10):
            label = QtWidgets.QLabel("label")
            label.setFixedSize(230, 100)
            label.setStyleSheet("background-color: #91A0AA"
                                )
            self.factory_layout.addWidget(label)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "工廠安全之員工服儀智慧辨識系統"))
        self.label.setText(_translate("MainWindow", "time"))
        self.close_btn.setText(_translate("MainWindow", "關閉系統"))
        self.label_3.setText(_translate("MainWindow", "登入管理者"))
        self.face_reg_scr.setText(_translate("MainWindow", "Monitor screen"))
        self.gen_features_btn.setText(_translate("MainWindow", "擷取特徵"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.face_reg_tab), _translate("MainWindow", "人臉註冊"))
        self.face_scr.setText(_translate("MainWindow", "Monitor screen"))
        self.face_rec_label.setText(_translate("MainWindow", "人臉辨識紀錄"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.face_tab), _translate("MainWindow", "人臉辨識"))
        self.factory_scr.setText(_translate("MainWindow", "Monitor screen"))
        self.factory_rec_label.setText(_translate("MainWindow", "安全辨識紀錄"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.factory_tab), _translate("MainWindow", "安全辨識"))
        self.score_table.setSortingEnabled(False)
        item = self.score_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.score_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.score_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.score_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.score_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.score_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.score_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.score_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.score_table.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.score_table.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.score_table.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.score_table.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.score_table.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.score_table.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.score_table.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.score_table.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.score_table.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.score_table.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "18"))
        item = self.score_table.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "19"))
        item = self.score_table.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "20"))
        item = self.score_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "人員編號"))
        item = self.score_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "人員姓名"))
        item = self.score_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "扣分項目"))
        item = self.score_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "扣除分數"))
        item = self.score_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "人員總分"))
        self.score_delete_btn.setText(_translate("MainWindow", "刪除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.score_tab), _translate("MainWindow", "分數紀錄表"))
        self.io_table.setSortingEnabled(False)
        item = self.io_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.io_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.io_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.io_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.io_table.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.io_table.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.io_table.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.io_table.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.io_table.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.io_table.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.io_table.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.io_table.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.io_table.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.io_table.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.io_table.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.io_table.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.io_table.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.io_table.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "18"))
        item = self.io_table.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "19"))
        item = self.io_table.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "20"))
        item = self.io_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "人員編號"))
        item = self.io_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "人員姓名"))
        item = self.io_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "人員身分"))
        item = self.io_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "進廠時間"))
        item = self.io_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "出廠時間"))
        self.io_delete_btn.setText(_translate("MainWindow", "刪除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.io_tab), _translate("MainWindow", "進出紀錄表"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
