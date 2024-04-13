from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QWidget,QMessageBox, QTreeWidgetItem
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
import sys
from database import DataBase
from xml_files import Read_xml
import sqlite3
import pandas as pd
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

class Login(QWidget, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.tentativas = 0
        self.setWindowTitle("Login do Sistema")

        self.btn_login.clicked.connect(self.open_system)

    def open_system(self):

        if self.txt_password.text() == '123':
            if self.txt_login.text() == 'Joao':
                self.w = MainWindow()
                self.w.show()
                self.close()

            else:
                print('Senha invalida')

    def checkLogin(self):
        self.users = DataBase()
        self.users.connect()
        autenticado = self.users.check_user(self.txt_login.text().upper(), self.txt_password.text())

        if autenticado.lower() == "administrador" or autenticado.lower() == "user":
            self.users.close_connection()
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou senha incorreto \n \n Tentativa: {self.tentativas +1} de 3')
                msg.exec_()
                self.tentativas += 1
            if self.tentativas == 3:
                self.users.close_connection()
                sys.exit(0)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")
        self.btn_pg_cadastro.setVisible(False)

        #páginas do sistema

        self.btn_Home.clicked.connect(lambda: self.Page.setCurrentWidget(self.pg_home))
        self.btn_tabelas.clicked.connect(lambda: self.Page.setCurrentWidget(self.pg_table))
        self.btn_pg_import.clicked.connect(lambda: self.Page.setCurrentWidget(self.pg_import))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Page.setCurrentWidget(self.pg_cadastro))

        self.btn_cadastrar.clicked.connect(self.subscribe_user)

        #ARQUIVO XML
        self.btn_open_2.clicked.connect(self.open_path)
        self.btn_import.clicked.connect(self.import_xml_files)

        self.txt_filtro.textChanged.connect(self.update_filter)

        self.reset_table()



    def subscribe_user(self):

        if self.txt_senha.text() != self.txt_senha2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erro no cadastro!")
            msg.setText("A senha não é igual!")
            msg.exec_()
            return None

        name = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.connect()
        db.insert_user(name,user,password,access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha2.setText("")

    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self,str("Open Directory"),
                                                          "/home",
                                                          QFileDialog.ShowDirsOnly
                                       
                                                          | QFileDialog.DontResolveSymlinks)
        self.lineEdit.setText(self.path)
   
    def import_xml_files(self):
        print(self.lineEdit.text())
        xml = Read_xml(self.lineEdit.text())
        print(xml)
        all = xml.all_files()

        db = DataBase()
        db.connect()
        cont = 1

        for i in all:
            fullDataSet = xml.get_data_xml(i)
            db.insert_data(fullDataSet)
            cont+=1

        #ATUALIZA A TABELA

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importação XML")
        msg.setText("importação concluída!")
        msg.exec_()

        db.close_connection()

    def table_estoque(self):

        cn  =  sqlite3.connect('system.db')
        result = pd.read_sql_query("""SELECT quantidade, medicacao, datadeentrada FROM Notas WHERE datadesaida IS NULL; """, cn)
        print(result)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            #faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_estoque, i)
                self.campo.setCheckState(0, Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_estoque.setSortingEnabled(True)
   
        for i in range(1,15):
            self.tw_estoque.resizeColumnToContents(i)
     
    def table_saida(self):

        cn  =  sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT quantidade, medicacao, datadesaida, paciente FROM Notas WHERE datadesaida IS NOT NULL; ", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            #faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_saida, i)
                self.campo.setCheckState(0, Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_saida.setSortingEnabled(True)
   
        for i in range(1,15):
            self.tw_saida.resizeColumnToContents(i)

    def reset_table(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()

        self.table_saida()
        self.table_estoque()

    def update_filter(self, s):
        pass

    def gerar_saida(self):
        pass

    def gerar_estorno(self):
        pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())
