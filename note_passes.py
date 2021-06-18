from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NotePasses(object):
    def setupUi(self, NotePasses):
        NotePasses.setObjectName("NotePasses")
        NotePasses.resize(800, 450)

        self.vL_main = QtWidgets.QVBoxLayout(NotePasses)
        self.vL_main.setObjectName("vL_main")

        self.widget_prog = QtWidgets.QWidget(NotePasses)
        self.widget_prog.setObjectName("widget_prog")

        self.hL_widget_prog = QtWidgets.QHBoxLayout(self.widget_prog)
        self.hL_widget_prog.setObjectName("hL_widget_prog")
        self.vL_main.addWidget(self.widget_prog)

        self.lab_prog = QtWidgets.QLabel(NotePasses)
        self.lab_prog.setObjectName("lab_prog")
        self.hL_widget_prog.addWidget(self.lab_prog)

        self.comboBox_prog = QtWidgets.QComboBox(NotePasses)
        self.comboBox_prog.setObjectName("comboBox_prog")
        self.hL_widget_prog.addWidget(self.comboBox_prog)

        self.lab_group = QtWidgets.QLabel(NotePasses)
        self.lab_group.setObjectName("lab_group")
        self.hL_widget_prog.addWidget(self.lab_group)

        self.comboBox_group = QtWidgets.QComboBox(NotePasses)
        self.comboBox_group.setObjectName("comboBox_group")
        self.hL_widget_prog.addWidget(self.comboBox_group)

        self.checkBox_all_group = QtWidgets.QCheckBox(NotePasses)
        self.checkBox_all_group.setObjectName("checkBox_all_group")
        self.vL_main.addWidget(self.checkBox_all_group)

        self.scrollArea_outlay_studs = QtWidgets.QScrollArea(NotePasses)
        self.scrollArea_outlay_studs.setWidgetResizable(True)
        self.scrollArea_outlay_studs.setObjectName("scrollArea_outlay_studs")
        self.sAWContent_outlay_studs = QtWidgets.QWidget()
        self.sAWContent_outlay_studs.setObjectName("sAWContent_outlay_studs")
        self.vL_sAWContent_outlay_studs = QtWidgets.QVBoxLayout(self.sAWContent_outlay_studs)
        self.vL_sAWContent_outlay_studs.setObjectName("vL_sAWContent_outlay_studs")
        self.scrollArea_outlay_studs.setWidget(self.sAWContent_outlay_studs)
        self.vL_main.addWidget(self.scrollArea_outlay_studs)

        self.widget_dates = QtWidgets.QWidget(NotePasses)
        self.widget_dates.setObjectName("widget_dates")
        self.hL_widget_dates = QtWidgets.QHBoxLayout(self.widget_dates)
        self.hL_widget_dates.setObjectName("hL_widget_dates")
        self.vL_main.addWidget(self.widget_dates)

        self.lab_date_start = QtWidgets.QLabel(NotePasses)
        self.lab_date_start.setObjectName("lab_date_start")
        self.hL_widget_dates.addWidget(self.lab_date_start)

        self.dateEdit_date_start = QtWidgets.QDateEdit(NotePasses)
        self.dateEdit_date_start.setObjectName("dateEdit_date_start")
        self.hL_widget_dates.addWidget(self.dateEdit_date_start)

        self.lab_date_end = QtWidgets.QLabel(NotePasses)
        self.lab_date_end.setObjectName("lab_date_end")
        self.hL_widget_dates.addWidget(self.lab_date_end)

        self.dateEdit_date_end = QtWidgets.QDateEdit(NotePasses)
        self.dateEdit_date_end.setObjectName("dateEdit_date_end")
        self.hL_widget_dates.addWidget(self.dateEdit_date_end)

        self.widget_date = QtWidgets.QWidget(NotePasses)
        self.widget_date.setObjectName("widget_date")
        self.hL_widget_date = QtWidgets.QHBoxLayout(self.widget_date)
        self.hL_widget_date.setObjectName("hL_widget_date")
        self.vL_main.addWidget(self.widget_date)

        self.lab_date = QtWidgets.QLabel(NotePasses)
        self.lab_date.setObjectName("lab_date")
        self.hL_widget_date.addWidget(self.lab_date)

        self.dateEdit_date = QtWidgets.QDateEdit(NotePasses)
        self.dateEdit_date.setObjectName("dateEdit_date")
        self.hL_widget_date.addWidget(self.dateEdit_date)

        self.widget_head = QtWidgets.QWidget(NotePasses)
        self.widget_head.setObjectName("widget_head")
        self.hL_widget_head = QtWidgets.QHBoxLayout(self.widget_head)
        self.hL_widget_head.setObjectName("hL_widget_head")
        self.vL_main.addWidget(self.widget_head)

        self.lab_head = QtWidgets.QLabel(NotePasses)
        self.lab_head.setObjectName("lab_head")
        self.hL_widget_head.addWidget(self.lab_head)

        self.comboBox_head = QtWidgets.QComboBox(NotePasses)
        self.comboBox_head.setObjectName("comboBox_head")
        self.hL_widget_head.addWidget(self.comboBox_head)

        self.widget_manager = QtWidgets.QWidget(NotePasses)
        self.widget_manager.setObjectName("widget_manager")
        self.hL_widget_manager = QtWidgets.QHBoxLayout(self.widget_manager)
        self.hL_widget_manager.setObjectName("hL_widget_manager")
        self.vL_main.addWidget(self.widget_manager)

        self.lab_manager_cpui = QtWidgets.QLabel(NotePasses)
        self.lab_manager_cpui.setObjectName("lab_manager_cpui")
        self.hL_widget_manager.addWidget(self.lab_manager_cpui)

        self.comboBox_manager_cpui = QtWidgets.QComboBox(NotePasses)
        self.comboBox_manager_cpui.setObjectName("comboBox_manager_cpui")
        self.hL_widget_manager.addWidget(self.comboBox_manager_cpui)

        self.pushButton_save_doc = QtWidgets.QPushButton(NotePasses)
        self.pushButton_save_doc.setObjectName("pushButton_save_doc")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save_doc.setFont(font)
        self.vL_main.addWidget(self.pushButton_save_doc)

        self.pushButton_back = QtWidgets.QPushButton(NotePasses)
        self.pushButton_back.setObjectName("pushButton_back")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.vL_main.addWidget(self.pushButton_back)

        self.retranslateUi(NotePasses)
        QtCore.QMetaObject.connectSlotsByName(NotePasses)

    def retranslateUi(self, NotePasses):
        _translate = QtCore.QCoreApplication.translate
        NotePasses.setWindowTitle(_translate("NotePasses", "Редактор документа"))
        self.lab_head.setText(_translate("NotePasses", "Директор: "))
        self.pushButton_save_doc.setText(_translate("NotePasses", "Сохранить служебную записку"))
        self.pushButton_back.setText(_translate("NotePasses", "Назад"))
        self.lab_prog.setText(_translate("NotePasses", "Программа: "))
        self.lab_group.setText(_translate("NotePasses", "Группа: "))
        self.checkBox_all_group.setText(_translate("NotePasses", "Выбрать всех из группы"))
        self.lab_date_start.setText(_translate("NotePasses", "Даты проведения с: "))
        self.lab_date.setText(_translate("NotePasses", "Дата создания записки: "))
        self.lab_date_end.setText(_translate("NotePasses", "        по: "))
        self.lab_manager_cpui.setText(_translate("NotePasses", "Зав. ЦПЮИ: "))
