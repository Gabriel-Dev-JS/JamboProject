from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget,QTableWidgetItem,QTabWidget,QTableWidget)
from Ui_Login import Ui_Form
from Ui_Tabela import Ui_Tela
from DataBase import Banco

import sys

########## INSTANCIEI A TELA DE LOGIN ##########
class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do sistema")
        self.pushButton.clicked.connect(self.abrirSistema)

########### CRIEI UM SISTEMA DE VALIDAÇÃO #########
    def abrirSistema(self):
        if self.text_usuario.text() == "admin" and self.text_senha.text() == "123":
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print('senha invalida')

######### INSTANCIEIA A TELA RPINCIPAL COM A TABELA ############
class MainWindow(QMainWindow, Ui_Tela, QTabWidget,QTableWidget):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gerenciamento de estoque")

        self.btn_adicionar.clicked.connect(self.inserir_estoque)
        self.btn_excluir.clicked.connect(self.delete)
        self.btn_listar.clicked.connect(self.trazer_dados)

    ######FUNÇÕES VINDO DO BDD########

    ###### FUNÇÃO DE INSERIR NO ESTOQUE
    def inserir_estoque(self):
        db = Banco()
        db.conexao()
        dados = (self.lineEdit_6.text(),self.lineEdit_7.text(),self.lineEdit_8.text(),self.lineEdit_9.text(),self.lineEdit_10.text())
        db.registrar_estoque(dados)
        return db.encerrar()


    #######FUNÇÃO DE DELETE##########3
    def delete(self):
        db = Banco()
        db.conexao()
        id = (self.lineEdit_11.text())
        return db.deletar_produto(id)
        db.encerrar()

    ############## FUNÇÃO PARA TRAZER DO BDD ########
    def trazer_dados(self):
        db = Banco()
        db.conexao()
        resultado = db.consultar_estoque()
        for i in resultado:
            print(i)
        #db.encerrar()
        #return
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))
        db.encerrar()
        return

    def atualizar(self):
        db.Banco()
        db.conexao()

if __name__ == "__main__":
    db = Banco()
    db.conexao()
    db.criar_tabela()
    db.encerrar()

    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()

