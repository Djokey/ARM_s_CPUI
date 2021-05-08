from ui import *
from headers_ui import *
from programs_ui import *
from teachers_ui import *
from groups_ui import *
from arm_db import *
import sys
import os
import win32api
import win32print
from PyQt5.QtWidgets import QMessageBox


# Class for main window application
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._translate = QtCore.QCoreApplication.translate

        self.ui.widget_headers = QtWidgets.QWidget(self.ui.widget_roster_editors)
        self.ui.hL_widget_roster_editors.addWidget(self.ui.widget_headers)
        self.head_ui = Ui_Headers()
        self.head_ui.setupUi(self.ui.widget_headers)

        self.ui.widget_teachers = QtWidgets.QWidget(self.ui.widget_roster_editors)
        self.ui.hL_widget_roster_editors.addWidget(self.ui.widget_teachers)
        self.teach_ui = Ui_Teachers()
        self.teach_ui.setupUi(self.ui.widget_teachers)

        self.ui.widget_programs = QtWidgets.QWidget(self.ui.widget_roster_editors)
        self.ui.hL_widget_roster_editors.addWidget(self.ui.widget_programs)
        self.prog_ui = Ui_Programs()
        self.prog_ui.setupUi(self.ui.widget_programs)

        self.ui.widget_groups = QtWidgets.QWidget(self.ui.widget_roster_editors)
        self.ui.hL_widget_roster_editors.addWidget(self.ui.widget_groups)
        self.groups_ui = Ui_Groups()
        self.groups_ui.setupUi(self.ui.widget_groups)

        self.clear_for_start()
        self.setup_buttons_funcs()
        self.load_for_start()
        self.resize(1000, 600)

    # Func for edit database table Headers
    def headers_win(self):
        self.ui.widget_roster.hide()
        self.ui.widget_headers.show()
        self.load_db_headers()

    # Func for edit database table Programs
    def programs_win(self):
        self.ui.widget_roster.hide()
        self.ui.widget_programs.show()
        self.load_db_programs()

    # Func for edit database table Teachers
    def teachers_win(self):
        self.ui.widget_roster.hide()
        self.ui.widget_teachers.show()
        self.load_db_teachers()

    # Func for edit database table Teachers
    def groups_win(self):
        self.ui.widget_roster.hide()
        self.ui.widget_groups.show()
        self.load_db_groups()

    # Func for setup all buttons
    def setup_buttons_funcs(self):
        # Func for print docs
        def print_doc(filepath, filename):
            f = '"' + filepath + filename + '"'
            win32api.ShellExecute(0, "printto", f, '"%s"' % win32print.GetDefaultPrinter(), ".", 0)

        # But for notes
        def notes_checked():
            notes_list = self.ui.sAWContent_notes.children()
            _set_doc_warning = 1
            for i in notes_list:
                if i.objectName() == 'vL_sAWContent_notes':
                    pass
                else:
                    if i.isChecked():
                        print_doc(os.path.abspath(os.curdir) + r'/Документы/Записки/', i.text() + '.docx')
                        _set_doc_warning = 0
                        break
                    else:
                        _set_doc_warning = 1
            if _set_doc_warning:
                set_doc_warning("Ошибка (не выбран документ для печати)",
                                'Сначала выберите документ для печати.\n\nНажмите на нужный документ, '
                                'чтобы выбрать его, а потом нажмите на кнопку "Печать"')

        # But for decree
        def decree_checked():
            decree_list = self.ui.sAWContent_decree.children()
            _set_doc_warning = 1
            for i in decree_list:
                if i.objectName() == 'vL_sAWContent_decree':
                    pass
                else:
                    if i.isChecked():
                        print_doc(os.path.abspath(os.curdir) + r'/Документы/Приказы/', i.text() + '.docx')
                        _set_doc_warning = 0
                        break
                    else:
                        _set_doc_warning = 1
            if _set_doc_warning:
                set_doc_warning("Ошибка (не выбран документ для печати)",
                                'Сначала выберите документ для печати.\n\nНажмите на нужный документ, '
                                'чтобы выбрать его, а потом нажмите на кнопку "Печать"')

        # But for timetable ПОЗЖЕ НЕ ЗАБЫТЬ БЫ :D
        # def timetable_checked():
        #     pass

        # But for notes
        def headers_control_db(type_post):
            headers_list = self.head_ui.sAWContent_headers_list.children()
            _set_doc_warning = 1
            headers_selected = ''
            if type_post == 'save':
                for i in headers_list:
                    if i.objectName() == 'vL_sAWContent_headers_list':
                        pass
                    else:
                        if i.isChecked():
                            headers_selected = i.objectName().split('_')[-1]
                            _set_doc_warning = 0
                            break
                        else:
                            _set_doc_warning = 1
                if _set_doc_warning:
                    set_doc_warning("Ошибка (не выбрана запись для изменения)",
                                    'Сначала выберите запись для изменения.\n\nНажмите на нужную запись, '
                                    'чтобы выбрать ее, измените ее содержимое, а потом нажмите на кнопку '
                                    '"Сохранить в выбранную запись"')
                else:
                    _db = ARMDataBase()
                    _sql = "UPDATE headers SET " \
                           "head_name = '{0}', " \
                           "head_phone = '{1}', " \
                           "head_mail = '{2}', " \
                           "head_web = '{3}', " \
                           "head_prof = '{4}' " \
                           "WHERE id_head = '{5}'".format(self.head_ui.textEdit_headers_fullname.toPlainText(),
                                                          self.head_ui.textEdit_headers_phone.toPlainText(),
                                                          self.head_ui.textEdit_headers_mail.toPlainText(),
                                                          self.head_ui.textEdit_headers_web.toPlainText(),
                                                          self.head_ui.textEdit_headers_prof.toPlainText(),
                                                          headers_selected)
                    _db.query(_sql)
                    self.load_db_headers()
            elif type_post == 'add':
                _db = ARMDataBase()
                _sql = "INSERT INTO headers VALUES(" \
                       "NULL," \
                       "'{0}'," \
                       "'{1}'," \
                       "'{2}'," \
                       "'{3}'," \
                       "'{4}')".format(self.head_ui.textEdit_headers_fullname.toPlainText(),
                                       self.head_ui.textEdit_headers_phone.toPlainText(),
                                       self.head_ui.textEdit_headers_mail.toPlainText(),
                                       self.head_ui.textEdit_headers_web.toPlainText(),
                                       self.head_ui.textEdit_headers_prof.toPlainText())
                _db.query(_sql)
                self.load_db_headers()
            elif type_post == "del":
                for i in headers_list:
                    if i.objectName() == 'vL_sAWContent_headers_list':
                        pass
                    else:
                        if i.isChecked():
                            headers_selected = i.objectName().split('_')[-1]
                            _set_doc_warning = 0
                            break
                        else:
                            _set_doc_warning = 1
                if _set_doc_warning:
                    set_doc_warning("Ошибка (не выбрана запись для удаления)",
                                    'Сначала выберите запись для удаления.\n\nНажмите на нужную запись, '
                                    'чтобы выбрать ее, а потом нажмите на кнопку '
                                    '"Удалить выбранную запись"')
                else:
                    _db = ARMDataBase()
                    _sql = "DELETE FROM headers WHERE id_head={0}".format(headers_selected)
                    _db.query(_sql)
                    self.load_db_headers()

        def programs_control_db(type_post):
            programs_list = self.prog_ui.sAWContent_programs_list.children()
            _set_doc_warning = 1
            programs_selected = ''
            if type_post == 'save':
                for i in programs_list:
                    if i.objectName() == 'vL_sAWContent_programs_list':
                        pass
                    else:
                        if i.isChecked():
                            programs_selected = i.objectName().split('_')[-1]
                            _set_doc_warning = 0
                            break
                        else:
                            _set_doc_warning = 1
                if _set_doc_warning:
                    set_doc_warning("Ошибка (не выбрана запись для изменения)",
                                    'Сначала выберите запись для изменения.\n\nНажмите на нужную запись, '
                                    'чтобы выбрать ее, измените ее содержимое, а потом нажмите на кнопку '
                                    '"Сохранить в выбранную запись"')
                else:
                    _db = ARMDataBase()
                    _sql = "UPDATE programs SET " \
                           "prog_name = '{0}', " \
                           "prog_range = '{1}' " \
                           "WHERE id_prog = '{2}'".format(self.prog_ui.textEdit_prog_name.toPlainText(),
                                                          self.prog_ui.textEdit_prog_range.toPlainText(),
                                                          programs_selected)
                    _db.query(_sql)
                    self.load_db_programs()
            elif type_post == 'add':
                _db = ARMDataBase()
                _sql = "INSERT INTO programs VALUES(" \
                       "NULL," \
                       "'{0}'," \
                       "'{1}')".format(self.prog_ui.textEdit_prog_name.toPlainText(),
                                       self.prog_ui.textEdit_prog_range.toPlainText())
                _db.query(_sql)
                self.load_db_programs()
            elif type_post == "del":
                for i in programs_list:
                    if i.objectName() == 'vL_sAWContent_programs_list':
                        pass
                    else:
                        if i.isChecked():
                            programs_selected = i.objectName().split('_')[-1]
                            _set_doc_warning = 0
                            break
                        else:
                            _set_doc_warning = 1
                if _set_doc_warning:
                    set_doc_warning("Ошибка (не выбрана запись для удаления)",
                                    'Сначала выберите запись для удаления.\n\nНажмите на нужную запись, '
                                    'чтобы выбрать ее, а потом нажмите на кнопку '
                                    '"Удалить выбранную запись"')
                else:
                    _db = ARMDataBase()
                    _sql = "DELETE FROM programs WHERE id_prog={0}".format(programs_selected)
                    _db.query(_sql)
                    self.load_db_programs()

        def teachers_control_db(type_post):
            teachers_list = self.teach_ui.sAWContent_teachers_list.children()
            _set_doc_warning = 1
            teachers_selected = ''
            if type_post == 'save':
                for i in teachers_list:
                    if i.objectName() == 'vL_sAWContent_teachers_list':
                        pass
                    else:
                        if i.isChecked():
                            teachers_selected = i.objectName().split('_')[-1]
                            _set_doc_warning = 0
                            break
                        else:
                            _set_doc_warning = 1
                if _set_doc_warning:
                    set_doc_warning("Ошибка (не выбрана запись для изменения)",
                                    'Сначала выберите запись для изменения.\n\nНажмите на нужную запись, '
                                    'чтобы выбрать ее, измените ее содержимое, а потом нажмите на кнопку '
                                    '"Сохранить в выбранную запись"')
                else:
                    _db = ARMDataBase()
                    _sql = "UPDATE teachers SET " \
                           "teach_name = '{0}', " \
                           "teach_phone = '{1}', " \
                           "teach_mail = '{2}', " \
                           "teach_web = '{3}', " \
                           "teach_prof = '{4}' " \
                           "WHERE id_teach = '{5}'".format(self.teach_ui.textEdit_teachers_fullname.toPlainText(),
                                                           self.teach_ui.textEdit_teachers_phone.toPlainText(),
                                                           self.teach_ui.textEdit_teachers_mail.toPlainText(),
                                                           self.teach_ui.textEdit_teachers_web.toPlainText(),
                                                           self.teach_ui.textEdit_teachers_prof.toPlainText(),
                                                           teachers_selected)
                    _db.query(_sql)
                    self.load_db_teachers()
            elif type_post == 'add':
                _db = ARMDataBase()
                _sql = "INSERT INTO teachers VALUES(" \
                       "NULL," \
                       "'{0}'," \
                       "'{1}'," \
                       "'{2}'," \
                       "'{3}'," \
                       "'{4}')".format(self.teach_ui.textEdit_teachers_fullname.toPlainText(),
                                       self.teach_ui.textEdit_teachers_phone.toPlainText(),
                                       self.teach_ui.textEdit_teachers_mail.toPlainText(),
                                       self.teach_ui.textEdit_teachers_web.toPlainText(),
                                       self.teach_ui.textEdit_teachers_prof.toPlainText())
                _db.query(_sql)
                self.load_db_teachers()
            elif type_post == "del":
                for i in teachers_list:
                    if i.objectName() == 'vL_sAWContent_teachers_list':
                        pass
                    else:
                        if i.isChecked():
                            teachers_selected = i.objectName().split('_')[-1]
                            _set_doc_warning = 0
                            break
                        else:
                            _set_doc_warning = 1
                if _set_doc_warning:
                    set_doc_warning("Ошибка (не выбрана запись для удаления)",
                                    'Сначала выберите запись для удаления.\n\nНажмите на нужную запись, '
                                    'чтобы выбрать ее, а потом нажмите на кнопку '
                                    '"Удалить выбранную запись"')
                else:
                    _db = ARMDataBase()
                    _sql = "DELETE FROM teachers WHERE id_teach={0}".format(teachers_selected)
                    _db.query(_sql)
                    self.load_db_teachers()

        def groups_control_db(type_post):
            groups_list = self.groups_ui.sAWContent_groups_list.children()
            _set_doc_warning = 1
            groups_selected = ''
            if type_post == 'save':
                for i in groups_list:
                    if i.objectName() == 'vL_sAWContent_groups_list':
                        pass
                    else:
                        if i.isChecked():
                            groups_selected = i.objectName().split('_')[-1]
                            _set_doc_warning = 0
                            break
                        else:
                            _set_doc_warning = 1
                if _set_doc_warning:
                    set_doc_warning("Ошибка (не выбрана запись для изменения)",
                                    'Сначала выберите запись для изменения.\n\nНажмите на нужную запись, '
                                    'чтобы выбрать ее, измените ее содержимое, а потом нажмите на кнопку '
                                    '"Сохранить в выбранную запись"')
                else:
                    _db = ARMDataBase()
                    _sql = "UPDATE groups SET " \
                           "group_name = '{0}', " \
                           "class = '{1}', " \
                           "id_prog = '{2}' " \
                           "WHERE id_group = '{3}'".format(self.groups_ui.textEdit_groups_name.toPlainText(),
                                                           self.groups_ui.textEdit_groups_class.toPlainText(),
                                                           str(self.groups_ui.comboBox_groups_numprog.currentData()),
                                                           groups_selected)
                    _db.query(_sql)
                    self.load_db_groups()
            elif type_post == 'add':
                _db = ARMDataBase()
                _sql = "INSERT INTO groups VALUES(" \
                       "NULL," \
                       "'{0}'," \
                       "'{1}'," \
                       "'{2}')".format(self.groups_ui.textEdit_groups_class.toPlainText(),
                                       self.groups_ui.textEdit_groups_name.toPlainText(),
                                       str(self.groups_ui.comboBox_groups_numprog.currentData()))
                _db.query(_sql)
                self.load_db_groups()
            elif type_post == "del":
                for i in groups_list:
                    if i.objectName() == 'vL_sAWContent_groups_list':
                        pass
                    else:
                        if i.isChecked():
                            groups_selected = i.objectName().split('_')[-1]
                            _set_doc_warning = 0
                            break
                        else:
                            _set_doc_warning = 1
                if _set_doc_warning:
                    set_doc_warning("Ошибка (не выбрана запись для удаления)",
                                    'Сначала выберите запись для удаления.\n\nНажмите на нужную запись, '
                                    'чтобы выбрать ее, а потом нажмите на кнопку '
                                    '"Удалить выбранную запись"')
                else:
                    _db = ARMDataBase()
                    _sql = "DELETE FROM groups WHERE id_group={0}".format(groups_selected)
                    _db.query(_sql)
                    self.load_db_groups()

        def headers_back():
            self.ui.widget_headers.hide()
            self.ui.widget_roster.show()

        def programs_back():
            self.ui.widget_programs.hide()
            self.ui.widget_roster.show()

        def teachers_back():
            self.ui.widget_teachers.hide()
            self.ui.widget_roster.show()

        def groups_back():
            self.ui.widget_groups.hide()
            self.ui.widget_roster.show()

        # Setup buts
        self.ui.pushButton_print_notes.clicked.connect(lambda: notes_checked())
        self.ui.pushButton_print_decree.clicked.connect(lambda: decree_checked())

        self.ui.pushButton_headers_roster.clicked.connect(lambda: self.headers_win())
        self.ui.pushButton_programs_roster.clicked.connect(lambda: self.programs_win())
        self.ui.pushButton_teachers_roster.clicked.connect(lambda: self.teachers_win())
        self.ui.pushButton_groups_roster.clicked.connect(lambda: self.groups_win())

        self.head_ui.pushButton_headers_add.clicked.connect(lambda: headers_control_db('add'))
        self.head_ui.pushButton_headers_save.clicked.connect(lambda: headers_control_db('save'))
        self.head_ui.pushButton_headers_delete.clicked.connect(lambda: headers_control_db('del'))
        self.head_ui.pushButton_headers_back.clicked.connect(lambda: headers_back())
        self.head_ui.lineEdit_search_headers.textEdited.connect(
            lambda: self.load_db_headers(self.head_ui.lineEdit_search_headers.text()))

        self.prog_ui.pushButton_programs_add.clicked.connect(lambda: programs_control_db('add'))
        self.prog_ui.pushButton_programs_save.clicked.connect(lambda: programs_control_db('save'))
        self.prog_ui.pushButton_programs_delete.clicked.connect(lambda: programs_control_db('del'))
        self.prog_ui.pushButton_programs_back.clicked.connect(lambda: programs_back())
        self.prog_ui.lineEdit_search_programs.textEdited.connect(
            lambda: self.load_db_programs(self.prog_ui.lineEdit_search_programs.text()))

        self.teach_ui.pushButton_teachers_add.clicked.connect(lambda: teachers_control_db('add'))
        self.teach_ui.pushButton_teachers_save.clicked.connect(lambda: teachers_control_db('save'))
        self.teach_ui.pushButton_teachers_delete.clicked.connect(lambda: teachers_control_db('del'))
        self.teach_ui.pushButton_teachers_back.clicked.connect(lambda: teachers_back())
        self.teach_ui.lineEdit_search_teachers.textEdited.connect(
            lambda: self.load_db_teachers(self.teach_ui.lineEdit_search_teachers.text()))

        self.groups_ui.pushButton_groups_add.clicked.connect(lambda: groups_control_db('add'))
        self.groups_ui.pushButton_groups_save.clicked.connect(lambda: groups_control_db('save'))
        self.groups_ui.pushButton_groups_delete.clicked.connect(lambda: groups_control_db('del'))
        self.groups_ui.pushButton_groups_back.clicked.connect(lambda: groups_back())
        self.groups_ui.lineEdit_search_groups.textEdited.connect(
            lambda: self.load_db_groups(self.groups_ui.lineEdit_search_groups.text()))

    def clear_for_start(self):
        self.ui.widget_headers.hide()
        self.ui.widget_programs.hide()
        self.ui.widget_teachers.hide()
        self.ui.widget_groups.hide()

    def load_for_start(self):
        notes_list = os.listdir(os.path.abspath(os.curdir) + r'/Документы/Записки/')
        decree_list = os.listdir(os.path.abspath(os.curdir) + r'/Документы/Приказы/')

        def load_docx(list_docx, p, docx_name):
            for docx in list_docx:
                pos1 = docx.find('№')
                pos2 = docx.find('.')
                doc_id = docx[pos1 + 1:pos2]
                self.create_list_el("clb_" + docx_name + doc_id, docx[:-5], p)

        # Loading doc's for lists with doc's
        load_docx(notes_list, self.ui.sAWContent_notes, 'decree_')
        load_docx(decree_list, self.ui.sAWContent_decree, 'note_')
        # Add normal icon
        self.ui.icon = QtGui.QIcon()
        self.ui.icon.addPixmap(QtGui.QPixmap("sfu_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(self.ui.icon)

    # create_list_el('Здесь objectName для кнопки',
    #                     'Здесь текст, который будет показан',
    #                     'Родительский элемент, с которым будет работа')
    def create_list_el(self, name, text, ls):
        a = QtWidgets.QCommandLinkButton(ls)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        a.setFont(font)
        a.setCheckable(True)
        a.setChecked(False)
        a.setAutoExclusive(True)
        a.setAutoDefault(False)
        a.setDefault(False)
        a.setObjectName(name)
        ls_Layout = ls.children()[0]
        ls_Layout.addWidget(a)
        a.setText(self._translate("MainWindow", text))
        return a

    def create_combo_box_el(self, ls, index, text):
        ls.addItem(text, index)
        return ls

    # Loader database for header
    def load_db_headers(self, search_text=None):
        clear_list(self.head_ui.sAWContent_headers_list.children())

        def loader_headers_edits():
            selected_header = ''
            headers_list = self.head_ui.sAWContent_headers_list.children()
            if len(headers_list) != 2:
                for head in headers_list:
                    if head.objectName() != 'vL_sAWContent_headers_list':
                        if head.isChecked():
                            selected_header = head.objectName().split('_')[-1]
                            break
            else:
                selected_header = self.head_ui.sAWContent_headers_list.children()[-1].objectName().split('_')[-1]
            _db1 = ARMDataBase()
            _sql1 = "SELECT * FROM headers WHERE id_head=" + selected_header
            _head = _db1.query(_sql1)
            self.head_ui.textEdit_headers_fullname.setText(_head[0][1])
            self.head_ui.textEdit_headers_prof.setText(_head[0][5])

            if _head[0][2] is not None or _head[0][2] != '':
                self.head_ui.textEdit_headers_phone.setText(_head[0][2])
            else:
                self.head_ui.textEdit_headers_phone.setText('')

            if _head[0][3] is not None or _head[0][3] != '':
                self.head_ui.textEdit_headers_mail.setText(_head[0][3])
            else:
                self.head_ui.textEdit_headers_mail.setText('')

            if _head[0][4] is not None or _head[0][4] != '':
                self.head_ui.textEdit_headers_web.setText(_head[0][4])
            else:
                self.head_ui.textEdit_headers_web.setText('')

        _db = ARMDataBase()
        _sql = "SELECT * FROM headers"
        headers = _db.query(_sql)
        head_loader = []
        for i in range(len(headers)):
            heads = []
            for h in headers[i]:
                heads.append(h)
            head_loader.append(str(heads[0])[:])
            heads[0] = 'clb_head_' + str(heads[0])
            heads[1] = 'ФИО: ' + heads[1] + '\n'
            heads[2] = 'Телефоны: ' + heads[2] + '\n' if heads[2] is not None or heads[2] != '' else ''
            heads[3] = 'Электронные почты: ' + heads[3] + '\n' if heads[3] is not None or heads[3] != '' else ''
            heads[4] = 'Социальные сети: ' + heads[4] + '\n' if heads[4] is not None or heads[4] != '' else ''
            heads[5] = 'Должность: ' + heads[5] + '\n' if heads[5] is not None or heads[5] != '' else ''
            searcher = ''
            _search_text = search_text
            for h in heads:
                if h is not None or h != '':
                    searcher = searcher + h.lower()
            if _search_text is not None and _search_text != '':
                _search_text = search_text.lower()
                if _search_text in searcher:
                    head_but = self.create_list_el(heads[0],
                                                   heads[1] + heads[5] + heads[2] + heads[3] + heads[4],
                                                   self.head_ui.sAWContent_headers_list)
                    head_but.clicked.connect(lambda: loader_headers_edits())
            else:
                head_but = self.create_list_el(heads[0],
                                               heads[1] + heads[5] + heads[2] + heads[3] + heads[4],
                                               self.head_ui.sAWContent_headers_list)
                head_but.clicked.connect(lambda: loader_headers_edits())

    # Loader database for programs
    def load_db_programs(self, search_text=None):
        clear_list(self.prog_ui.sAWContent_programs_list.children())

        def loader_programs_edits():
            selected_program = ''
            programs_list = self.prog_ui.sAWContent_programs_list.children()
            if len(programs_list) != 2:
                for prog in programs_list:
                    if prog.objectName() != 'vL_sAWContent_programs_list':
                        if prog.isChecked():
                            selected_program = prog.objectName().split('_')[-1]
                            break
            else:
                selected_program = self.prog_ui.sAWContent_programs_list.children()[-1].objectName().split('_')[-1]
            _db1 = ARMDataBase()
            _sql1 = "SELECT * FROM programs WHERE id_prog=" + selected_program
            _prog = _db1.query(_sql1)
            self.prog_ui.textEdit_prog_name.setText(_prog[0][1])
            self.prog_ui.textEdit_prog_range.setText(_prog[0][2])

            if _prog[0][2] is not None or _prog[0][2] != '':
                self.head_ui.textEdit_headers_phone.setText(_prog[0][2])
            else:
                self.head_ui.textEdit_headers_phone.setText('')

        _db = ARMDataBase()
        _sql = "SELECT * FROM programs"
        programs = _db.query(_sql)
        prog_loader = []
        for i in range(len(programs)):
            progs = []
            for h in programs[i]:
                progs.append(h)
            prog_loader.append(str(progs[0])[:])
            progs[0] = 'clb_prog_' + str(progs[0])
            progs[1] = 'Программа: ' + progs[1] + '\n'
            progs[2] = 'Продолжительность: в течении ' + progs[2] + '-х месяцев\n' if progs[2] is not None or progs[
                2] != '' else ''
            searcher = ''
            _search_text = search_text
            for h in progs:
                if h is not None or h != '':
                    searcher = searcher + h.lower()
            if _search_text is not None and _search_text != '':
                _search_text = search_text.lower()
                if _search_text in searcher:
                    prog_but = self.create_list_el(progs[0],
                                                   progs[1] + progs[2],
                                                   self.prog_ui.sAWContent_programs_list)
                    prog_but.clicked.connect(lambda: loader_programs_edits())
            else:
                prog_but = self.create_list_el(progs[0],
                                               progs[1] + progs[2],
                                               self.prog_ui.sAWContent_programs_list)
                prog_but.clicked.connect(lambda: loader_programs_edits())

    # Loader database for teachers
    def load_db_teachers(self, search_text=None):
        clear_list(self.teach_ui.sAWContent_teachers_list.children())

        def loader_teachers_edits():
            selected_teacher = ''
            teachers_list = self.teach_ui.sAWContent_teachers_list.children()
            if len(teachers_list) != 2:
                for teach in teachers_list:
                    if teach.objectName() != 'vL_sAWContent_teachers_list':
                        if teach.isChecked():
                            selected_teacher = teach.objectName().split('_')[-1]
                            break
            else:
                selected_teacher = self.teach_ui.sAWContent_teachers_list.children()[-1].objectName().split('_')[-1]
            _db1 = ARMDataBase()
            _sql1 = "SELECT * FROM teachers WHERE id_teacher=" + selected_teacher
            _teach = _db1.query(_sql1)
            self.teach_ui.textEdit_teachers_fullname.setText(_teach[0][1])
            self.teach_ui.textEdit_teachers_prof.setText(_teach[0][5])

            if _teach[0][2] is not None or _teach[0][2] != '':
                self.teach_ui.textEdit_teachers_phone.setText(_teach[0][2])
            else:
                self.teach_ui.textEdit_teachers_phone.setText('')

            if _teach[0][3] is not None or _teach[0][3] != '':
                self.teach_ui.textEdit_teachers_mail.setText(_teach[0][3])
            else:
                self.teach_ui.textEdit_teachers_mail.setText('')

            if _teach[0][4] is not None or _teach[0][4] != '':
                self.teach_ui.textEdit_teachers_web.setText(_teach[0][4])
            else:
                self.teach_ui.textEdit_teachers_web.setText('')

        _db = ARMDataBase()
        _sql = "SELECT * FROM teachers"
        teachers = _db.query(_sql)
        teach_loader = []
        for i in range(len(teachers)):
            teachs = []
            for h in teachers[i]:
                teachs.append(h)
            teach_loader.append(str(teachs[0])[:])
            teachs[0] = 'clb_teach_' + str(teachs[0])
            teachs[1] = 'ФИО: ' + teachs[1] + '\n'
            teachs[2] = 'Телефоны: ' + teachs[2] + '\n' if teachs[2] is not None or teachs[2] != '' else ''
            teachs[3] = 'Электронные почты: ' + teachs[3] + '\n' if teachs[3] is not None or teachs[3] != '' else ''
            teachs[4] = 'Социальные сети: ' + teachs[4] + '\n' if teachs[4] is not None or teachs[4] != '' else ''
            teachs[5] = 'Должность: ' + teachs[5] + '\n' if teachs[5] is not None or teachs[5] != '' else ''
            searcher = ''
            _search_text = search_text
            for h in teachs:
                if h is not None or h != '':
                    searcher = searcher + h.lower()
            if _search_text is not None and _search_text != '':
                _search_text = search_text.lower()
                if _search_text in searcher:
                    teach_but = self.create_list_el(teachs[0],
                                                    teachs[1] + teachs[5] + teachs[2] + teachs[3] + teachs[4],
                                                    self.teach_ui.sAWContent_teachers_list)
                    teach_but.clicked.connect(lambda: loader_teachers_edits())
            else:
                teach_but = self.create_list_el(teachs[0],
                                                teachs[1] + teachs[5] + teachs[2] + teachs[3] + teachs[4],
                                                self.teach_ui.sAWContent_teachers_list)
                teach_but.clicked.connect(lambda: loader_teachers_edits())

    # Loader database for groups
    def load_db_groups(self, search_text=None):
        clear_list(self.groups_ui.sAWContent_groups_list.children())

        def loader_groups_edits():
            selected_group = ''
            groups_list = self.groups_ui.sAWContent_groups_list.children()
            if len(groups_list) != 2:
                for grp in groups_list:
                    if grp.objectName() != 'vL_sAWContent_groups_list':
                        if grp.isChecked():
                            selected_group = grp.objectName().split('_')[-1]
                            break
            else:
                selected_group = self.groups_ui.sAWContent_groups_list.children()[-1].objectName().split('_')[-1]
            _db1 = ARMDataBase()
            _sql1 = "SELECT * FROM groups WHERE id_group=" + selected_group
            _grp = _db1.query(_sql1)
            self.groups_ui.textEdit_groups_name.setText(_grp[0][2])
            self.groups_ui.comboBox_groups_numprog.setCurrentIndex(
                self.groups_ui.comboBox_groups_numprog.findData(_grp[0][3]))
            if _grp[0][2] is not None or _grp[0][2] != '':
                self.groups_ui.textEdit_groups_class.setText(_grp[0][1])
            else:
                self.groups_ui.textEdit_groups_class.setText('')

        _db = ARMDataBase()
        _sql = "SELECT * FROM groups"
        groups = _db.query(_sql)
        grp_loader = []
        for i in range(len(groups)):
            grps = []
            for h in groups[i]:
                grps.append(h)
            grp_loader.append(str(grps[0])[:])

            _db = ARMDataBase()
            _sql = "SELECT prog_name FROM programs WHERE id_prog=" + str(grps[3])
            group_prog = _db.query(_sql)

            grps[0] = 'clb_grp_' + str(grps[0])
            grps[1] = 'Класс: ' + grps[1] + '\n' if grps[1] is not None or grps[1] != '' else ''
            grps[2] = 'Группа: ' + grps[2] + '\n'
            grps[3] = 'Программа: ' + group_prog[0][0] + '\n' if group_prog[0][0] is not None or group_prog[0][
                0] != '' else ''
            searcher = ''
            _search_text = search_text
            for h in grps:
                if h is not None or h != '':
                    searcher = searcher + h.lower()
            if _search_text is not None and _search_text != '':
                _search_text = search_text.lower()
                if _search_text in searcher:
                    grp_but = self.create_list_el(grps[0],
                                                  grps[2] + grps[3] + grps[1],
                                                  self.groups_ui.sAWContent_groups_list)
                    grp_but.clicked.connect(lambda: loader_groups_edits())
            else:
                grp_but = self.create_list_el(grps[0],
                                              grps[2] + grps[3] + grps[1],
                                              self.groups_ui.sAWContent_groups_list)
                grp_but.clicked.connect(lambda: loader_groups_edits())

        _db = ARMDataBase()
        _sql = "SELECT * FROM programs"
        programs = _db.query(_sql)
        _programs = []

        self.groups_ui.comboBox_groups_numprog.clear()
        for prog in programs:
            self.create_combo_box_el(self.groups_ui.comboBox_groups_numprog, prog[0], str(prog[1]))


# Clearing edit list
def clear_list(children_list):
    for i in children_list:
        if i.objectName().startswith('clb_'):
            i.setAttribute(55, 1)
            i.close()


# Func for warning
def set_doc_warning(war_name, war_text, war_icon="sfu_logo.ico"):
    _set_doc_warning = QMessageBox()
    _set_doc_warning.setWindowTitle(war_name)
    _set_doc_warning.setText(war_text)
    _set_doc_warning.setIcon(QMessageBox.Warning)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(war_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    _set_doc_warning.setWindowIcon(icon)
    _set_doc_warning.exec_()


# Func for main window start
def main_win_start():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


# Main func
def main():
    main_win_start()


# Start application if her main
if __name__ == "__main__":
    main()
