import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi



class Welcome(QDialog):
    def __init__(self):
        super(Welcome,self).__init__()
        loadUi("welcome.ui",self)


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbtn.clicked.connect(self.loginfunction)
        self.cancelbtn.clicked.connect(self.closeIt)
        self.psswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.emailerror.setVisible(False)

    def loginfunction(self):
        email=self.emailinput.text()
        password=self.psswd.text()
        try:
                       
            # print(email,password)
            welcome = Welcome()
            widget.addWidget(welcome)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            
        except:
            self.emailerror.setVisible(True)

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() +1 )

    def closeIt(self): 
        widget.close()

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("register.ui",self)
        self.regbtn.clicked.connect(self.createaccfunction)
        self.cancelbtn.clicked.connect(self.closeIt)
        self.pswdr.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repswdr.setEchoMode(QtWidgets.QLineEdit.Password)
        self.emailerror.setVisible(False)
        self.pswderror.setVisible(False)

    def createaccfunction(self):
        email = self.emailinputr.text()
        if self.pswdr.text()==self.repswdr.text():
            password=self.pswdr.text()
            try:
               
                # print(email,password)
                login = Login()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex() - 1)
            except:
                self.emailerror.setVisible(True)
        else:
            self.pswderror.setVisible(True)

    def closeIt(self): 
        self.close()
        widget.setCurrentIndex(widget.currentIndex() - 1)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=Login()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(880)
    widget.setFixedHeight(620)
    widget.show()
    app.exec_()