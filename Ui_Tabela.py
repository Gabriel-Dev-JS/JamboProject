# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newJambo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Tela(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(911, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 911, 81))
        self.frame.setStyleSheet(u"background-color: rgb(255, 244, 250);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_sair = QPushButton(self.frame)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setGeometry(QRect(260, 20, 411, 28))
        self.btn_sair.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 80, 911, 521))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 244, 250);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.estoque = QTabWidget(self.page)
        self.estoque.setObjectName(u"estoque")
        self.estoque.setGeometry(QRect(20, 50, 511, 371))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 10, 501, 331))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.estoque.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(45, 49, 121, 16))
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(45, 106, 101, 16))
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(45, 163, 101, 16))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(45, 277, 121, 16))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(45, 220, 111, 16))
        self.lineEdit_7 = QLineEdit(self.tab_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_7.setGeometry(QRect(280, 106, 200, 22))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QLineEdit(self.tab_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_6.setGeometry(QRect(280, 49, 200, 22))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_9 = QLineEdit(self.tab_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(280, 220, 200, 22))
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 244, 250);\n"
                                      "background-color: rgb(255, 255, 255);")
        self.lineEdit_8 = QLineEdit(self.tab_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(280, 163, 200, 22))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 244, 250);\n"
                                      "background-color: rgb(255, 255, 255);")
        self.lineEdit_10 = QLineEdit(self.tab_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(280, 277, 200, 22))
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_11 = QLineEdit(self.tab_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setEnabled(True)
        self.lineEdit_11.setGeometry(QRect(280, 0, 200, 22))
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(45, 10, 121, 16))
        self.estoque.addTab(self.tab_2, "")
        self.btn_alterar = QPushButton(self.page)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setGeometry(QRect(560, 100, 201, 28))
        self.btn_alterar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_excluir = QPushButton(self.page)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setGeometry(QRect(560, 290, 201, 28))
        self.btn_excluir.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_adicionar = QPushButton(self.page)
        self.btn_adicionar.setObjectName(u"btn_adicionar")
        self.btn_adicionar.setGeometry(QRect(560, 200, 201, 28))
        self.btn_adicionar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_listar = QPushButton(self.page)
        self.btn_listar.setObjectName(u"btn_listar")
        self.btn_listar.setGeometry(QRect(560, 370, 201, 28))
        self.btn_listar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lineEdit = QLineEdit(self.page_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(85, 190, 640, 40))
        self.lineEdit_2 = QLineEdit(self.page_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(85, 120, 640, 40))
        self.lineEdit_3 = QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(85, 50, 640, 40))
        self.lineEdit_4 = QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(85, 320, 640, 40))
        self.lineEdit_5 = QLineEdit(self.page_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(85, 260, 640, 40))
        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(110, 400, 581, 28))
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.estoque.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_sair.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"produto", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"valor", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"quantidade", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"validade", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"data_entrada", None));
        self.estoque.setTabText(self.estoque.indexOf(self.tab),
                                QCoreApplication.translate("MainWindow", u"estoque", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"VALOR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DATA_ENTRADA", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"VALIDADE", None))
        self.lineEdit_6.setText("")
        self.lineEdit_11.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.estoque.setTabText(self.estoque.indexOf(self.tab_2),
                                QCoreApplication.translate("MainWindow", u"adicionar", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERAR", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.btn_adicionar.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR", None))
        self.btn_listar.setText(QCoreApplication.translate("MainWindow", u"LISTAR", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
    # retranslateUi



