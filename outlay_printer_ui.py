from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OutlayPrinter(object):
    def setupUi(self, OutlayPrinter):
        OutlayPrinter.setObjectName("OutlayPrinter")
        OutlayPrinter.resize(800, 450)
        self.vL_main = QtWidgets.QVBoxLayout(OutlayPrinter)
        self.vL_main.setObjectName("vL_main")

        self.widget_head = QtWidgets.QWidget(OutlayPrinter)
        self.widget_head.setObjectName("widget_head")
        self.hL_widget_head = QtWidgets.QHBoxLayout(self.widget_head)
        self.hL_widget_head.setObjectName("hL_widget_head")
        self.vL_main.addWidget(self.widget_head)

        self.lab_head = QtWidgets.QLabel(OutlayPrinter)
        self.lab_head.setObjectName("lab_head")
        self.hL_widget_head.addWidget(self.lab_head)

        self.comboBox_head = QtWidgets.QComboBox(OutlayPrinter)
        self.comboBox_head.setObjectName("comboBox_head")
        self.hL_widget_head.addWidget(self.comboBox_head)

        self.widget_confirm = QtWidgets.QWidget(OutlayPrinter)
        self.widget_confirm.setObjectName("widget_confirm")
        self.hL_widget_confirm = QtWidgets.QHBoxLayout(self.widget_confirm)
        self.hL_widget_confirm.setObjectName("hL_widget_confirm")
        self.vL_main.addWidget(self.widget_confirm)

        self.lab_date_confirm = QtWidgets.QLabel(OutlayPrinter)
        self.lab_date_confirm.setObjectName("lab_date_confirm")
        self.hL_widget_confirm.addWidget(self.lab_date_confirm)

        self.dateEdit_date_confirm = QtWidgets.QDateEdit(OutlayPrinter)
        self.dateEdit_date_confirm.setObjectName("dateEdit_date_confirm")
        self.hL_widget_confirm.addWidget(self.dateEdit_date_confirm)

        self.widget_prog = QtWidgets.QWidget(OutlayPrinter)
        self.widget_prog.setObjectName("widget_prog")
        self.hL_widget_prog = QtWidgets.QHBoxLayout(self.widget_prog)
        self.hL_widget_prog.setObjectName("hL_widget_prog")
        self.vL_main.addWidget(self.widget_prog)

        self.lab_prog = QtWidgets.QLabel(OutlayPrinter)
        self.lab_prog.setObjectName("lab_prog")
        self.hL_widget_prog.addWidget(self.lab_prog)

        self.comboBox_prog = QtWidgets.QComboBox(OutlayPrinter)
        self.comboBox_prog.setObjectName("comboBox_prog")
        self.hL_widget_prog.addWidget(self.comboBox_prog)

        self.lab_class = QtWidgets.QLabel(OutlayPrinter)
        self.lab_class.setObjectName("lab_class")
        self.hL_widget_prog.addWidget(self.lab_class)

        self.lEdit_class = QtWidgets.QLineEdit(OutlayPrinter)
        self.lEdit_class.setObjectName("lEdit_class")
        self.hL_widget_prog.addWidget(self.lEdit_class)

        self.widget_dates = QtWidgets.QWidget(OutlayPrinter)
        self.widget_dates.setObjectName("widget_dates")
        self.hL_widget_dates = QtWidgets.QHBoxLayout(self.widget_dates)
        self.hL_widget_dates.setObjectName("hL_widget_dates")
        self.vL_main.addWidget(self.widget_dates)

        self.lab_date_start = QtWidgets.QLabel(OutlayPrinter)
        self.lab_date_start.setObjectName("lab_date_start")
        self.hL_widget_dates.addWidget(self.lab_date_start)

        self.dateEdit_date_start = QtWidgets.QDateEdit(OutlayPrinter)
        self.dateEdit_date_start.setObjectName("dateEdit_date_start")
        self.hL_widget_dates.addWidget(self.dateEdit_date_start)

        self.lab_date_end = QtWidgets.QLabel(OutlayPrinter)
        self.lab_date_end.setObjectName("lab_date_end")
        self.hL_widget_dates.addWidget(self.lab_date_end)

        self.dateEdit_date_end = QtWidgets.QDateEdit(OutlayPrinter)
        self.dateEdit_date_end.setObjectName("dateEdit_date_end")
        self.hL_widget_dates.addWidget(self.dateEdit_date_end)

        self.widget_manager = QtWidgets.QWidget(OutlayPrinter)
        self.widget_manager.setObjectName("widget_manager")
        self.hL_widget_manager = QtWidgets.QHBoxLayout(self.widget_manager)
        self.hL_widget_manager.setObjectName("hL_widget_manager")
        self.vL_main.addWidget(self.widget_manager)

        self.lab_manager_cpui = QtWidgets.QLabel(OutlayPrinter)
        self.lab_manager_cpui.setObjectName("lab_manager_cpui")
        self.hL_widget_manager.addWidget(self.lab_manager_cpui)

        self.comboBox_manager_cpui = QtWidgets.QComboBox(OutlayPrinter)
        self.comboBox_manager_cpui.setObjectName("comboBox_manager_cpui")
        self.hL_widget_manager.addWidget(self.comboBox_manager_cpui)

        self.widget_bookkeeper = QtWidgets.QWidget(OutlayPrinter)
        self.widget_bookkeeper.setObjectName("widget_bookkeeper")
        self.hL_widget_bookkeeper = QtWidgets.QHBoxLayout(self.widget_bookkeeper)
        self.hL_widget_bookkeeper.setObjectName("hL_widget_bookkeeper")
        self.vL_main.addWidget(self.widget_bookkeeper)

        self.lab_bookkeeper = QtWidgets.QLabel(OutlayPrinter)
        self.lab_bookkeeper.setObjectName("lab_bookkeeper")
        self.hL_widget_bookkeeper.addWidget(self.lab_bookkeeper)

        self.comboBox_bookkeeper = QtWidgets.QComboBox(OutlayPrinter)
        self.comboBox_bookkeeper.setObjectName("comboBox_bookkeeper")
        self.hL_widget_bookkeeper.addWidget(self.comboBox_bookkeeper)

        self.widget_pfs = QtWidgets.QWidget(OutlayPrinter)
        self.widget_pfs.setObjectName("widget_pfs")
        self.hL_widget_pfs = QtWidgets.QHBoxLayout(self.widget_pfs)
        self.hL_widget_pfs.setObjectName("hL_widget_pfs")
        self.vL_main.addWidget(self.widget_pfs)

        self.lab_pfs = QtWidgets.QLabel(OutlayPrinter)
        self.lab_pfs.setObjectName("lab_pfs")
        self.hL_widget_pfs.addWidget(self.lab_pfs)

        self.comboBox_pfs = QtWidgets.QComboBox(OutlayPrinter)
        self.comboBox_pfs.setObjectName("comboBox_pfs")
        self.hL_widget_pfs.addWidget(self.comboBox_pfs)

        self.widget_subs_teachs = QtWidgets.QWidget(OutlayPrinter)
        self.widget_subs_teachs.setObjectName("widget_subs_teachs")
        self.gL_widget_subs_teachs = QtWidgets.QGridLayout(self.widget_subs_teachs)
        self.gL_widget_subs_teachs.setObjectName("gL_widget_subs_teachs")
        self.vL_main.addWidget(self.widget_subs_teachs)

        self.widget_sub_teach_1 = QtWidgets.QWidget(self.widget_subs_teachs)
        self.widget_sub_teach_1.setObjectName("widget_sub_teach")
        self.gL_widget_sub_teach_1 = QtWidgets.QGridLayout(self.widget_sub_teach_1)
        self.gL_widget_sub_teach_1.setObjectName("gL_widget_sub_teach")
        self.gL_widget_subs_teachs.addWidget(self.widget_sub_teach_1, 0, 0)

        self.lab_sub_name_1 = QtWidgets.QLabel(self.widget_sub_teach_1)
        self.lab_sub_name_1.setObjectName("lab_sub_name_1")
        self.gL_widget_sub_teach_1.addWidget(self.lab_sub_name_1, 0, 0)

        self.lEdit_sub_name_1 = QtWidgets.QLineEdit(self.widget_sub_teach_1)
        self.lEdit_sub_name_1.setObjectName("lEdit_sub_name_1")
        self.gL_widget_sub_teach_1.addWidget(self.lEdit_sub_name_1, 0, 1)

        self.lab_teach_name_1 = QtWidgets.QLabel(self.widget_sub_teach_1)
        self.lab_teach_name_1.setObjectName("lab_teach_name_1")
        self.gL_widget_sub_teach_1.addWidget(self.lab_teach_name_1, 1, 0)

        self.lEdit_teach_name_1 = QtWidgets.QLineEdit(self.widget_sub_teach_1)
        self.lEdit_teach_name_1.setObjectName("lEdit_teach_name_1")
        self.gL_widget_sub_teach_1.addWidget(self.lEdit_teach_name_1, 1, 1)

        self.pushButton_save_doc = QtWidgets.QPushButton(OutlayPrinter)
        self.pushButton_save_doc.setObjectName("pushButton_save_doc")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save_doc.setFont(font)
        self.vL_main.addWidget(self.pushButton_save_doc)

        self.retranslateUi(OutlayPrinter)
        QtCore.QMetaObject.connectSlotsByName(OutlayPrinter)

    def retranslateUi(self, OutlayPrinter):
        _translate = QtCore.QCoreApplication.translate
        OutlayPrinter.setWindowTitle(_translate("OutlayPrinter", "Редактор сметы"))
        self.lab_head.setText(_translate("OutlayPrinter", "Директор: "))
        self.pushButton_save_doc.setText(_translate("OutlayPrinter", "Сохранить смету"))
        self.lab_date_confirm.setText(_translate("OutlayPrinter", "Дата утверждения: "))
        self.lab_prog.setText(_translate("OutlayPrinter", "Курсы: "))
        self.lab_class.setText(_translate("OutlayPrinter", "        Класс: "))
        self.lab_date_start.setText(_translate("OutlayPrinter", "Даты проведения с: "))
        self.lab_date_end.setText(_translate("OutlayPrinter", "        по: "))
        self.lab_manager_cpui.setText(_translate("OutlayPrinter", "Зав. ЦПЮИ: "))
        self.lab_bookkeeper.setText(_translate("OutlayPrinter", "Гл. бухгалтер: "))
        self.lab_pfs.setText(_translate("OutlayPrinter", "Зав. ПФС: "))
        self.lab_sub_name_1.setText(_translate("OutlayPrinter", "Название предмета 1: "))
        self.lab_teach_name_1.setText(_translate("OutlayPrinter", "ФИО преподавателя 1: "))
