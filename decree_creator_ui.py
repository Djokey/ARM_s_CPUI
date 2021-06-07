from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DecreeCreator(object):
    def setupUi(self, DecreeCreator):
        DecreeCreator.setObjectName("DecreeCreator")
        DecreeCreator.resize(800, 700)

        self.not_main = QtWidgets.QVBoxLayout(DecreeCreator)
        self.not_main.setObjectName("not_main")

        self.widget_main = QtWidgets.QWidget(DecreeCreator)
        self.not_main.addWidget(self.widget_main)

        self.vL_main = QtWidgets.QVBoxLayout(self.widget_main)
        self.vL_main.setObjectName("vL_main")

        self.pushButton_decree_enrollment = QtWidgets.QPushButton(self.widget_main)
        self.pushButton_decree_enrollment.setObjectName("pushButton_decree_enrollment")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_decree_enrollment.setFont(font)
        self.vL_main.addWidget(self.pushButton_decree_enrollment)

        self.retranslateUi(DecreeCreator)
        QtCore.QMetaObject.connectSlotsByName(DecreeCreator)

    def retranslateUi(self, DecreeCreator):
        _translate = QtCore.QCoreApplication.translate
        DecreeCreator.setWindowTitle(_translate("DecreeCreator", "Редактор сметы"))
        self.pushButton_decree_enrollment.setText(_translate("DecreeCreator", "Приказ на зачисление"))
        # self.pushButton_decree_enrollment.setText(_translate("DecreeCreator", "Сохранить смету"))
