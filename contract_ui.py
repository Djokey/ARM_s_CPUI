from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Contract(object):
    def setupUi(self, Contract):
        Contract.setObjectName("Contract")
        Contract.resize(600, 450)

        self.vL_main = QtWidgets.QVBoxLayout(Contract)
        self.vL_main.setObjectName("vL_main")

        self.checkBox_add_new_stud = QtWidgets.QCheckBox(Contract)
        self.checkBox_add_new_stud.setObjectName("checkBox_add_new_stud")
        self.vL_main.addWidget(self.checkBox_add_new_stud)

        self.widget_head = QtWidgets.QWidget(Contract)
        self.widget_head.setObjectName("widget_head")
        self.hL_widget_head = QtWidgets.QHBoxLayout(self.widget_head)
        self.hL_widget_head.setObjectName("hL_widget_head")
        self.vL_main.addWidget(self.widget_head)

        self.lab_head = QtWidgets.QLabel(Contract)
        self.lab_head.setObjectName("lab_head")
        self.hL_widget_head.addWidget(self.lab_head)

        self.comboBox_head = QtWidgets.QComboBox(Contract)
        self.comboBox_head.setObjectName("comboBox_head")
        self.hL_widget_head.addWidget(self.comboBox_head)

        self.widget_head_ls = QtWidgets.QWidget(Contract)
        self.widget_head_ls.setObjectName("widget_head_ls")
        self.hL_widget_head_ls = QtWidgets.QHBoxLayout(self.widget_head_ls)
        self.hL_widget_head_ls.setObjectName("hL_widget_head_ls")
        self.vL_main.addWidget(self.widget_head_ls)

        self.lab_head_ls = QtWidgets.QLabel(Contract)
        self.lab_head_ls.setObjectName("lab_head_ls")
        self.hL_widget_head_ls.addWidget(self.lab_head_ls)

        self.comboBox_head_ls = QtWidgets.QComboBox(Contract)
        self.comboBox_head_ls.setObjectName("comboBox_head_ls")
        self.hL_widget_head_ls.addWidget(self.comboBox_head_ls)

        self.widget_manager_cpui = QtWidgets.QWidget(Contract)
        self.widget_manager_cpui.setObjectName("widget_manager_cpui")
        self.hL_widget_manager_cpui = QtWidgets.QHBoxLayout(self.widget_manager_cpui)
        self.hL_widget_manager_cpui.setObjectName("hL_widget_manager_cpui")
        self.vL_main.addWidget(self.widget_manager_cpui)

        self.lab_manager_cpui = QtWidgets.QLabel(Contract)
        self.lab_manager_cpui.setObjectName("lab_manager_cpui")
        self.hL_widget_manager_cpui.addWidget(self.lab_manager_cpui)

        self.comboBox_manager_cpui = QtWidgets.QComboBox(Contract)
        self.comboBox_manager_cpui.setObjectName("comboBox_manager_cpui")
        self.hL_widget_manager_cpui.addWidget(self.comboBox_manager_cpui)

        self.widget_prog = QtWidgets.QWidget(Contract)
        self.widget_prog.setObjectName("widget_prog")

        self.hL_widget_prog = QtWidgets.QHBoxLayout(self.widget_prog)
        self.hL_widget_prog.setObjectName("hL_widget_prog")
        self.vL_main.addWidget(self.widget_prog)

        self.lab_prog = QtWidgets.QLabel(Contract)
        self.lab_prog.setObjectName("lab_prog")
        self.hL_widget_prog.addWidget(self.lab_prog)

        self.comboBox_prog = QtWidgets.QComboBox(Contract)
        self.comboBox_prog.setObjectName("comboBox_prog")
        self.hL_widget_prog.addWidget(self.comboBox_prog)

        self.lab_class = QtWidgets.QLabel(Contract)
        self.lab_class.setObjectName("lab_class")
        self.hL_widget_prog.addWidget(self.lab_class)

        self.lEdit_class = QtWidgets.QLineEdit(Contract)
        self.lEdit_class.setObjectName("lEdit_class")
        self.hL_widget_prog.addWidget(self.lEdit_class)

        self.lab_date_start = QtWidgets.QLabel(Contract)
        self.lab_date_start.setObjectName("lab_date_start")
        self.hL_widget_prog.addWidget(self.lab_date_start)

        self.dateEdit_date_start = QtWidgets.QDateEdit(Contract)
        self.dateEdit_date_start.setObjectName("dateEdit_date_start")
        self.hL_widget_prog.addWidget(self.dateEdit_date_start)

        self.lab_date_end = QtWidgets.QLabel(Contract)
        self.lab_date_end.setObjectName("lab_date_end")
        self.hL_widget_prog.addWidget(self.lab_date_end)

        self.dateEdit_date_end = QtWidgets.QDateEdit(Contract)
        self.dateEdit_date_end.setObjectName("dateEdit_date_end")
        self.hL_widget_prog.addWidget(self.dateEdit_date_end)

        self.widget_fullname = QtWidgets.QWidget(Contract)
        self.widget_fullname.setObjectName("widget_fullname")

        self.hL_widget_fullname = QtWidgets.QHBoxLayout(self.widget_fullname)
        self.hL_widget_fullname.setObjectName("hL_widget_fullname")
        self.vL_main.addWidget(self.widget_fullname)

        self.lab_fullname = QtWidgets.QLabel(Contract)
        self.lab_fullname.setObjectName("lab_fullname")
        self.hL_widget_fullname.addWidget(self.lab_fullname)

        self.lEdit_fullname = QtWidgets.QLineEdit(Contract)
        self.lEdit_fullname.setObjectName("lEdit_fullname")
        self.hL_widget_fullname.addWidget(self.lEdit_fullname)

        self.lab_fullname_parent = QtWidgets.QLabel(Contract)
        self.lab_fullname_parent.setObjectName("lab_fullname_parent")
        self.hL_widget_fullname.addWidget(self.lab_fullname_parent)

        self.lEdit_fullname_parent = QtWidgets.QLineEdit(Contract)
        self.lEdit_fullname_parent.setObjectName("lEdit_fullname_parent")
        self.hL_widget_fullname.addWidget(self.lEdit_fullname_parent)

        self.widget_birthday = QtWidgets.QWidget(Contract)
        self.widget_birthday.setObjectName("widget_birthday")

        self.hL_widget_birthday = QtWidgets.QHBoxLayout(self.widget_birthday)
        self.hL_widget_birthday.setObjectName("hL_widget_birthday")
        self.vL_main.addWidget(self.widget_birthday)

        self.lab_birthday = QtWidgets.QLabel(Contract)
        self.lab_birthday.setObjectName("lab_birthday")
        self.hL_widget_birthday.addWidget(self.lab_birthday)

        self.dateEdit_birthday = QtWidgets.QDateEdit(Contract)
        self.dateEdit_birthday.setObjectName("dateEdit_birthday")
        self.hL_widget_birthday.addWidget(self.dateEdit_birthday)

        self.groupBox_gender = QtWidgets.QGroupBox(Contract)
        self.groupBox_gender.setObjectName("groupBox_gender")
        self.hL_widget_birthday.addWidget(self.groupBox_gender)

        self.hL_groupBox_gender = QtWidgets.QHBoxLayout(self.groupBox_gender)
        self.hL_groupBox_gender.setObjectName("hL_groupBox_gender")

        self.radioButton_gender_male = QtWidgets.QRadioButton(self.groupBox_gender)
        self.radioButton_gender_male.setChecked(True)
        self.radioButton_gender_male.setObjectName("radioButton_stud_gender_male")
        self.hL_groupBox_gender.addWidget(self.radioButton_gender_male)

        self.radioButton_gender_female = QtWidgets.QRadioButton(self.groupBox_gender)
        self.radioButton_gender_female.setObjectName("radioButton_stud_gender_female")
        self.hL_groupBox_gender.addWidget(self.radioButton_gender_female)

        self.widget_address = QtWidgets.QWidget(Contract)
        self.widget_address.setObjectName("widget_address")

        self.hL_widget_address = QtWidgets.QHBoxLayout(self.widget_address)
        self.hL_widget_address.setObjectName("hL_widget_address")
        self.vL_main.addWidget(self.widget_address)

        self.lab_address = QtWidgets.QLabel(Contract)
        self.lab_address.setObjectName("lab_address")
        self.hL_widget_address.addWidget(self.lab_address)

        self.lEdit_address = QtWidgets.QLineEdit(Contract)
        self.lEdit_address.setObjectName("lEdit_address")
        self.hL_widget_address.addWidget(self.lEdit_address)

        self.lab_uinst = QtWidgets.QLabel(Contract)
        self.lab_uinst.setObjectName("lab_uinst")
        self.hL_widget_address.addWidget(self.lab_uinst)

        self.lEdit_uinst = QtWidgets.QLineEdit(Contract)
        self.lEdit_uinst.setObjectName("lEdit_uinst")
        self.hL_widget_address.addWidget(self.lEdit_uinst)

        self.widget_phone = QtWidgets.QWidget(Contract)
        self.widget_phone.setObjectName("widget_phone")

        self.hL_widget_phone = QtWidgets.QHBoxLayout(self.widget_phone)
        self.hL_widget_phone.setObjectName("hL_widget_phone")
        self.vL_main.addWidget(self.widget_phone)

        self.lab_phone = QtWidgets.QLabel(Contract)
        self.lab_phone.setObjectName("lab_phone")
        self.hL_widget_phone.addWidget(self.lab_phone)

        self.lEdit_phone = QtWidgets.QLineEdit(Contract)
        self.lEdit_phone.setObjectName("lEdit_phone")
        self.hL_widget_phone.addWidget(self.lEdit_phone)

        self.lab_phone_parent = QtWidgets.QLabel(Contract)
        self.lab_phone_parent.setObjectName("lab_phone_parent")
        self.hL_widget_phone.addWidget(self.lab_phone_parent)

        self.lEdit_phone_parent = QtWidgets.QLineEdit(Contract)
        self.lEdit_phone_parent.setObjectName("lEdit_phone_parent")
        self.hL_widget_phone.addWidget(self.lEdit_phone_parent)

        self.widget_mail = QtWidgets.QWidget(Contract)
        self.widget_mail.setObjectName("widget_mail")

        self.hL_widget_mail = QtWidgets.QHBoxLayout(self.widget_mail)
        self.hL_widget_mail.setObjectName("hL_widget_mail")
        self.vL_main.addWidget(self.widget_mail)

        self.lab_mail = QtWidgets.QLabel(Contract)
        self.lab_mail.setObjectName("lab_mail")
        self.hL_widget_mail.addWidget(self.lab_mail)

        self.lEdit_mail = QtWidgets.QLineEdit(Contract)
        self.lEdit_mail.setObjectName("lEdit_mail")
        self.hL_widget_mail.addWidget(self.lEdit_mail)

        self.lab_mail_parent = QtWidgets.QLabel(Contract)
        self.lab_mail_parent.setObjectName("lab_mail_parent")
        self.hL_widget_mail.addWidget(self.lab_mail_parent)

        self.lEdit_mail_parent = QtWidgets.QLineEdit(Contract)
        self.lEdit_mail_parent.setObjectName("lEdit_mail_parent")
        self.hL_widget_mail.addWidget(self.lEdit_mail_parent)

        self.widget_passport = QtWidgets.QWidget(Contract)
        self.widget_passport.setObjectName("widget_passport")

        self.hL_widget_passport = QtWidgets.QHBoxLayout(self.widget_passport)
        self.hL_widget_passport.setObjectName("hL_widget_passport")
        self.vL_main.addWidget(self.widget_passport)

        self.lab_passport = QtWidgets.QLabel(Contract)
        self.lab_passport.setObjectName("lab_passport")
        self.hL_widget_passport.addWidget(self.lab_passport)

        self.lEdit_seria = QtWidgets.QLineEdit(Contract)
        self.lEdit_seria.setObjectName("lEdit_seria")
        self.hL_widget_passport.addWidget(self.lEdit_seria)

        self.lEdit_number = QtWidgets.QLineEdit(Contract)
        self.lEdit_number.setObjectName("lEdit_number")
        self.hL_widget_passport.addWidget(self.lEdit_number)

        self.dateEdit_passport_date = QtWidgets.QDateEdit(Contract)
        self.dateEdit_passport_date.setObjectName("dateEdit_passport_date")
        self.hL_widget_passport.addWidget(self.dateEdit_passport_date)

        self.widget_passport_whom = QtWidgets.QWidget(Contract)
        self.widget_passport_whom.setObjectName("widget_passport_whom")

        self.hL_widget_passport_whom = QtWidgets.QHBoxLayout(self.widget_passport_whom)
        self.hL_widget_passport_whom.setObjectName("hL_widget_passport_whom")
        self.vL_main.addWidget(self.widget_passport_whom)

        self.lab_passport_whom = QtWidgets.QLabel(Contract)
        self.lab_passport_whom.setObjectName("lab_passport_whom")
        self.hL_widget_passport_whom.addWidget(self.lab_passport_whom)

        self.lEdit_passport_whom = QtWidgets.QLineEdit(Contract)
        self.lEdit_passport_whom.setObjectName("lEdit_passport_whom")
        self.hL_widget_passport_whom.addWidget(self.lEdit_passport_whom)

        self.lab_passport_parent_whom = QtWidgets.QLabel(Contract)
        self.lab_passport_parent_whom.setObjectName("lab_passport_parent_whom")
        self.hL_widget_passport_whom.addWidget(self.lab_passport_parent_whom)

        self.lEdit_passport_parent_whom = QtWidgets.QLineEdit(Contract)
        self.lEdit_passport_parent_whom.setObjectName("lEdit_passport_parent_whom")
        self.hL_widget_passport_whom.addWidget(self.lEdit_passport_parent_whom)

        self.widget_passport_parent = QtWidgets.QWidget(Contract)
        self.widget_passport_parent.setObjectName("widget_passport_parent")

        self.hL_widget_passport_parent = QtWidgets.QHBoxLayout(self.widget_passport_parent)
        self.hL_widget_passport_parent.setObjectName("hL_widget_passport_parent")
        self.vL_main.addWidget(self.widget_passport_parent)

        self.lab_passport_parent = QtWidgets.QLabel(Contract)
        self.lab_passport_parent.setObjectName("lab_passport_parent")
        self.hL_widget_passport_parent.addWidget(self.lab_passport_parent)

        self.lEdit_seria_parent = QtWidgets.QLineEdit(Contract)
        self.lEdit_seria_parent.setObjectName("lEdit_seria_parent")
        self.hL_widget_passport_parent.addWidget(self.lEdit_seria_parent)

        self.lEdit_number_parent = QtWidgets.QLineEdit(Contract)
        self.lEdit_number_parent.setObjectName("lEdit_number_parent")
        self.hL_widget_passport_parent.addWidget(self.lEdit_number_parent)

        self.dateEdit_passport_parent_date = QtWidgets.QDateEdit(Contract)
        self.dateEdit_passport_parent_date.setObjectName("dateEdit_passport_parent_date")
        self.hL_widget_passport_parent.addWidget(self.dateEdit_passport_parent_date)

        self.scrollArea_subs = QtWidgets.QScrollArea(Contract)
        self.scrollArea_subs.setWidgetResizable(True)
        self.scrollArea_subs.setObjectName("scrollArea_subs")
        self.sAWContent_subs = QtWidgets.QWidget()
        self.sAWContent_subs.setObjectName("sAWContent_subs")
        self.vL_sAWContent_subs = QtWidgets.QVBoxLayout(self.sAWContent_subs)
        self.vL_sAWContent_subs.setObjectName("vL_sAWContent_subs")
        self.scrollArea_subs.setWidget(self.sAWContent_subs)
        self.vL_main.addWidget(self.scrollArea_subs)

        self.pushButton_save_doc = QtWidgets.QPushButton(Contract)
        self.pushButton_save_doc.setObjectName("pushButton_save_doc")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save_doc.setFont(font)
        self.vL_main.addWidget(self.pushButton_save_doc)

        self.pushButton_back = QtWidgets.QPushButton(Contract)
        self.pushButton_back.setObjectName("pushButton_back")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.vL_main.addWidget(self.pushButton_back)

        self.retranslateUi(Contract)
        QtCore.QMetaObject.connectSlotsByName(Contract)

    def retranslateUi(self, Contract):
        _translate = QtCore.QCoreApplication.translate
        Contract.setWindowTitle(_translate("Contract", "Редактор документа"))
        self.lab_head.setText(_translate("Contract", "Директор: "))
        self.lab_manager_cpui.setText(_translate("Contract", "Зав. ЦПЮИ: "))
        self.lab_head_ls.setText(_translate("Contract", "Зав. правовым сектором: "))
        self.pushButton_save_doc.setText(_translate("Contract", "Сохранить документы договора"))
        self.pushButton_back.setText(_translate("Contract", "Назад"))
        self.lab_prog.setText(_translate("Contract", "Программа: "))
        self.lab_class.setText(_translate("Contract", "Класс (9, 10, 11): "))
        self.lab_birthday.setText(_translate("Contract", "Дата рождения: "))
        self.lab_passport_whom.setText(_translate("Contract", "Кем выдан паспорт обучающегося: "))
        self.lab_passport_parent_whom.setText(_translate("Contract", "Кем выдан паспорт представителя: "))
        self.lab_fullname.setText(_translate("Contract", "ФИО обучающегося: "))
        self.lab_fullname_parent.setText(_translate("Contract", "ФИО представителя: "))
        self.lab_date_start.setText(_translate("Contract", "Даты проведения с: "))
        self.lab_address.setText(_translate("Contract", "Адрес регистрации: "))
        self.lab_uinst.setText(_translate("Contract", "Место учебы: "))
        self.lab_date_end.setText(_translate("Contract", "        по: "))
        self.lab_phone.setText(_translate("Contract", "Телефон: "))
        self.lab_phone_parent.setText(_translate("Contract", "Телефон представителя: "))
        self.checkBox_add_new_stud.setText(_translate("Contract", "Сразу добавить обучающегося в реестр"))
        self.lab_mail.setText(_translate("Contract", "Электронная почта: "))
        self.lab_passport.setText(_translate("Contract", "Паспорт (серия, номер, дата выдачи): "))
        self.lab_passport_parent.setText(_translate("Contract", "Паспорт представителя (серия, номер, дата выдачи): "))
        self.lab_mail_parent.setText(_translate("Contract", "Электронная почта представителя: "))
        self.groupBox_gender.setTitle(_translate("Contract", "Пол"))
        self.radioButton_gender_male.setText(_translate("Contract", "Мужской"))
        self.radioButton_gender_female.setText(_translate("Contract", "Женский"))
