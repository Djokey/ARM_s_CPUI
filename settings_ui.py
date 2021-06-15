from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(700, 450)
        self.vL_main = QtWidgets.QVBoxLayout(Settings)
        self.vL_main.setObjectName("vL_main")

        self.gr_box = QtWidgets.QWidget()
        self.vL_main.addWidget(self.gr_box)

        self.vL_gr_box = QtWidgets.QVBoxLayout(self.gr_box)
        self.vL_gr_box.setObjectName("vL_gr_box")

        self.check_mail = QtWidgets.QCheckBox()
        self.check_mail.setObjectName("check_mail")
        self.vL_gr_box.addWidget(self.check_mail)

        self.label_mail = QtWidgets.QLabel()
        self.label_mail.setObjectName("label_mail")
        self.vL_gr_box.addWidget(self.label_mail)

        self.lEdit_mail = QtWidgets.QLineEdit()
        self.lEdit_mail.setObjectName("lEdit_mail")
        self.vL_gr_box.addWidget(self.lEdit_mail)

        self.label_password = QtWidgets.QLabel()
        self.label_password.setObjectName("label_password")
        self.vL_gr_box.addWidget(self.label_password)

        self.lEdit_password = QtWidgets.QLineEdit()
        self.lEdit_password.setObjectName("lEdit_password")
        self.lEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.vL_gr_box.addWidget(self.lEdit_password)

        self.label_service = QtWidgets.QLabel()
        self.label_service.setObjectName("label_service")
        self.vL_gr_box.addWidget(self.label_service)

        self.lEdit_service = QtWidgets.QLineEdit()
        self.lEdit_service.setObjectName("lEdit_service")
        self.vL_gr_box.addWidget(self.lEdit_service)

        self.label_sender = QtWidgets.QLabel()
        self.label_sender.setObjectName("label_sender")
        self.vL_gr_box.addWidget(self.label_sender)

        self.lEdit_sender = QtWidgets.QLineEdit()
        self.lEdit_sender.setObjectName("lEdit_sender")
        self.vL_gr_box.addWidget(self.lEdit_sender)

        self.label_path = QtWidgets.QLabel()
        self.label_path.setObjectName("label_path")
        self.vL_gr_box.addWidget(self.label_path)

        self.lEdit_path = QtWidgets.QLineEdit()
        self.lEdit_path.setObjectName("lEdit_path")
        self.vL_gr_box.addWidget(self.lEdit_path)

        self.label_rate = QtWidgets.QLabel()
        self.label_rate.setObjectName("label_rate")
        self.vL_gr_box.addWidget(self.label_rate)

        self.spin_rate = QtWidgets.QSpinBox()
        self.spin_rate.setObjectName("spin_rate")
        self.spin_rate.setMinimum(1)
        self.vL_gr_box.addWidget(self.spin_rate)

        self.label_save = QtWidgets.QLabel()
        self.label_save.setObjectName("label_save")
        self.vL_gr_box.addWidget(self.label_save)

        self.btn_save = QtWidgets.QPushButton()
        self.btn_save.setObjectName("btn_save")
        self.vL_gr_box.addWidget(self.btn_save)

        self.btn_back = QtWidgets.QPushButton()
        self.btn_back.setObjectName("btn_back")
        self.vL_gr_box.addWidget(self.btn_back)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Настройки"))
        self.label_password.setText(_translate("Settings", "Пароль от вашего почтового ящика:"))
        self.label_mail.setText(_translate("Settings", "Ваш почтовый ящик:"))
        self.label_sender.setText(_translate("Settings", "Почтовый ящик отправителя:"))
        self.label_path.setText(_translate("Settings", "Путь сохранения почты:"))
        self.label_rate.setText(_translate("Settings", "Частота проверки почты (минуты):"))
        self.label_service.setText(_translate("Settings", "Почтовый сервис:"))
        self.label_save.setText(_translate("Settings", "Сохраняйте настройки только если знаете, что делаете!"))
        self.btn_save.setText(_translate("Settings", "Сохранить настройки"))
        self.btn_back.setText(_translate("Settings", "Отмена"))
        self.check_mail.setText(_translate("Settings", "Проверять почту"))
