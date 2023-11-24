# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newTela.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(721, 587)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.264, y1:0.204864, x2:0.975, y2:1, stop:0.00497512 rgba(255, 130, 142, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 170, 651, 321))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.264, y1:0.204864, x2:0.975, y2:1, stop:0.00497512 rgba(255, 130, 142, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 271, 201))
        self.label_2.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0.264, y1:0.204864, x2:0.975, y2:1, stop:0.00497512 rgba(255, 130, 142, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(340, 20, 281, 541))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.264, y1:0.204864, x2:0.975, y2:1, stop:0.00497512 rgba(255, 130, 142, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 290, 281, 251))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.text_usuario = QLineEdit(self.frame_3)
        self.text_usuario.setObjectName(u"text_usuario")
        self.text_usuario.setGeometry(QRect(80, 80, 113, 22))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_usuario.sizePolicy().hasHeightForWidth())
        self.text_usuario.setSizePolicy(sizePolicy)
        self.text_usuario.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.text_senha = QLineEdit(self.frame_3)
        self.text_senha.setObjectName(u"text_senha")
        self.text_senha.setGeometry(QRect(80, 140, 113, 22))
        self.text_senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 190, 93, 28))
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(False)
        self.frame_4.setGeometry(QRect(30, 60, 221, 151))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 141, 61))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"  CAFETERIA \n"
" JAMBO-ROSA", None))
        self.text_usuario.setText("")
        self.text_usuario.setPlaceholderText(QCoreApplication.translate("Form", u"USUARIO", None))
        self.text_senha.setPlaceholderText(QCoreApplication.translate("Form", u"SENHA", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"LOGAR", None))
        self.label.setText(QCoreApplication.translate("Form", u"       LOGIN", None))
    # retranslateUi

