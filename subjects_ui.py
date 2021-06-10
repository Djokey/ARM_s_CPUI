from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Subjects(object):
    def setupUi(self, Subjects):
        Subjects.setObjectName("Subjects")
        Subjects.resize(910, 591)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Subjects)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_sub_input_box = QtWidgets.QWidget(Subjects)
        self.widget_sub_input_box.setObjectName("widget_sub_input_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_sub_input_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.widget_sub_input_box)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_sub_add = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_sub_add.setFont(font)
        self.pushButton_sub_add.setObjectName("pushButton_sub_add")
        self.horizontalLayout_2.addWidget(self.pushButton_sub_add)
        self.pushButton_sub_save = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_sub_save.setFont(font)
        self.pushButton_sub_save.setObjectName("pushButton_sub_save")
        self.horizontalLayout_2.addWidget(self.pushButton_sub_save)
        self.verticalLayout.addWidget(self.widget)
        self.label_sub_name = QtWidgets.QLabel(self.widget_sub_input_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sub_name.setFont(font)
        self.label_sub_name.setObjectName("label_sub_name")
        self.verticalLayout.addWidget(self.label_sub_name)
        self.textEdit_sub_name = QtWidgets.QTextEdit(self.widget_sub_input_box)
        self.textEdit_sub_name.setObjectName("textEdit_sub_name")
        self.verticalLayout.addWidget(self.textEdit_sub_name)
        self.label_sub_tax = QtWidgets.QLabel(self.widget_sub_input_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sub_tax.setFont(font)
        self.label_sub_tax.setObjectName("label_sub_tax")
        self.verticalLayout.addWidget(self.label_sub_tax)
        self.lineEdit_sub_tax = QtWidgets.QLineEdit(self.widget_sub_input_box)
        self.lineEdit_sub_tax.setObjectName("lineEdit_sub_tax")
        self.verticalLayout.addWidget(self.lineEdit_sub_tax)
        self.label_sub_teach = QtWidgets.QLabel(self.widget_sub_input_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sub_teach.setFont(font)
        self.label_sub_teach.setObjectName("label_sub_teach")
        self.verticalLayout.addWidget(self.label_sub_teach)
        self.comboBox_sub_teach = QtWidgets.QComboBox(self.widget_sub_input_box)
        self.comboBox_sub_teach.setObjectName("comboBox_sub_teach")
        self.verticalLayout.addWidget(self.comboBox_sub_teach)
        self.label_sub_price = QtWidgets.QLabel(self.widget_sub_input_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sub_price.setFont(font)
        self.label_sub_price.setObjectName("label_sub_price")
        self.verticalLayout.addWidget(self.label_sub_price)
        self.lineEdit_sub_price = QtWidgets.QLineEdit(self.widget_sub_input_box)
        self.lineEdit_sub_price.setObjectName("lineEdit_sub_price")
        self.verticalLayout.addWidget(self.lineEdit_sub_price)
        self.label_sub_prog = QtWidgets.QLabel(self.widget_sub_input_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sub_prog.setFont(font)
        self.label_sub_prog.setObjectName("label_sub_prog")
        self.verticalLayout.addWidget(self.label_sub_prog)
        self.comboBox_sub_prog = QtWidgets.QComboBox(self.widget_sub_input_box)
        self.comboBox_sub_prog.setObjectName("comboBox_sub_prog")
        self.verticalLayout.addWidget(self.comboBox_sub_prog)
        self.label_sub_hours = QtWidgets.QLabel(self.widget_sub_input_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sub_hours.setFont(font)
        self.label_sub_hours.setObjectName("label_sub_hours")
        self.verticalLayout.addWidget(self.label_sub_hours)
        self.lineEdit_sub_hours = QtWidgets.QLineEdit(self.widget_sub_input_box)
        self.lineEdit_sub_hours.setObjectName("lineEdit_sub_hours")
        self.verticalLayout.addWidget(self.lineEdit_sub_hours)
        self.pushButton_sub_back = QtWidgets.QPushButton(self.widget_sub_input_box)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sub_back.setFont(font)
        self.pushButton_sub_back.setObjectName("pushButton_sub_back")
        self.verticalLayout.addWidget(self.pushButton_sub_back)
        self.horizontalLayout.addWidget(self.widget_sub_input_box)
        self.widget_sub_list_box = QtWidgets.QWidget(Subjects)
        self.widget_sub_list_box.setObjectName("widget_sub_list_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_sub_list_box)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_left_up_sub = QtWidgets.QWidget(self.widget_sub_list_box)
        self.widget_left_up_sub.setObjectName("widget_left_up_sub")
        self.hL_widget_left_up_sub = QtWidgets.QHBoxLayout(self.widget_left_up_sub)
        self.hL_widget_left_up_sub.setObjectName("hL_widget_left_up_sub")
        self.label_search_sub = QtWidgets.QLabel(self.widget_left_up_sub)
        self.label_search_sub.setObjectName("label_search_sub")
        self.hL_widget_left_up_sub.addWidget(self.label_search_sub)
        self.lineEdit_search_sub = QtWidgets.QLineEdit(self.widget_left_up_sub)
        self.lineEdit_search_sub.setObjectName("lineEdit_search_sub")
        self.hL_widget_left_up_sub.addWidget(self.lineEdit_search_sub)
        self.pushButton_sub_delete = QtWidgets.QPushButton(self.widget_left_up_sub)
        self.pushButton_sub_delete.setObjectName("pushButton_sub_delete")
        self.hL_widget_left_up_sub.addWidget(self.pushButton_sub_delete)
        self.verticalLayout_2.addWidget(self.widget_left_up_sub)
        self.scrollArea_sub_list = QtWidgets.QScrollArea(self.widget_sub_list_box)
        self.scrollArea_sub_list.setWidgetResizable(True)
        self.scrollArea_sub_list.setObjectName("scrollArea_sub_list")
        self.sAWContent_sub_list = QtWidgets.QWidget()
        self.sAWContent_sub_list.setGeometry(QtCore.QRect(0, 0, 478, 506))
        self.sAWContent_sub_list.setObjectName("sAWContent_sub_list")
        self.vL_sAWContent_sub_list = QtWidgets.QVBoxLayout(self.sAWContent_sub_list)
        self.vL_sAWContent_sub_list.setObjectName("vL_sAWContent_sub_list")
        self.scrollArea_sub_list.setWidget(self.sAWContent_sub_list)
        self.verticalLayout_2.addWidget(self.scrollArea_sub_list)
        self.horizontalLayout.addWidget(self.widget_sub_list_box)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Subjects)
        QtCore.QMetaObject.connectSlotsByName(Subjects)

    def retranslateUi(self, Subjects):
        _translate = QtCore.QCoreApplication.translate
        Subjects.setWindowTitle(_translate("Subjects", "Предметы"))
        self.pushButton_sub_add.setText(_translate("Subjects", "Добавить новую запись"))
        self.pushButton_sub_save.setText(_translate("Subjects", "Сохранить выбранную запись"))
        self.label_sub_name.setText(_translate("Subjects", "Наименование предмета"))
        self.label_sub_tax.setText(_translate("Subjects", "Преподавательская почасовая, руб."))
        self.label_sub_teach.setText(_translate("Subjects", "Преподаватель"))
        self.label_sub_price.setText(_translate("Subjects", "Полная стоимость, руб."))
        self.label_sub_prog.setText(_translate("Subjects", "Образовательная программа"))
        self.label_sub_hours.setText(_translate("Subjects", "Всего часов в предмете"))
        self.pushButton_sub_back.setText(_translate("Subjects", "Назад"))
        self.label_search_sub.setText(_translate("Subjects", "Поиск:"))
        self.pushButton_sub_delete.setText(_translate("Subjects", "Удалить выбранную запись"))
