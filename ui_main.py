# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableView, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(825, 549)
        MainWindow.setStyleSheet(u"background-color: rgb(16, 33, 109);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_Home = QPushButton(self.frame)
        self.btn_Home.setObjectName(u"btn_Home")
        self.btn_Home.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(53, 82, 162);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"color: white;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff; color:black;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_Home)

        self.btn_tabelas = QPushButton(self.frame)
        self.btn_tabelas.setObjectName(u"btn_tabelas")
        self.btn_tabelas.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(53, 82, 162);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"color: white;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff; color:black;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_tabelas)

        self.btn_pg_import = QPushButton(self.frame)
        self.btn_pg_import.setObjectName(u"btn_pg_import")
        self.btn_pg_import.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(53, 82, 162);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"color: white;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff; color:black;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_pg_import)


        self.verticalLayout.addWidget(self.frame)

        self.Page = QStackedWidget(self.centralwidget)
        self.Page.setObjectName(u"Page")
        self.Page.setStyleSheet(u"background-color: rgb(53, 82, 162);\n"
"border-radius:0px;\n"
"")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_8 = QVBoxLayout(self.pg_table)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"border-radius:0px;")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_7 = QVBoxLayout(self.tables)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_file = QLineEdit(self.tables)
        self.txt_file.setObjectName(u"txt_file")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_file.sizePolicy().hasHeightForWidth())
        self.txt_file.setSizePolicy(sizePolicy)
        self.txt_file.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"height: 20px;\n"
"border-radius: 5px;")

        self.horizontalLayout_2.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.tables)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(16, 33, 109);\n"
"color:white;\n"
"font-weight:bold;\n"
"width:60px;\n"
"height:20px;\n"
"border-radius:5px;\n"
"font-size:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.tw_estoque)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")
        self.tw_saida.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_importe = QPushButton(self.frame_2)
        self.btn_importe.setObjectName(u"btn_importe")
        self.btn_importe.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(16, 33, 109);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"color: white;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff; color:black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_importe)

        self.btn_gesaida = QPushButton(self.frame_2)
        self.btn_gesaida.setObjectName(u"btn_gesaida")
        self.btn_gesaida.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(16, 33, 109);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"color: white;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff; color:black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_gesaida)

        self.btn_estorno = QPushButton(self.frame_2)
        self.btn_estorno.setObjectName(u"btn_estorno")
        self.btn_estorno.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(16, 33, 109);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"color: white;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #fff; color:black;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_estorno)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        font = QFont()
        font.setPointSize(19)
        self.label_18.setFont(font)

        self.verticalLayout_11.addWidget(self.label_18)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_chart = QPushButton(self.tab_2)
        self.btn_chart.setObjectName(u"btn_chart")
        self.btn_chart.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(176, 176, 176);\n"
" color:black;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.btn_chart)

        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 3px;\n"
"font-size: 16px;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(176, 176, 176);\n"
" color:black;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.btn_excel)


        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        self.txt_filtro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"height:27px;")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.txt_filtro)

        self.tb_estoque = QTableView(self.tab_2)
        self.tb_estoque.setObjectName(u"tb_estoque")

        self.verticalLayout_11.addWidget(self.tb_estoque)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Page.addWidget(self.pg_table)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(53, 82, 162);\n"
"border-radius:10px;")

        self.verticalLayout_2.addWidget(self.label)

        self.Page.addWidget(self.pg_home)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.verticalLayout_10 = QVBoxLayout(self.pg_import)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_15 = QLabel(self.pg_import)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_10.addWidget(self.label_15)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit = QLineEdit(self.pg_import)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"height:27px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lineEdit)

        self.btn_open_2 = QPushButton(self.pg_import)
        self.btn_open_2.setObjectName(u"btn_open_2")
        self.btn_open_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"font-size: 16px;\n"
"height: 30px;\n"
"width:90px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(176, 176, 176);\n"
" color:black;\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.btn_open_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.pg_import)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_12.addWidget(self.label_16)

        self.btn_import = QPushButton(self.pg_import)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"font-size: 16px;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(176, 176, 176);\n"
" color:black;\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.btn_import)

        self.label_17 = QLabel(self.pg_import)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.Page.addWidget(self.pg_import)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")

        self.horizontalLayout_8.addWidget(self.txt_nome)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")

        self.horizontalLayout_7.addWidget(self.txt_usuario)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.txt_senha2 = QLineEdit(self.pg_cadastro)
        self.txt_senha2.setObjectName(u"txt_senha2")
        self.txt_senha2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.txt_senha2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_cadastrar.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.Page.addWidget(self.pg_cadastro)

        self.verticalLayout.addWidget(self.Page)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.btn_pg_cadastro = QPushButton(self.centralwidget)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")

        self.horizontalLayout_4.addWidget(self.btn_pg_cadastro)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Page.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_Home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_tabelas.setText(QCoreApplication.translate("MainWindow", u"TABELAS", None))
        self.btn_pg_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Data de Entrada", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Medica\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SAIDA", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Paciente", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data de sa\u00edda", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Medica\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        self.btn_importe.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gesaida.setText(QCoreApplication.translate("MainWindow", u"Gerar sa\u00edda", None))
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"Base", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Estoque</span></p></body></html>", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"Gerar Gr\u00e1fico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_filtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">PYGEN</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">IMPORTAR XML</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione o arquivo", None))
        self.btn_open_2.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_16.setText("")
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_17.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">tela de cadrasto</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Perfil:", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Admin", None))

        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_4.setText("")
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_5.setText("")
    # retranslateUi

