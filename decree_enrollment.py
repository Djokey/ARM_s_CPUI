from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DecreeEnrollment(object):
    def setupUi(self, DecreeEnrollment):
        DecreeEnrollment.setObjectName("DecreeEnrollment")
        DecreeEnrollment.resize(800, 450)
        
        self.vL_main = QtWidgets.QVBoxLayout(DecreeEnrollment)
        self.vL_main.setObjectName("vL_main")

        self.widget_prog = QtWidgets.QWidget(DecreeEnrollment)
        self.widget_prog.setObjectName("widget_prog")

        self.hL_widget_prog = QtWidgets.QHBoxLayout(self.widget_prog)
        self.hL_widget_prog.setObjectName("hL_widget_prog")
        self.vL_main.addWidget(self.widget_prog)

        self.lab_prog = QtWidgets.QLabel(DecreeEnrollment)
        self.lab_prog.setObjectName("lab_prog")
        self.hL_widget_prog.addWidget(self.lab_prog)

        self.comboBox_prog = QtWidgets.QComboBox(DecreeEnrollment)
        self.comboBox_prog.setObjectName("comboBox_prog")
        self.hL_widget_prog.addWidget(self.comboBox_prog)

        self.lab_group = QtWidgets.QLabel(DecreeEnrollment)
        self.lab_group.setObjectName("lab_group")
        self.hL_widget_prog.addWidget(self.lab_group)

        self.comboBox_group = QtWidgets.QComboBox(DecreeEnrollment)
        self.comboBox_group.setObjectName("comboBox_group")
        self.hL_widget_prog.addWidget(self.comboBox_group)

        self.checkBox_all_group = QtWidgets.QCheckBox(DecreeEnrollment)
        self.checkBox_all_group.setObjectName("checkBox_all_group")
        self.vL_main.addWidget(self.checkBox_all_group)

        self.scrollArea_outlay_studs = QtWidgets.QScrollArea(DecreeEnrollment)
        self.scrollArea_outlay_studs.setWidgetResizable(True)
        self.scrollArea_outlay_studs.setObjectName("scrollArea_outlay_studs")
        self.sAWContent_outlay_studs = QtWidgets.QWidget()
        self.sAWContent_outlay_studs.setObjectName("sAWContent_outlay_studs")
        self.vL_sAWContent_outlay_studs = QtWidgets.QVBoxLayout(self.sAWContent_outlay_studs)
        self.vL_sAWContent_outlay_studs.setObjectName("vL_sAWContent_outlay_studs")
        self.scrollArea_outlay_studs.setWidget(self.sAWContent_outlay_studs)
        self.vL_main.addWidget(self.scrollArea_outlay_studs)

        self.widget_dates = QtWidgets.QWidget(DecreeEnrollment)
        self.widget_dates.setObjectName("widget_dates")
        self.hL_widget_dates = QtWidgets.QHBoxLayout(self.widget_dates)
        self.hL_widget_dates.setObjectName("hL_widget_dates")
        self.vL_main.addWidget(self.widget_dates)

        self.lab_date_start = QtWidgets.QLabel(DecreeEnrollment)
        self.lab_date_start.setObjectName("lab_date_start")
        self.hL_widget_dates.addWidget(self.lab_date_start)

        self.dateEdit_date_start = QtWidgets.QDateEdit(DecreeEnrollment)
        self.dateEdit_date_start.setObjectName("dateEdit_date_start")
        self.hL_widget_dates.addWidget(self.dateEdit_date_start)

        self.lab_date_end = QtWidgets.QLabel(DecreeEnrollment)
        self.lab_date_end.setObjectName("lab_date_end")
        self.hL_widget_dates.addWidget(self.lab_date_end)

        self.dateEdit_date_end = QtWidgets.QDateEdit(DecreeEnrollment)
        self.dateEdit_date_end.setObjectName("dateEdit_date_end")
        self.hL_widget_dates.addWidget(self.dateEdit_date_end)

        self.widget_head = QtWidgets.QWidget(DecreeEnrollment)
        self.widget_head.setObjectName("widget_head")
        self.hL_widget_head = QtWidgets.QHBoxLayout(self.widget_head)
        self.hL_widget_head.setObjectName("hL_widget_head")
        self.vL_main.addWidget(self.widget_head)

        self.lab_head = QtWidgets.QLabel(DecreeEnrollment)
        self.lab_head.setObjectName("lab_head")
        self.hL_widget_head.addWidget(self.lab_head)

        self.comboBox_head = QtWidgets.QComboBox(DecreeEnrollment)
        self.comboBox_head.setObjectName("comboBox_head")
        self.hL_widget_head.addWidget(self.comboBox_head)

        self.widget_manager = QtWidgets.QWidget(DecreeEnrollment)
        self.widget_manager.setObjectName("widget_manager")
        self.hL_widget_manager = QtWidgets.QHBoxLayout(self.widget_manager)
        self.hL_widget_manager.setObjectName("hL_widget_manager")
        self.vL_main.addWidget(self.widget_manager)

        self.lab_manager_cpui = QtWidgets.QLabel(DecreeEnrollment)
        self.lab_manager_cpui.setObjectName("lab_manager_cpui")
        self.hL_widget_manager.addWidget(self.lab_manager_cpui)

        self.comboBox_manager_cpui = QtWidgets.QComboBox(DecreeEnrollment)
        self.comboBox_manager_cpui.setObjectName("comboBox_manager_cpui")
        self.hL_widget_manager.addWidget(self.comboBox_manager_cpui)

        self.widget_pfs = QtWidgets.QWidget(DecreeEnrollment)
        self.widget_pfs.setObjectName("widget_pfs")
        self.hL_widget_pfs = QtWidgets.QHBoxLayout(self.widget_pfs)
        self.hL_widget_pfs.setObjectName("hL_widget_pfs")
        self.vL_main.addWidget(self.widget_pfs)

        self.lab_pfs = QtWidgets.QLabel(DecreeEnrollment)
        self.lab_pfs.setObjectName("lab_pfs")
        self.hL_widget_pfs.addWidget(self.lab_pfs)

        self.comboBox_pfs = QtWidgets.QComboBox(DecreeEnrollment)
        self.comboBox_pfs.setObjectName("comboBox_pfs")
        self.hL_widget_pfs.addWidget(self.comboBox_pfs)

        self.widget_office = QtWidgets.QWidget(DecreeEnrollment)
        self.widget_office.setObjectName("widget_office")
        self.hL_widget_office = QtWidgets.QHBoxLayout(self.widget_office)
        self.hL_widget_office.setObjectName("hL_widget_office")
        self.vL_main.addWidget(self.widget_office)

        self.lab_office = QtWidgets.QLabel(DecreeEnrollment)
        self.lab_office.setObjectName("lab_office")
        self.hL_widget_office.addWidget(self.lab_office)

        self.comboBox_office = QtWidgets.QComboBox(DecreeEnrollment)
        self.comboBox_office.setObjectName("comboBox_office")
        self.hL_widget_office.addWidget(self.comboBox_office)

        self.pushButton_save_doc = QtWidgets.QPushButton(DecreeEnrollment)
        self.pushButton_save_doc.setObjectName("pushButton_save_doc")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save_doc.setFont(font)
        self.vL_main.addWidget(self.pushButton_save_doc)

        self.pushButton_back = QtWidgets.QPushButton(DecreeEnrollment)
        self.pushButton_back.setObjectName("pushButton_back")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.vL_main.addWidget(self.pushButton_back)

        self.retranslateUi(DecreeEnrollment)
        QtCore.QMetaObject.connectSlotsByName(DecreeEnrollment)

    def retranslateUi(self, DecreeEnrollment):
        _translate = QtCore.QCoreApplication.translate
        DecreeEnrollment.setWindowTitle(_translate("DecreeEnrollment", "Редактор приказа"))
        self.lab_head.setText(_translate("DecreeEnrollment", "Директор: "))
        self.pushButton_save_doc.setText(_translate("DecreeEnrollment", "Сохранить приказ"))
        self.pushButton_back.setText(_translate("DecreeEnrollment", "Назад"))
        self.lab_prog.setText(_translate("DecreeEnrollment", "Программа: "))
        self.lab_group.setText(_translate("DecreeEnrollment", "Группа: "))
        self.checkBox_all_group.setText(_translate("DecreeEnrollment", "Выбрать всех из группы"))
        self.lab_date_start.setText(_translate("DecreeEnrollment", "Даты проведения с: "))
        self.lab_date_end.setText(_translate("DecreeEnrollment", "        по: "))
        self.lab_manager_cpui.setText(_translate("DecreeEnrollment", "Зав. ЦПЮИ: "))
        self.lab_pfs.setText(_translate("DecreeEnrollment", "Зав. ПФС: "))
        self.lab_office.setText(_translate("DecreeEnrollment", "Зав. канцелярией: "))
