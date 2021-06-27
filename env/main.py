import sys
from PyQt5 import QtWidgets, QtSql
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi



class Welcome(QDialog):
    def __init__(self):
        super(Welcome,self).__init__()
        loadUi("welcome.ui",self)
        self.logoutbtn.clicked.connect(self.logoutfunction)

    def logoutfunction(self): 
        widget.close()
        widget.setCurrentIndex(widget.currentIndex() - 1)


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.openDB()
        self.loginbtn.clicked.connect(self.loginfunction)
        self.cancelbtn.clicked.connect(self.closeIt)
        self.psswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.emailerror.setVisible(False)

    def openDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.sqlite")
        if not self.db.open():
            print("error")
        self.query = QtSql.QSqlQuery()

    def loginfunction(self):
        email=self.emailinput.text()
        password=self.psswd.text()
        self.query.exec_("select * from users where email = '%s' and password = '%s';"%(email,password))
        self.query.first()
        if self.query.value("email") != None and self.query.value("password") != None:
            # print(email,password)
            welcome = Welcome()
            widget.addWidget(welcome)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            self.emailerror.setVisible(True)

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() +1 )

    def closeIt(self): 
        widget.close()
        widget.setCurrentIndex(widget.currentIndex() - 1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("register.ui",self)
        self.query = QtSql.QSqlQuery()
        self.regbtn.clicked.connect(self.createaccfunction)
        self.cancelbtn.clicked.connect(self.closeIt)
        self.pswdr.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repswdr.setEchoMode(QtWidgets.QLineEdit.Password)
        self.emailerror.setVisible(False)
        self.pswderror.setVisible(False)
        

    def createaccfunction(self):
        email = self.emailinputr.text().isEmpty()
        if self.pswdr.text()==self.repswdr.text():
            password=self.pswdr.text()
            self.query.exec_("select * from users where email = '%s';"%(email))
            self.query.first()
            if self.query.value("email") == None:
                self.query.exec_("insert into users (email, password) values('%s','%s');"%(email,password))
                # self.query.first()
                # print(email,password)
                login = Login()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
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