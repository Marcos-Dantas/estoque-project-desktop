# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(598, 465)
        Login.setStyleSheet(u"background-color: rgb(137, 182, 178);")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 50, 481, 361))
        self.frame.setStyleSheet(u"background-color: rgb(84, 112, 109);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_login = QLineEdit(self.frame)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setGeometry(QRect(110, 150, 261, 31))
        font = QFont()
        font.setPointSize(11)
        self.txt_login.setFont(font)
        self.txt_login.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;")
        self.txt_login.setAlignment(Qt.AlignCenter)
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(110, 230, 261, 31))
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(170, 280, 151, 31))
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(99, 99, 99);\n"
"	\n"
"	color: rgb(186, 186, 186);\n"
"\n"
"\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 0, 131, 131))
        self.label.setPixmap(QPixmap(u"img/Usuario.png"))
        self.label.setScaledContents(False)
        self.n_senha = QLabel(self.frame)
        self.n_senha.setObjectName(u"n_senha")
        self.n_senha.setGeometry(QRect(110, 200, 131, 31))
        self.n_user = QLabel(self.frame)
        self.n_user.setObjectName(u"n_user")
        self.n_user.setGeometry(QRect(110, 120, 131, 31))
        self.n_user.raise_()
        self.n_senha.raise_()
        self.label.raise_()
        self.txt_login.raise_()
        self.txt_password.raise_()
        self.btn_login.raise_()
        QWidget.setTabOrder(self.txt_login, self.txt_password)
        QWidget.setTabOrder(self.txt_password, self.btn_login)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.txt_login.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Passoword", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.label.setText("")
        self.n_senha.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:14pt; color:#232323;\">Senha:</span></p></body></html>", None))
        self.n_user.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:14pt; color:#232323;\">Usu\u00e1rio:</span></p></body></html>", None))
    # retranslateUi

