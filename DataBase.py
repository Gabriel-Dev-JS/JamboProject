import sqlite3
class Banco():
    def __init__(self, nome="estoque.db") ->None:
        self.nome = nome
    def conexao(self):
        self.connection = sqlite3.connect(self.nome)

#######CRUD########

    #####CRIEI TABELA#######
    def criar_tabela(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS estoque(id INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT, valor TEXT, quantidade INTEGER, validade TEXT, data_entrada TEXT)')
            self.connection.commit()
        except:
            pass

    ######## FUNÇÃO DE INSERIR NA TABELA#######
    def registrar_estoque(self, dados):


        campo_tabela = ('produto', 'valor', 'quantidade', 'validade', 'data_entrada')
        quan = ("?,?,?,?,?")

        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" INSERT INTO estoque {campo_tabela} VALUES ({quan})""", dados)
            self.connection.commit()
        except:
            pass

    #########FUNÇÃO DE CONSULTAR TABELA########
    def consultar_estoque(self):
         try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM estoque ORDER BY produto ")
            produtos = cursor.fetchall()
            return produtos
         except:
             pass

    #######FUNÇÃO DE DELETAR DA TABELA######
    def deletar_produto(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f" DELETE FROM estoque WHERE id = '{id}'")
            self.connection.commit()

        except:
            pass

    #####FECHAR CONEXÃO
    def encerrar(self):
        try:
            self.connection.close()
        except:
            pass





if __name__ == "__main__":
    db = Banco()
    db.conexao()
    db.criar_tabela()
    db.registrar_estoque()
    db.consultar_estoque()
    db.deletar_produto(id)
    db.encerrar()
