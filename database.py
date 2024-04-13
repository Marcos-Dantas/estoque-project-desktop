import sqlite3
from sqlite3.dbapi2 import Cursor

class DataBase():
    def __init__(self, name="system.db") -> None:
        self.name = name
        self.connection = None  # Inicialize a conexão como None

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL
                );
            """)
            self.connection.commit()  # Commit após criar a tabela
        except AttributeError:
            print("Faça a conexão")

    def insert_user(self, name, user, password, access):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)
            """, (name, user, password, access))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Nome de usuário já existe. Por favor, escolha outro nome de usuário.")

    def check_user(self, user, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM users;
            """)
            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Administrador":
                    return "Administrador"
                elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Usuário":
                    return "user"
                else:
                    continue
            return "sem acesso"
        except:
            pass
    
    def insert_data(self, full_dataset):

        cursor = self.connection.cursor()

        campos_tabela = (
            'quantidade','medicacao','datadeentrada','datadesaida','usuario', 'paciente')  
        qntd = ','.join(map(str, '?'*6))
        query = f"""INSERT INTO Notas {campos_tabela} VALUES ({qntd})"""

        try:
            cursor.execute(query, tuple(full_dataset)) 
            self.connection.commit()
        except sqlite3.IntegrityError:
            print('Nota já existe no banco')
    
    def create_table_nfe(self):

        cursor = self.connection.cursor()

        cursor.execute(f"""

            CREATE TABLE IF NOT EXISTS Notas(

            quantidade TEXT,
            medicacao TEXT,
            datadeentrada TEXT,
            datadesaida TEXT,
            paciente TEXT,
            usuario TEXT,
        
        PRIMARY KEY(quantidade, medicacao, paciente)                

            );

        """)

if __name__ == "__main__":
    db = DataBase()
    db.connect()
    db.create_table_users()
    db.create_table_nfe()
    db.close_connection()
