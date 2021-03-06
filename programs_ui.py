from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Programs(object):
    def setupUi(self, Programs):
        Programs.setObjectName("Programs")
        Programs.resize(933, 591)
        self.hL_Programs = QtWidgets.QHBoxLayout(Programs)
        self.hL_Programs.setObjectName("hL_Programs")
        self.widget_programs_input_box = QtWidgets.QWidget(Programs)
        self.widget_programs_input_box.setObjectName("widget_programs_input_box")
        self.vL_widget_programs_input_box = QtWidgets.QVBoxLayout(self.widget_programs_input_box)
        self.vL_widget_programs_input_box.setObjectName("vL_widget_programs_input_box")

        self.widget_programs_edit_buts = QtWidgets.QWidget(self.widget_programs_input_box)
        self.widget_programs_edit_buts.setObjectName("widget_programs_edit_buts")
        self.hL_widget_programs_edit_buts = QtWidgets.QHBoxLayout(self.widget_programs_edit_buts)
        self.hL_widget_programs_edit_buts.setObjectName("hL_widget_programs_edit_buts")

        self.pushButton_programs_add = QtWidgets.QPushButton(self.widget_programs_edit_buts)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_programs_add.setFont(font)
        self.pushButton_programs_add.setObjectName("pushButton_programs_add")
        self.hL_widget_programs_edit_buts.addWidget(self.pushButton_programs_add)

        self.pushButton_programs_save = QtWidgets.QPushButton(self.widget_programs_edit_buts)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_programs_save.setFont(font)
        self.pushButton_programs_save.setObjectName("pushButton_programs_save")
        self.hL_widget_programs_edit_buts.addWidget(self.pushButton_programs_save)
        self.vL_widget_programs_input_box.addWidget(self.widget_programs_edit_buts)

        self.label_prog_name = QtWidgets.QLabel(self.widget_programs_input_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_prog_name.setFont(font)
        self.label_prog_name.setObjectName("label_prog_name")
        self.vL_widget_programs_input_box.addWidget(self.label_prog_name)

        self.textEdit_prog_name = QtWidgets.QTextEdit(self.widget_programs_input_box)
        self.textEdit_prog_name.setObjectName("textEdit_prog_name")
        self.vL_widget_programs_input_box.addWidget(self.textEdit_prog_name)

        self.label_prog_range = QtWidgets.QLabel(self.widget_programs_input_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_prog_range.setFont(font)
        self.label_prog_range.setObjectName("label_prog_range")
        self.vL_widget_programs_input_box.addWidget(self.label_prog_range)

        self.textEdit_prog_range = QtWidgets.QTextEdit(self.widget_programs_input_box)
        self.textEdit_prog_range.setObjectName("textEdit_prog_range")
        self.vL_widget_programs_input_box.addWidget(self.textEdit_prog_range)

        self.label_start_program = QtWidgets.QLabel(self.widget_programs_input_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_start_program.setFont(font)
        self.label_start_program.setObjectName("label_start_program")
        self.vL_widget_programs_input_box.addWidget(self.label_start_program)

        self.dateEdit_start_program = QtWidgets.QDateEdit(self.widget_programs_input_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_start_program.setFont(font)
        self.dateEdit_start_program.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit_start_program.setObjectName("dateEdit_start_program")
        self.vL_widget_programs_input_box.addWidget(self.dateEdit_start_program)

        self.label_end_program = QtWidgets.QLabel(self.widget_programs_input_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_end_program.setFont(font)
        self.label_end_program.setObjectName("label_end_program")
        self.vL_widget_programs_input_box.addWidget(self.label_end_program)

        self.dateEdit_end_program = QtWidgets.QDateEdit(self.widget_programs_input_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_end_program.setFont(font)
        self.dateEdit_end_program.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit_end_program.setObjectName("dateEdit_end_program")
        self.vL_widget_programs_input_box.addWidget(self.dateEdit_end_program)

        self.pushButton_programs_back = QtWidgets.QPushButton(self.widget_programs_input_box)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_programs_back.setFont(font)
        self.pushButton_programs_back.setObjectName("pushButton_programs_back")
        self.vL_widget_programs_input_box.addWidget(self.pushButton_programs_back)
        self.hL_Programs.addWidget(self.widget_programs_input_box)

        self.widget_programs_list_box = QtWidgets.QWidget(Programs)
        self.widget_programs_list_box.setObjectName("widget_programs_list_box")

        self.vL_widget_programs_list_box = QtWidgets.QVBoxLayout(self.widget_programs_list_box)
        self.vL_widget_programs_list_box.setObjectName("vL_widget_programs_list_box")

        self.widget_left_up_programs = QtWidgets.QWidget(self.widget_programs_list_box)
        self.widget_left_up_programs.setObjectName("widget_left_up_programs")

        self.hL_widget_left_up_programs = QtWidgets.QHBoxLayout(self.widget_left_up_programs)
        self.hL_widget_left_up_programs.setObjectName("hL_widget_left_up_programs")

        self.label_search_programs = QtWidgets.QLabel(self.widget_left_up_programs)
        self.label_search_programs.setObjectName("label_search_programs")
        self.hL_widget_left_up_programs.addWidget(self.label_search_programs)

        self.lineEdit_search_programs = QtWidgets.QLineEdit(self.widget_left_up_programs)
        self.lineEdit_search_programs.setObjectName("lineEdit_search_programs")
        self.hL_widget_left_up_programs.addWidget(self.lineEdit_search_programs)

        self.pushButton_programs_delete = QtWidgets.QPushButton(self.widget_left_up_programs)
        self.pushButton_programs_delete.setObjectName("pushButton_programs_delete")
        self.hL_widget_left_up_programs.addWidget(self.pushButton_programs_delete)

        self.vL_widget_programs_list_box.addWidget(self.widget_left_up_programs)

        self.scrollArea_programs_list = QtWidgets.QScrollArea(self.widget_programs_list_box)
        self.scrollArea_programs_list.setAutoFillBackground(False)
        self.scrollArea_programs_list.setWidgetResizable(True)
        self.scrollArea_programs_list.setObjectName("scrollArea_programs_list")

        self.sAWContent_programs_list = QtWidgets.QWidget()
        self.sAWContent_programs_list.setGeometry(QtCore.QRect(0, 0, 501, 506))
        self.sAWContent_programs_list.setObjectName("sAWContent_programs_list")
        self.vL_sAWContent_programs_list = QtWidgets.QVBoxLayout(self.sAWContent_programs_list)
        self.vL_sAWContent_programs_list.setObjectName("vL_sAWContent_programs_list")
        self.scrollArea_programs_list.setWidget(self.sAWContent_programs_list)
        self.vL_widget_programs_list_box.addWidget(self.scrollArea_programs_list)

        self.hL_Programs.addWidget(self.widget_programs_list_box)

        self.hL_Programs.setStretch(0, 1)
        self.hL_Programs.setStretch(1, 2)

        self.retranslateUi(Programs)
        QtCore.QMetaObject.connectSlotsByName(Programs)

    def retranslateUi(self, Programs):
        _translate = QtCore.QCoreApplication.translate
        Programs.setWindowTitle(_translate("Programs", "?????????????????????????????? ??????????????????"))
        self.pushButton_programs_add.setText(_translate("Programs", "???????????????? ?????????? ????????????"))
        self.pushButton_programs_save.setText(_translate("Programs", "?????????????????? ?????????????????? ????????????"))
        self.label_prog_name.setText(_translate("Programs", "???????????????????????? ?????????????????????????????? ??????????????????"))
        self.label_prog_range.setText(_translate("Programs", "?????????????????????????????????? ??????????????\n"
"(????????????????: 4 ?????? 8)"))
        self.label_start_program.setText(_translate("Programs", "???????? ???????????? ?????????????????? (????????, ??????????, ??????)"))
        self.label_end_program.setText(_translate("Programs", "???????? ?????????????????? ?????????????????? (????????, ??????????, ??????)"))
        self.pushButton_programs_back.setText(_translate("Programs", "??????????"))
        self.label_search_programs.setText(_translate("Programs", "??????????:"))
        self.pushButton_programs_delete.setText(_translate("Programs", "?????????????? ?????????????????? ????????????"))
