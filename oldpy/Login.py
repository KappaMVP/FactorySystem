import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from logingui import Ui_Dialog  #由.UI檔案生成.py檔案後，匯入建立的GUI類

from test1 import *

#python mysql
import pymysql


class Login_window(QtWidgets.QMainWindow,Ui_Dialog):  
    
    connect = pymysql.connect(host='Localhost',port=3306, user="root",password="",db="test")
    name = "fuckyou"
    def __init__(self):  
        super(Login_window, self).__init__()  
        self.setupUi(self)
        self.pushButton.setText("登入")
        self.pushButton_2.setText("取消")  
        
        self.pushButton.clicked.connect(self.btn_login_fuc) 
        self.pushButton_2.clicked.connect(self.btn_cancel)
        
        #buttonfunction
    def btn_login_fuc(self):
        cursor = self.connect.cursor()
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        sql = 'select * from login where account="%s" and password="%s"'%(account,password)
        cursor.execute(sql)
        a = cursor.fetchone()
        if cursor.rowcount==0:
            QMessageBox.warning(self, "warning","帳密錯誤")
        else:
            self.name = a[1]
            window.show()
            self.close()
            
    def btn_cancel(self):
        self.close()
    
    def username(self):
        return self.name


if __name__ == '__main__': #如果這個檔案是主程式。
    app = QtWidgets.QApplication(sys.argv) #QApplication相當於main函式，也就是整個程式（很多檔案）的主入口函式。對於GUI程式必須至少有一個這樣的例項來讓程式執行。
    login = Login_window() #生成一個例項（物件）
    window = MainWindow() #生成主視窗的例項
    login.show() #有了例項，就得讓它顯示。這裡的show()是QWidget的方法，用來顯示視窗。
    sys.exit(app.exec_()) # 呼叫sys庫的exit退出方法，條件是app.exec_()也就是整個視窗關閉。
    