# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\ARM_s_CPUI\interface/headers_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Headers(object):
    def setupUi(self, Headers):
        Headers.setObjectName("Headers")
        Headers.resize(976, 627)
        self.hL_Headers = QtWidgets.QHBoxLayout(Headers)
        self.hL_Headers.setObjectName("hL_Headers")
        self.widget_headers_input = QtWidgets.QWidget(Headers)
        self.widget_headers_input.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_headers_input.sizePolicy().hasHeightForWidth())
        self.widget_headers_input.setSizePolicy(sizePolicy)
        self.widget_headers_input.setObjectName("widget_headers_input")
        self.vL_widget_headers_input_list = QtWidgets.QVBoxLayout(self.widget_headers_input)
        self.vL_widget_headers_input_list.setObjectName("vL_widget_headers_input_list")
        self.widget_headers_input_buts = QtWidgets.QWidget(self.widget_headers_input)
        self.widget_headers_input_buts.setObjectName("widget_headers_input_buts")
        self.hL_widget_headers_buts = QtWidgets.QHBoxLayout(self.widget_headers_input_buts)
        self.hL_widget_headers_buts.setObjectName("hL_widget_headers_buts")
        self.pushButton_headers_add = QtWidgets.QPushButton(self.widget_headers_input_buts)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_headers_add.setFont(font)
        self.pushButton_headers_add.setObjectName("pushButton_headers_add")
        self.hL_widget_headers_buts.addWidget(self.pushButton_headers_add)
        self.pushButton_headers_save = QtWidgets.QPushButton(self.widget_headers_input_buts)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_headers_save.setFont(font)
        self.pushButton_headers_save.setObjectName("pushButton_headers_save")
        self.hL_widget_headers_buts.addWidget(self.pushButton_headers_save)
        self.vL_widget_headers_input_list.addWidget(self.widget_headers_input_buts)
        self.label_headers_fullname = QtWidgets.QLabel(self.widget_headers_input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_headers_fullname.setFont(font)
        self.label_headers_fullname.setObjectName("label_headers_fullname")
        self.vL_widget_headers_input_list.addWidget(self.label_headers_fullname)
        self.textEdit_headers_fullname = QtWidgets.QTextEdit(self.widget_headers_input)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_headers_fullname.setFont(font)
        self.textEdit_headers_fullname.setObjectName("textEdit_headers_fullname")
        self.vL_widget_headers_input_list.addWidget(self.textEdit_headers_fullname)
        self.label_headers_prof = QtWidgets.QLabel(self.widget_headers_input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_headers_prof.setFont(font)
        self.label_headers_prof.setObjectName("label_headers_prof")
        self.vL_widget_headers_input_list.addWidget(self.label_headers_prof)
        self.textEdit_headers_prof = QtWidgets.QTextEdit(self.widget_headers_input)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_headers_prof.setFont(font)
        self.textEdit_headers_prof.setObjectName("textEdit_headers_prof")
        self.vL_widget_headers_input_list.addWidget(self.textEdit_headers_prof)
        self.label_headers_phone = QtWidgets.QLabel(self.widget_headers_input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_headers_phone.setFont(font)
        self.label_headers_phone.setObjectName("label_headers_phone")
        self.vL_widget_headers_input_list.addWidget(self.label_headers_phone)
        self.textEdit_headers_phone = QtWidgets.QTextEdit(self.widget_headers_input)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_headers_phone.setFont(font)
        self.textEdit_headers_phone.setObjectName("textEdit_headers_phone")
        self.vL_widget_headers_input_list.addWidget(self.textEdit_headers_phone)
        self.label_headers_mail = QtWidgets.QLabel(self.widget_headers_input)
        self.label_headers_mail.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_headers_mail.setFont(font)
        self.label_headers_mail.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_headers_mail.setObjectName("label_headers_mail")
        self.vL_widget_headers_input_list.addWidget(self.label_headers_mail)
        self.textEdit_headers_mail = QtWidgets.QTextEdit(self.widget_headers_input)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_headers_mail.setFont(font)
        self.textEdit_headers_mail.setObjectName("textEdit_headers_mail")
        self.vL_widget_headers_input_list.addWidget(self.textEdit_headers_mail)
        self.label_headers_web = QtWidgets.QLabel(self.widget_headers_input)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_headers_web.setFont(font)
        self.label_headers_web.setObjectName("label_headers_web")
        self.vL_widget_headers_input_list.addWidget(self.label_headers_web)
        self.textEdit_headers_web = QtWidgets.QTextEdit(self.widget_headers_input)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_headers_web.setFont(font)
        self.textEdit_headers_web.setObjectName("textEdit_headers_web")
        self.vL_widget_headers_input_list.addWidget(self.textEdit_headers_web)
        self.pushButton_headers_back = QtWidgets.QPushButton(self.widget_headers_input)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_headers_back.setFont(font)
        self.pushButton_headers_back.setObjectName("pushButton_headers_back")
        self.vL_widget_headers_input_list.addWidget(self.pushButton_headers_back)
        self.hL_Headers.addWidget(self.widget_headers_input)
        self.widget_left_headers = QtWidgets.QWidget(Headers)
        self.widget_left_headers.setObjectName("widget_left_headers")
        self.vL_widget_left_headers = QtWidgets.QVBoxLayout(self.widget_left_headers)
        self.vL_widget_left_headers.setObjectName("vL_widget_left_headers")
        self.widget_left_up_headers = QtWidgets.QWidget(self.widget_left_headers)
        self.widget_left_up_headers.setObjectName("widget_left_up_headers")
        self.hL_widget_left_up_headers = QtWidgets.QHBoxLayout(self.widget_left_up_headers)
        self.hL_widget_left_up_headers.setObjectName("hL_widget_left_up_headers")
        self.label_search_headers = QtWidgets.QLabel(self.widget_left_up_headers)
        self.label_search_headers.setObjectName("label_search_headers")
        self.hL_widget_left_up_headers.addWidget(self.label_search_headers)
        self.lineEdit_search_headers = QtWidgets.QLineEdit(self.widget_left_up_headers)
        self.lineEdit_search_headers.setObjectName("lineEdit_search_headers")
        self.hL_widget_left_up_headers.addWidget(self.lineEdit_search_headers)
        self.pushButton_headers_delete = QtWidgets.QPushButton(self.widget_left_up_headers)
        self.pushButton_headers_delete.setObjectName("pushButton_headers_delete")
        self.hL_widget_left_up_headers.addWidget(self.pushButton_headers_delete)
        self.vL_widget_left_headers.addWidget(self.widget_left_up_headers)
        self.scrollArea_headers_list = QtWidgets.QScrollArea(self.widget_left_headers)
        self.scrollArea_headers_list.setAutoFillBackground(False)
        self.scrollArea_headers_list.setWidgetResizable(True)
        self.scrollArea_headers_list.setObjectName("scrollArea_headers_list")
        self.sAWContent_headers_list = QtWidgets.QWidget()
        self.sAWContent_headers_list.setGeometry(QtCore.QRect(0, 0, 544, 542))
        self.sAWContent_headers_list.setObjectName("sAWContent_headers_list")
        self.vL_sAWContent_headers_list = QtWidgets.QVBoxLayout(self.sAWContent_headers_list)
        self.vL_sAWContent_headers_list.setObjectName("vL_sAWContent_headers_list")
        self.scrollArea_headers_list.setWidget(self.sAWContent_headers_list)
        self.vL_widget_left_headers.addWidget(self.scrollArea_headers_list)
        self.hL_Headers.addWidget(self.widget_left_headers)
        self.hL_Headers.setStretch(0, 1)
        self.hL_Headers.setStretch(1, 2)

        self.retranslateUi(Headers)
        QtCore.QMetaObject.connectSlotsByName(Headers)

    def retranslateUi(self, Headers):
        _translate = QtCore.QCoreApplication.translate
        Headers.setWindowTitle(_translate("Headers", "Реестр руководителей"))
        self.pushButton_headers_add.setText(_translate("Headers", "Добавить новую запись"))
        self.pushButton_headers_save.setText(_translate("Headers", "Сохранить в выбранную запись"))
        self.label_headers_fullname.setText(_translate("Headers", "Фамилия Имя Отчество"))
        self.label_headers_prof.setText(_translate("Headers", "Должность"))
        self.label_headers_phone.setText(_translate("Headers", "Телефон (не обязательно)"))
        self.label_headers_mail.setText(_translate("Headers", "Электронная почта (не обязательно)"))
        self.label_headers_web.setText(_translate("Headers", "Ссылки на социальные сети (не обязательно)"))
        self.pushButton_headers_back.setText(_translate("Headers", "Назад"))
        self.label_search_headers.setText(_translate("Headers", "Поиск:"))
        self.pushButton_headers_delete.setText(_translate("Headers", "Удалить выбранную запись"))
