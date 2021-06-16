from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Outlay(object):
    def setupUi(self, Outlay):
        Outlay.setObjectName("Outlay")
        Outlay.resize(898, 569)
        self.vL_outlay = QtWidgets.QVBoxLayout(Outlay)
        self.vL_outlay.setObjectName("vL_outlay")

        self.variability_list = [["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]]
        self.calcs_before = 5
        self.tail = [["hours", "tax", "price"], ["hours", "tax", "price"], ["hours", "tax", "price"], ["hours", "tax", "price"]]

        self.widget_progs = QtWidgets.QWidget(Outlay)
        self.widget_progs.setObjectName("widget_progs")
        self.hL_widget_progs = QtWidgets.QHBoxLayout(self.widget_progs)
        self.hL_widget_progs.setObjectName("hL_widget_progs")
        self.vL_outlay.addWidget(self.widget_progs)

        self.label_progs = QtWidgets.QLabel(self.widget_progs)
        self.label_progs.setObjectName("label_progs")
        self.hL_widget_progs.addWidget(self.label_progs)

        self.comboBox_progs = QtWidgets.QComboBox(self.widget_progs)
        self.comboBox_progs.setEditable(False)
        self.comboBox_progs.setPlaceholderText("")
        self.comboBox_progs.setObjectName("comboBox_progs")
        self.hL_widget_progs.addWidget(self.comboBox_progs)

        self.widget_subs = QtWidgets.QWidget(Outlay)
        self.widget_subs.setObjectName("widget_subs")
        self.hL_widget_subs = QtWidgets.QHBoxLayout(self.widget_subs)
        self.hL_widget_subs.setObjectName("hL_widget_subs")
        self.vL_outlay.addWidget(self.widget_subs)

        self.label_subs = QtWidgets.QLabel(self.widget_subs)
        self.label_subs.setObjectName("label_subs")
        self.hL_widget_subs.addWidget(self.label_subs)
        
        self.widget_col_subs = QtWidgets.QWidget(self.widget_subs)
        self.widget_col_subs.setObjectName("widget_col_subs")
        self.hL_widget_col_subs = QtWidgets.QHBoxLayout(self.widget_col_subs)
        self.hL_widget_col_subs.setObjectName("hL_widget_col_subs")
        self.hL_widget_subs.addWidget(self.widget_col_subs)

        self.radio_col_1 = QtWidgets.QRadioButton(self.widget_col_subs)
        self.radio_col_1.setObjectName("radio_col_1")
        self.hL_widget_col_subs.addWidget(self.radio_col_1)
        self.radio_col_1.setChecked(True)

        self.radio_col_2 = QtWidgets.QRadioButton(self.widget_col_subs)
        self.radio_col_2.setObjectName("radio_col_2")
        self.hL_widget_col_subs.addWidget(self.radio_col_2)

        self.radio_col_3 = QtWidgets.QRadioButton(self.widget_col_subs)
        self.radio_col_3.setObjectName("radio_col_3")
        self.hL_widget_col_subs.addWidget(self.radio_col_3)

        self.radio_col_4 = QtWidgets.QRadioButton(self.widget_col_subs)
        self.radio_col_4.setObjectName("radio_col_4")
        self.hL_widget_col_subs.addWidget(self.radio_col_4)

        self.widget_calcs = QtWidgets.QWidget(Outlay)
        self.widget_calcs.setObjectName("widget_calcs")
        self.gL_widget_calcs = QtWidgets.QGridLayout(self.widget_calcs)
        self.gL_widget_calcs.setObjectName("gL_widget_calcs")
        self.vL_outlay.addWidget(self.widget_calcs)

        self.label_otfot = QtWidgets.QLabel(Outlay)
        self.label_otfot.setObjectName("label_otfot")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_otfot.setFont(font)
        self.vL_outlay.addWidget(self.label_otfot)

        self.label_profit = QtWidgets.QLabel(Outlay)
        self.label_profit.setObjectName("label_profit")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_profit.setFont(font)
        self.vL_outlay.addWidget(self.label_profit)

        self.label_cost = QtWidgets.QLabel(Outlay)
        self.label_cost.setObjectName("label_cost")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_cost.setFont(font)
        self.vL_outlay.addWidget(self.label_cost)

        self.widget_btns = QtWidgets.QWidget(Outlay)
        self.widget_btns.setObjectName("widget_btns")
        self.hL_widget_btns = QtWidgets.QHBoxLayout(self.widget_btns)
        self.hL_widget_btns.setObjectName("hL_widget_btns")
        self.hL_widget_btns.setContentsMargins(0, 0, 0, 0)
        self.vL_outlay.addWidget(self.widget_btns)

        self.pushButton_outlay_back = QtWidgets.QPushButton(self.widget_btns)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_outlay_back.setFont(font)
        self.pushButton_outlay_back.setObjectName("pushButton_outlay_back")
        self.hL_widget_btns.addWidget(self.pushButton_outlay_back)

        self.pushButton_outlay_next = QtWidgets.QPushButton(self.widget_btns)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_outlay_next.setFont(font)
        self.pushButton_outlay_next.setObjectName("pushButton_outlay_next")
        self.hL_widget_btns.addWidget(self.pushButton_outlay_next)

        self.retranslateUi(Outlay)
        QtCore.QMetaObject.connectSlotsByName(Outlay)

    def retranslateUi(self, Outlay):
        _translate = QtCore.QCoreApplication.translate
        Outlay.setWindowTitle(_translate("Outlay", "Калькулятор сметы"))
        self.label_progs.setText(_translate("Outlay", "Вы можете выбрать уже существующую программу: "))
        self.label_subs.setText(_translate("Outlay", "Выберите количество предметов: "))
        self.label_otfot.setText(_translate("Outlay", "ФОТ к затратам % = "))
        self.label_profit.setText(_translate("Outlay", "Доходы = "))
        self.label_cost.setText(_translate("Outlay", "ФОТ = "))
        self.pushButton_outlay_back.setText(_translate("Outlay", "Назад"))
        self.pushButton_outlay_next.setText(_translate("Outlay", "Далее"))
        self.radio_col_1.setText("1")
        self.radio_col_2.setText("2")
        self.radio_col_3.setText("3")
        self.radio_col_4.setText("4")
