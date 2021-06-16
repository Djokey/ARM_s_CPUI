from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NotePasswords(object):
    def setupUi(self, NotePasswords):
        NotePasswords.setObjectName("NotePasswords")
        NotePasswords.resize(800, 450)

        self.vL_main = QtWidgets.QVBoxLayout(NotePasswords)
        self.vL_main.setObjectName("vL_main")

        self.widget_prog = QtWidgets.QWidget(NotePasswords)
        self.widget_prog.setObjectName("widget_prog")

        self.hL_widget_prog = QtWidgets.QHBoxLayout(self.widget_prog)
        self.hL_widget_prog.setObjectName("hL_widget_prog")
        self.vL_main.addWidget(self.widget_prog)

        self.lab_prog = QtWidgets.QLabel(NotePasswords)
        self.lab_prog.setObjectName("lab_prog")
        self.hL_widget_prog.addWidget(self.lab_prog)

        self.comboBox_prog = QtWidgets.QComboBox(NotePasswords)
        self.comboBox_prog.setObjectName("comboBox_prog")
        self.hL_widget_prog.addWidget(self.comboBox_prog)

        self.lab_group = QtWidgets.QLabel(NotePasswords)
        self.lab_group.setObjectName("lab_group")
        self.hL_widget_prog.addWidget(self.lab_group)

        self.comboBox_group = QtWidgets.QComboBox(NotePasswords)
        self.comboBox_group.setObjectName("comboBox_group")
        self.hL_widget_prog.addWidget(self.comboBox_group)

        self.checkBox_all_group = QtWidgets.QCheckBox(NotePasswords)
        self.checkBox_all_group.setObjectName("checkBox_all_group")
        self.vL_main.addWidget(self.checkBox_all_group)

        self.scrollArea_outlay_studs = QtWidgets.QScrollArea(NotePasswords)
        self.scrollArea_outlay_studs.setWidgetResizable(True)
        self.scrollArea_outlay_studs.setObjectName("scrollArea_outlay_studs")
        self.sAWContent_outlay_studs = QtWidgets.QWidget()
        self.sAWContent_outlay_studs.setObjectName("sAWContent_outlay_studs")
        self.vL_sAWContent_outlay_studs = QtWidgets.QVBoxLayout(self.sAWContent_outlay_studs)
        self.vL_sAWContent_outlay_studs.setObjectName("vL_sAWContent_outlay_studs")
        self.scrollArea_outlay_studs.setWidget(self.sAWContent_outlay_studs)
        self.vL_main.addWidget(self.scrollArea_outlay_studs)

        self.widget_dates = QtWidgets.QWidget(NotePasswords)
        self.widget_dates.setObjectName("widget_dates")
        self.hL_widget_dates = QtWidgets.QHBoxLayout(self.widget_dates)
        self.hL_widget_dates.setObjectName("hL_widget_dates")
        self.vL_main.addWidget(self.widget_dates)

        self.lab_date_before = QtWidgets.QLabel(NotePasswords)
        self.lab_date_before.setObjectName("lab_date_before")
        self.hL_widget_dates.addWidget(self.lab_date_before)

        self.dateEdit_date_before = QtWidgets.QDateEdit(NotePasswords)
        self.dateEdit_date_before.setObjectName("dateEdit_date_before")
        self.hL_widget_dates.addWidget(self.dateEdit_date_before)

        self.widget_date = QtWidgets.QWidget(NotePasswords)
        self.widget_date.setObjectName("widget_date")
        self.hL_widget_date = QtWidgets.QHBoxLayout(self.widget_date)
        self.hL_widget_date.setObjectName("hL_widget_date")
        self.vL_main.addWidget(self.widget_date)

        self.lab_date = QtWidgets.QLabel(NotePasswords)
        self.lab_date.setObjectName("lab_date")
        self.hL_widget_date.addWidget(self.lab_date)

        self.dateEdit_date = QtWidgets.QDateEdit(NotePasswords)
        self.dateEdit_date.setObjectName("dateEdit_date")
        self.hL_widget_date.addWidget(self.dateEdit_date)

        self.widget_head = QtWidgets.QWidget(NotePasswords)
        self.widget_head.setObjectName("widget_head")
        self.hL_widget_head = QtWidgets.QHBoxLayout(self.widget_head)
        self.hL_widget_head.setObjectName("hL_widget_head")
        self.vL_main.addWidget(self.widget_head)

        self.lab_head = QtWidgets.QLabel(NotePasswords)
        self.lab_head.setObjectName("lab_head")
        self.hL_widget_head.addWidget(self.lab_head)

        self.comboBox_head = QtWidgets.QComboBox(NotePasswords)
        self.comboBox_head.setObjectName("comboBox_head")
        self.hL_widget_head.addWidget(self.comboBox_head)

        self.widget_manager = QtWidgets.QWidget(NotePasswords)
        self.widget_manager.setObjectName("widget_manager")
        self.hL_widget_manager = QtWidgets.QHBoxLayout(self.widget_manager)
        self.hL_widget_manager.setObjectName("hL_widget_manager")
        self.vL_main.addWidget(self.widget_manager)

        self.lab_manager_cpui = QtWidgets.QLabel(NotePasswords)
        self.lab_manager_cpui.setObjectName("lab_manager_cpui")
        self.hL_widget_manager.addWidget(self.lab_manager_cpui)

        self.comboBox_manager_cpui = QtWidgets.QComboBox(NotePasswords)
        self.comboBox_manager_cpui.setObjectName("comboBox_manager_cpui")
        self.hL_widget_manager.addWidget(self.comboBox_manager_cpui)

        self.pushButton_save_doc = QtWidgets.QPushButton(NotePasswords)
        self.pushButton_save_doc.setObjectName("pushButton_save_doc")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save_doc.setFont(font)
        self.vL_main.addWidget(self.pushButton_save_doc)

        self.pushButton_back = QtWidgets.QPushButton(NotePasswords)
        self.pushButton_back.setObjectName("pushButton_back")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.vL_main.addWidget(self.pushButton_back)

        self.retranslateUi(NotePasswords)
        QtCore.QMetaObject.connectSlotsByName(NotePasswords)

    def retranslateUi(self, NotePasswords):
        _translate = QtCore.QCoreApplication.translate
        NotePasswords.setWindowTitle(_translate("NotePasswords", "Редактор документа"))
        self.lab_head.setText(_translate("NotePasswords", "Руководитель департамента ИТ: "))
        self.pushButton_save_doc.setText(_translate("NotePasswords", "Сохранить служебку"))
        self.pushButton_back.setText(_translate("NotePasswords", "Назад"))
        self.lab_prog.setText(_translate("NotePasswords", "Программа: "))
        self.lab_group.setText(_translate("NotePasswords", "Группа: "))
        self.checkBox_all_group.setText(_translate("NotePasswords", "Выбрать всех из группы"))
        self.lab_date_before.setText(_translate("NotePasswords", "Доступ до: "))
        self.lab_date.setText(_translate("NotePasswords", "Дата создания записки: "))
        self.lab_manager_cpui.setText(_translate("NotePasswords", "Зав. ЦПЮИ: "))
