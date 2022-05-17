
# ------------------------
# Description
# 個人照片：photo(300*300)
# 員工編號：id_label
# 員工姓名：name_label
# 員工身分：identity_label
# 目前總分：score_label
# 統計圖表：chart_photo(381*451)
# 關閉按鈕：close_btn
# ------------------------
# 內有讀取圖片範例程式
# 搜尋: 圖片範例
# ------------------------

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib
matplotlib.use('Qt5Agg')


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(781, 581)
        Form.setStyleSheet("background-color: #2D3142;")
        self.close_btn = QtWidgets.QPushButton(Form)
        self.close_btn.setGeometry(QtCore.QRect(30, 530, 301, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setStyleSheet("background-color: #E5E5E5;height: 30px;")
        self.close_btn.setObjectName("close_btn")
        self.identity_title = QtWidgets.QLabel(Form)
        self.identity_title.setGeometry(QtCore.QRect(19, 440, 81, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.identity_title.setFont(font)
        self.identity_title.setAccessibleDescription("")
        self.identity_title.setStyleSheet("color: #E5E5E5;")
        self.identity_title.setAlignment(QtCore.Qt.AlignCenter)
        self.identity_title.setObjectName("identity_title")
        self.photo = QtWidgets.QLabel(Form)
        self.photo.setEnabled(True)
        self.photo.setGeometry(QtCore.QRect(30, 20, 300, 300))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.photo.setFont(font)
        self.photo.setStyleSheet("background-color: #546A7B;")
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.score_label = QtWidgets.QLabel(Form)
        self.score_label.setGeometry(QtCore.QRect(100, 480, 231, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.score_label.setFont(font)
        self.score_label.setStyleSheet("color: #E5E5E5;\n"
                                       "background-color: #546A7B;padding-left:8;")
        self.score_label.setObjectName("score_label")
        self.name_label = QtWidgets.QLabel(Form)
        self.name_label.setGeometry(QtCore.QRect(100, 400, 231, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: #E5E5E5;\n"
                                      "background-color: #546A7B;padding-left:8;")
        self.name_label.setObjectName("name_label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 340, 321, 1))
        self.line.setStyleSheet("background: #E5E5E5;\n"
                                "max-height: 1px;\n"
                                "border: none;\n"
                                "")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.name_title = QtWidgets.QLabel(Form)
        self.name_title.setGeometry(QtCore.QRect(19, 400, 81, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_title.setFont(font)
        self.name_title.setStyleSheet("color: #E5E5E5;")
        self.name_title.setAlignment(QtCore.Qt.AlignCenter)
        self.name_title.setObjectName("name_title")
        self.identity_label = QtWidgets.QLabel(Form)
        self.identity_label.setGeometry(QtCore.QRect(100, 440, 231, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.identity_label.setFont(font)
        self.identity_label.setAccessibleDescription("")
        self.identity_label.setStyleSheet("color: #E5E5E5;\n"
                                          "background-color: #546A7B;padding-left:8;")
        self.identity_label.setObjectName("identity_label")
        self.score_title = QtWidgets.QLabel(Form)
        self.score_title.setGeometry(QtCore.QRect(19, 480, 81, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.score_title.setFont(font)
        self.score_title.setStyleSheet("color: #E5E5E5;")
        self.score_title.setAlignment(QtCore.Qt.AlignCenter)
        self.score_title.setObjectName("score_title")
        self.id_title = QtWidgets.QLabel(Form)
        self.id_title.setGeometry(QtCore.QRect(19, 360, 81, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.id_title.setFont(font)
        self.id_title.setStyleSheet("color: #E5E5E5;")
        self.id_title.setAlignment(QtCore.Qt.AlignCenter)
        self.id_title.setObjectName("id_title")
        self.id_label = QtWidgets.QLabel(Form)
        self.id_label.setGeometry(QtCore.QRect(100, 360, 231, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.id_label.setFont(font)
        self.id_label.setStyleSheet("color: #E5E5E5;\n"
                                    "background-color: #546A7B;padding-left:8;")
        self.id_label.setObjectName("id_label")
        self.chart_line = QtWidgets.QLabel(Form)
        self.chart_line.setGeometry(QtCore.QRect(350, 70, 401, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.chart_line.setFont(font)
        self.chart_line.setStyleSheet("color: #000000;\n"
                                      "background-color: #f5cb5c;padding-left:8;")
        self.chart_line.setText("")
        self.chart_line.setObjectName("chart_line")
        self.chart_title = QtWidgets.QLabel(Form)
        self.chart_title.setGeometry(QtCore.QRect(350, 30, 141, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.chart_title.setFont(font)
        self.chart_title.setStyleSheet("color: #E5E5E5;")
        self.chart_title.setAlignment(QtCore.Qt.AlignCenter)
        self.chart_title.setObjectName("chart_title")
        self.chart_photo = QtWidgets.QLabel(Form)
        self.chart_photo.setEnabled(True)
        self.chart_photo.setGeometry(QtCore.QRect(360, 100, 381, 451))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.chart_photo.setFont(font)
        self.chart_photo.setStyleSheet("background-color: #546A7B;")
        self.chart_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.chart_photo.setObjectName("chart_photo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "員工資料"))
        self.close_btn.setText(_translate("Form", "關閉"))
        self.identity_title.setText(_translate("Form", "員工身分"))
        self.photo.setText(_translate("Form", "Photo"))
        self.score_label.setText(_translate("Form", "Score"))
        self.name_label.setText(_translate("Form", "Name"))
        self.name_title.setText(_translate("Form", "員工姓名"))
        self.identity_label.setText(_translate("Form", "Identity"))
        self.score_title.setText(_translate("Form", "目前總分"))
        self.id_title.setText(_translate("Form", "員工編號"))
        self.id_label.setText(_translate("Form", "ID"))
        self.chart_title.setText(_translate("Form", "個人統計圖表"))
        self.chart_photo.setText(_translate("Form", "Chart"))

        # 圖片範例-------------------------------------------------------
        photo = QtGui.QPixmap('good.jpg').scaled(
            300, 300, QtCore.Qt.KeepAspectRatio)
        # Qt.KeepAspectRatio: 保留圖片原長寬比顯示
        self.photo.setPixmap(photo)

        chart = QtGui.QPixmap('./good.jpg')
        self.chart_photo.setPixmap(chart)
        self.chart_photo.setScaledContents(True)
        # setScaledContents: 圖片配合label大小縮放顯示
        # --------------------------------------------------------------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
