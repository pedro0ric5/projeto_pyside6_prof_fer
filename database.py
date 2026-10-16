import sqlite3

class Database:
    def __init__(self, name = 'system.db'):
        self.name: str = name
        self.connection: sqlite3.Connection

    def connection(self):
        self.connection = sqlite3.Connection(self.name)

    def close_connection(self):
        try:
            if self.connection:
                self.connection.close()

        except sqlite3.Error as e:
            print("Erro ao fechar conexão: {e}")

    def create_table_empresa(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Empresa
            (
                CNPJ TEXT,
                NOME TEXT,
                LOGRADOURO TEXT,
                NUMERO TEXT,
                COMPLEMENTO TEXT,
                BAIRRO TEXT,
                MUNICIPIO TEXT,
                UF TEXT,
                CEP TEXT,
                TELEFONE TEXT,
                EMAIL TEXT,
                PRIMARY KEY(CNPJ)
            );"""
        )

    def register_empresa(self, fullDataSet):
        campos_tabela = ('CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL')
        qtd = ('?', '?','?','?','?','?','?','?','?','?','?' )
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""INSERT INTO Empresa {campos_tabela} VALUES({qtd}),""", fullDataSet)
            return("ok")
        except:
            return "ERRO"
    def select_all_empresa(self):
        try:
            cursor = self.close_connection.cursor()
            cursor.execute("SELECT * FROM Empresa ORDER BY NOME")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass
    def delete_empresa(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Empresa WHERE CNPJ = '{id}' ")
            self.connection.commit()
            return "empresa excluida com sucesso!"
        except:
            return "erro ao excluir registro"
    def update_empresa(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Empresa set
            CNPJ
            NOME
            LOOGADOURO
            NUMERO
            COMPLEMENTP
            BAIRRO
            MUNICIPIO
            UF
            CEP
            TELEFONE
            EMAIL
            WHERE CNPJJ = = '{fullDataSet[0]}'""")
        self.connection.commit ()