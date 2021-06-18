from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NoteList(object):
    def setupUi(self, NoteList):
        NoteList.setObjectName("NoteList")
        NoteList.resize(800, 450)

        self.vL_main = QtWidgets.QVBoxLayout(NoteList)
        self.vL_main.setObjectName("vL_main")

        self.checkBox_and_prog = QtWidgets.QCheckBox(NoteList)
        self.checkBox_and_prog.setObjectName("checkBox_and_prog")
        self.vL_main.addWidget(self.checkBox_and_prog)

        self.scrollArea_groups = QtWidgets.QScrollArea(NoteList)
        self.scrollArea_groups.setWidgetResizable(True)
        self.scrollArea_groups.setObjectName("scrollArea_groups")
        self.sAWContent_groups = QtWidgets.QWidget()
        self.sAWContent_groups.setObjectName("sAWContent_groups")
        self.vL_sAWContent_groups = QtWidgets.QVBoxLayout(self.sAWContent_groups)
        self.vL_sAWContent_groups.setObjectName("vL_sAWContent_groups")
        self.scrollArea_groups.setWidget(self.sAWContent_groups)
        self.vL_main.addWidget(self.scrollArea_groups)

        self.pushButton_save_doc = QtWidgets.QPushButton(NoteList)
        self.pushButton_save_doc.setObjectName("pushButton_save_doc")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save_doc.setFont(font)
        self.vL_main.addWidget(self.pushButton_save_doc)

        self.pushButton_back = QtWidgets.QPushButton(NoteList)
        self.pushButton_back.setObjectName("pushButton_back")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.vL_main.addWidget(self.pushButton_back)

        self.retranslateUi(NoteList)
        QtCore.QMetaObject.connectSlotsByName(NoteList)

    def retranslateUi(self, NoteList):
        _translate = QtCore.QCoreApplication.translate
        NoteList.setWindowTitle(_translate("NoteList", "Редактор документа"))
        self.pushButton_save_doc.setText(_translate("NoteList", "Сохранить списки"))
        self.pushButton_back.setText(_translate("NoteList", "Назад"))
        self.checkBox_and_prog.setText(_translate("NoteList", "Списки с программами"))
