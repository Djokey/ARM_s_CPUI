from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TTableEditor(object):
    def setupUi(self, TTableEditor):
        TTableEditor.setObjectName("TTableEditor")
        TTableEditor.resize(800, 450)
        self.vL_main = QtWidgets.QVBoxLayout(TTableEditor)
        self.vL_main.setObjectName("vL_main")

        self.widget_hours_set = QtWidgets.QWidget(TTableEditor)
        self.hL_widget_hours_Set = QtWidgets.QHBoxLayout(self.widget_hours_set)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_hours_set.sizePolicy().hasHeightForWidth())
        self.widget_hours_set.setSizePolicy(sizePolicy)
        self.vL_main.addWidget(self.widget_hours_set)

        self.lab_hours = QtWidgets.QLabel(self.widget_hours_set)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_hours.setFont(font)
        self.hL_widget_hours_Set.addWidget(self.lab_hours)

        self.lEdit_hours = QtWidgets.QSpinBox(self.widget_hours_set)
        self.lEdit_hours.setValue(2)
        self.hL_widget_hours_Set.addWidget(self.lEdit_hours)

        self.widget_btns = QtWidgets.QWidget(TTableEditor)
        self.hL_widget_btns = QtWidgets.QHBoxLayout(self.widget_btns)
        self.vL_main.addWidget(self.widget_btns)

        self.btn_set_hours = QtWidgets.QPushButton(self.widget_btns)
        self.hL_widget_btns.addWidget(self.btn_set_hours)

        self.btn_del_hours = QtWidgets.QPushButton(self.widget_btns)
        self.hL_widget_btns.addWidget(self.btn_del_hours)

        self.widget_hours_list = QtWidgets.QWidget(TTableEditor)
        self.hL_widget_hours_list = QtWidgets.QHBoxLayout(self.widget_hours_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_hours_list.sizePolicy().hasHeightForWidth())
        self.widget_hours_list.setSizePolicy(sizePolicy)
        self.vL_main.addWidget(self.widget_hours_list)

        self.calendar = QtWidgets.QCalendarWidget(self.widget_hours_list)
        self.hL_widget_hours_list.addWidget(self.calendar)

        self.scrollArea_hours_list = QtWidgets.QScrollArea(self.widget_hours_list)
        self.scrollArea_hours_list.setWidgetResizable(True)
        self.scrollArea_hours_list.setObjectName("scrollArea_hours_list")
        self.sAWContent_hours_list = QtWidgets.QWidget()
        self.sAWContent_hours_list.setObjectName("sAWContent_hours_list")
        self.vL_sAWContent_hours_list = QtWidgets.QVBoxLayout(self.sAWContent_hours_list)
        self.vL_sAWContent_hours_list.setObjectName("vL_sAWContent_hours_list")
        self.scrollArea_hours_list.setWidget(self.sAWContent_hours_list)
        self.hL_widget_hours_list.addWidget(self.scrollArea_hours_list)

        self.lab_sum = QtWidgets.QLabel(TTableEditor)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab_sum.setFont(font)
        self.vL_main.addWidget(self.lab_sum)

        self.lab_need = QtWidgets.QLabel(TTableEditor)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lab_need.setFont(font)
        self.vL_main.addWidget(self.lab_need)

        self.hL_widget_hours_list.setStretch(1, 2)

        self.retranslateUi(TTableEditor)
        QtCore.QMetaObject.connectSlotsByName(TTableEditor)

    def retranslateUi(self, TTableEditor):
        _translate = QtCore.QCoreApplication.translate
        TTableEditor.setWindowTitle(_translate("TTableEditor", "Редактор расписания"))
        self.lab_hours.setText(_translate("TTableEditor", "Количество часов:"))
        self.btn_set_hours.setText(_translate("TTableEditor", "Установить часы"))
        self.btn_del_hours.setText(_translate("TTableEditor", "Удалить часы"))
        self.lab_sum.setText(_translate("TTableEditor", "Сумма часов: "))
        self.lab_need.setText(_translate("TTableEditor", "Необходимо часов: "))
