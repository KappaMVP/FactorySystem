from PyQt5 import QtGui ,QtCore
 
class LoginDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowTitle(u'登入')
        self.resize(300,150)
         
        self.leName =QtGui.QLineEdit(self)
        self.leName.setPlaceholderText(u'使用者名稱')
         
        self.lePassword =QtGui.QLineEdit(self)
        self.lePassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lePassword.setPlaceholderText(u'密碼')
         
        self.pbLogin =QtGui.QPushButton(u'登入',self)
        self.pbCancel =QtGui.QPushButton(u'取消',self)
         
        self.pbLogin.clicked.connect(self.login)
        self.pbCancel.clicked.connect(self.reject)
         
        layout =QtGui.QVBoxLayout()
        layout.addWidget(self.leName)
        layout.addWidget(self.lePassword)
         
        # 放一個間隔物件美化佈局
        spacerItem =QtGui.QSpacerItem(20,48,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
         
        # 按鈕佈局
        buttonLayout =QtGui.QHBoxLayout()
        # 左側放一個間隔
        spancerItem2 =QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        buttonLayout.addItem(spancerItem2)
        buttonLayout.addWidget(self.pbLogin)
        buttonLayout.addWidget(self.pbCancel)
         
        layout.addLayout(buttonLayout)
         
        self.setLayout(layout)
     
    def login(self):
        print('login')
        ifself.leName.text()=='admin'andself.lePassword.text()=='jimmykuu':
            self.accept()# 關閉對話方塊並返回1
    else:
        QtGui.QMessageBox.critical(self, u'錯誤', u'使用者名稱密碼不匹配')
     
 
def login():
"""返回True或False"""
dialog =LoginDialog()
if dialog.exec_():
returnTrue
else:
returnFalse
 
if __name__ =='__main__':
import sys
app =QtGui.QApplication(sys.argv)
if login():
mainWindow =QtGui.QMainWindow()
mainWindow.show()
sys.exit(app.exec_())