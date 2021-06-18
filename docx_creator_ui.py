from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DocxCreator(object):
    def setupUi(self, DocxCreator):
        DocxCreator.setObjectName("DocxCreator")
        DocxCreator.resize(800, 700)

        self.not_main = QtWidgets.QVBoxLayout(DocxCreator)
        self.not_main.setObjectName("not_main")

        self.widget_main = QtWidgets.QWidget(DocxCreator)
        self.not_main.addWidget(self.widget_main)

        self.vL_main = QtWidgets.QVBoxLayout(self.widget_main)
        self.vL_main.setObjectName("vL_main")

        self.pushButton_decree_enrollment = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_decree_enrollment.setObjectName("pushButton_decree_enrollment")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_decree_enrollment.setFont(font)
        self.vL_main.addWidget(self.pushButton_decree_enrollment)

        self.pushButton_note_passes = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_note_passes.setObjectName("pushButton_note_passes")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_note_passes.setFont(font)
        self.vL_main.addWidget(self.pushButton_note_passes)

        self.pushButton_note_passwords = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_note_passwords.setObjectName("pushButton_note_passwords")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_note_passwords.setFont(font)
        self.vL_main.addWidget(self.pushButton_note_passwords)

        self.pushButton_note_studs_list = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_note_studs_list.setObjectName("pushButton_note_studs_list")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_note_studs_list.setFont(font)
        self.vL_main.addWidget(self.pushButton_note_studs_list)

        self.pushButton_contract = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_contract.setObjectName("pushButton_contract")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_contract.setFont(font)
        self.vL_main.addWidget(self.pushButton_contract)

        self.retranslateUi(DocxCreator)
        QtCore.QMetaObject.connectSlotsByName(DocxCreator)

    def retranslateUi(self, DocxCreator):
        _translate = QtCore.QCoreApplication.translate
        DocxCreator.setWindowTitle(_translate("DocxCreator", "Редактор сметы"))
        self.pushButton_decree_enrollment.setText(_translate("DocxCreator", "Приказ на зачисление"))
        self.pushButton_note_passes.setText(_translate("DocxCreator", "Служебная записка на пропуска"))
        self.pushButton_note_passwords.setText(_translate("DocxCreator", "Служебная записка на пароли"))
        self.pushButton_note_studs_list.setText(_translate("DocxCreator", "Служебная записка на списки обучающихся"))
        self.pushButton_contract.setText(_translate("DocxCreator", "Договор"))
