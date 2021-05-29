import copy
import threading
import time
import sys
import os
import win32api
import win32print
import datetime
import docx

from ui import *
from headers_ui import *
from programs_ui import *
from teachers_ui import *
from groups_ui import *
from subjects_ui import *
from students_ui import *
from enrollment_ui import *
from outlay_ui import *
from timetable_edit_ui import *
from outlay_printer_ui import *
from arm_db import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.table import _Cell


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

        self.ui.widget_subjects = QtWidgets.QWidget(self.ui.widget_roster_editors)
        self.ui.hL_widget_roster_editors.addWidget(self.ui.widget_subjects)
        self.sub_ui = Ui_Subjects()
        self.sub_ui.setupUi(self.ui.widget_subjects)

        self.ui.widget_students = QtWidgets.QWidget(self.ui.widget_roster_editors)
        self.ui.hL_widget_roster_editors.addWidget(self.ui.widget_students)
        self.stud_ui = Ui_Students()
        self.stud_ui.setupUi(self.ui.widget_students)

        self.ui.widget_outlay = QtWidgets.QWidget(self.ui.widget_roster_editors)
        self.ui.hL_widget_roster_editors.addWidget(self.ui.widget_outlay)
        self.outlay_ui = Ui_Outlay()
        self.outlay_ui.setupUi(self.ui.widget_outlay)

        self.ui.widget_enrollment = QtWidgets.QWidget(self.ui.widget_roster_editors)
        self.ui.hL_widget_roster_editors.addWidget(self.ui.widget_enrollment)
        self.enr_ui = Ui_Enrollment()
        self.enr_ui.setupUi(self.ui.widget_enrollment)

        self.ttable = QtWidgets.QDialog(self)
        self.ttable_ui = Ui_TTableEditor()
        self.ttable_ui.setupUi(self.ttable)
        self.ttable.setWindowTitle('Редактор расписания')

        self.ttable_selected_sub = ''
        self.ttable_list = []

        self.outlay_printer = QtWidgets.QDialog(self)
        self.outpr_ui = Ui_OutlayPrinter()
        self.outpr_ui.setupUi(self.outlay_printer)
        self.outlay_printer.setWindowTitle('Редактор сметы')
        self.outlay_data = []

        self.disk_dir = os.getenv("SystemDrive")
        self.user = os.environ.get("USERNAME")
        self.dir = os.path.abspath(os.curdir)
        self.clear_for_start()
        self.setup_buttons_funcs()
        self.load_for_start()
        self.resize(1000, 885)

        # MAIN END

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

    # Func for edit database table Groups
    def groups_win(self):
        self.ui.widget_roster.hide()
        self.ui.widget_groups.show()
        self.load_db_groups()

    # Func for edit database table Subjects
    def subjects_win(self):
        self.ui.widget_roster.hide()
        self.ui.widget_subjects.show()
        self.load_db_subjects()

    # Func for edit database table Students
    def students_win(self):
        self.ui.widget_roster.hide()
        self.ui.widget_students.show()
        self.load_db_students()

    # Func for edit database table Enrollment
    def enrollment_win(self):
        self.ui.widget_roster.hide()
        self.ui.widget_enrollment.show()
        self.load_db_enrollment()

    # Func for edit database table Outlay
    def outlay_win(self):
        self.ui.widget_roster.hide()
        self.ui.widget_outlay.show()
        self.load_db_outlay()

    # Func for setup all buttons
    def setup_buttons_funcs(self):
        # But for notes
        def notes_print():
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
        def decree_print():
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

        # But for timetable
        def timetable_print():
            timetable_list = self.ui.sAWContent_timetable.children()
            _set_doc_warning = 1
            for i in timetable_list:
                if i.objectName().startswith("clb_"):
                    if i.isChecked():
                        create_timetable(i.objectName().split("_")[-1])
                        _set_doc_warning = 0
                        break
                    else:
                        _set_doc_warning = 1
            if _set_doc_warning:
                set_doc_warning("Ошибка (не выбрано расписание для сохранения)",
                                'Сначала выберите расписание для сохранения.\n\nНажмите на нужное расписание, '
                                'чтобы выбрать его, а потом нажмите на кнопку "Сохранить как документ"')
            else:
                set_doc_warning("Отправлено",
                                'Документ будет сохранен в прочие документы.')

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
                    _db.close()
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
                _db.close()
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
                    _db.close()
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
                           "prog_range = '{1}', " \
                           "prog_range_dates = '{2}' " \
                           "WHERE id_prog = '{3}'".format(self.prog_ui.textEdit_prog_name.toPlainText(),
                                                          self.prog_ui.textEdit_prog_range.toPlainText(),
                                                          self.prog_ui.dateEdit_start_program.date().
                                                          toString('dd.MM.yyyy')
                                                          + "|" +
                                                          self.prog_ui.dateEdit_end_program.date().
                                                          toString('dd.MM.yyyy'),
                                                          programs_selected)
                    _db.query(_sql)
                    _db.close()
                    self.load_db_programs()
            elif type_post == 'add':
                _db = ARMDataBase()
                _sql = "INSERT INTO programs VALUES(" \
                       "NULL," \
                       "'{0}'," \
                       "'{1}'," \
                       "'{2}')".format(self.prog_ui.textEdit_prog_name.toPlainText(),
                                       self.prog_ui.textEdit_prog_range.toPlainText(),
                                       self.prog_ui.dateEdit_start_program.date().
                                       toString('dd.MM.yyyy')
                                       + "|" +
                                       self.prog_ui.dateEdit_end_program.date().
                                       toString('dd.MM.yyyy'))
                _db.query(_sql)
                _db.close()
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
                    _sql = "SELECT id_group FROM groups WHERE id_prog=" + programs_selected
                    groups = _db.query(_sql)
                    for group in groups:
                        _sql = "SELECT id_student FROM students WHERE id_group=" + groups_selected
                        studs = _db.query(_sql)
                        for stud in studs:
                            _sql = "UPDATE subs_in_studs SET status='0' WHERE id_student=" + stud[0]
                            _db.query(_sql)
                    _sql = "UPDATE groups SET id_prog='8' WHERE id_prog=" + programs_selected
                    _db.query(_sql)
                    _sql = "UPDATE subjects SET id_prog='8' WHERE id_prog=" + programs_selected
                    _db.query(_sql)
                    _sql = "DELETE FROM programs WHERE id_prog={0}".format(programs_selected)
                    _db.query(_sql)
                    _db.close()
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
                    _db.close()
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
                _db.close()
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
                    _sql = "DELETE FROM teachers WHERE id_teacher={0}".format(teachers_selected)
                    _db.query(_sql)
                    _db.close()
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
                    _sql = "SELECT id_prog FROM groups WHERE id_group=" + groups_selected
                    prog_checker = str(_db.query(_sql)[0][0])
                    if prog_checker != str(self.groups_ui.comboBox_groups_prog.currentData()):
                        _sql = "SELECT id_student FROM students WHERE id_group=" + groups_selected
                        studs = _db.query(_sql)
                        for stud in studs:
                            _sql = "UPDATE subs_in_studs SET status='0' WHERE id_student=" + stud[0]
                            _db.query(_sql)
                    _sql = "UPDATE groups SET " \
                           "group_name = '{0}', " \
                           "class = '{1}', " \
                           "id_prog = '{2}' " \
                           "WHERE id_group = '{3}'".format(self.groups_ui.textEdit_groups_name.toPlainText(),
                                                           self.groups_ui.textEdit_groups_class.toPlainText(),
                                                           str(self.groups_ui.comboBox_groups_prog.currentData()),
                                                           groups_selected)
                    _db.query(_sql)
                    _db.close()
                    self.load_db_groups()
            elif type_post == 'add':
                _db = ARMDataBase()
                _sql = "INSERT INTO groups VALUES(" \
                       "NULL," \
                       "'{0}'," \
                       "'{1}'," \
                       "'{2}')".format(self.groups_ui.textEdit_groups_class.toPlainText(),
                                       self.groups_ui.textEdit_groups_name.toPlainText(),
                                       str(self.groups_ui.comboBox_groups_prog.currentData()))
                _db.query(_sql)
                _db.close()
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
                    _sql = "SELECT id_student FROM students WHERE id_group=" + groups_selected
                    studs = _db.query(_sql)
                    for stud in studs:
                        _sql = "UPDATE students SET id_group='1' WHERE id_student=" + stud[0]
                        _db.query(_sql)
                        _sql = "UPDATE subs_in_studs SET status='0' WHERE id_student=" + stud[0]
                        _db.query(_sql)
                    _sql = "DELETE FROM groups WHERE id_group={0}".format(groups_selected)
                    _db.query(_sql)
                    _db.close()
                    self.load_db_groups()

        def subjects_control_db(type_post):
            subjects_list = self.sub_ui.sAWContent_sub_list.children()
            _set_doc_warning = 1
            subjects_selected = ''
            if type_post == 'save':
                for i in subjects_list:
                    if i.objectName() == 'vL_sAWContent_sub_list':
                        pass
                    else:
                        if i.isChecked():
                            subjects_selected = i.objectName().split('_')[-1]
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
                    _sql = "SELECT id_prog FROM subjects WHERE id_sub=" + subjects_selected
                    prog_checker = str(_db.query(_sql)[0][0])
                    if prog_checker != str(self.sub_ui.comboBox_sub_prog.currentData()):
                        _sql = "UPDATE subs_in_studs SET status='0' WHERE id_sub=" + subjects_selected
                        _db.query(_sql)
                    _sql = "UPDATE subjects SET " \
                           "sub_name = '{0}', " \
                           "sub_price_hour = '{1}', " \
                           "id_teacher = '{2}', " \
                           "sub_price_month = '{3}', " \
                           "id_prog = '{4}', " \
                           "sub_hours_need = '{5}' " \
                           "WHERE id_sub = '{6}'".format(self.sub_ui.textEdit_sub_name.toPlainText(),
                                                         self.sub_ui.lineEdit_sub_tax.text(),
                                                         str(self.sub_ui.comboBox_sub_teach.currentData()),
                                                         self.sub_ui.lineEdit_sub_price.text(),
                                                         str(self.sub_ui.comboBox_sub_prog.currentData()),
                                                         self.sub_ui.lineEdit_sub_hours.text(),
                                                         subjects_selected)
                    _db.query(_sql)
                    _db.close()
                    self.load_db_subjects()
            elif type_post == 'add':
                _db = ARMDataBase()
                _sql = "INSERT INTO subjects VALUES(" \
                       "NULL," \
                       "'{0}'," \
                       "'{1}'," \
                       "'{2}'," \
                       "'{3}'," \
                       "'{4}'," \
                       "NULL," \
                       "'0'," \
                       "'{5}')".format(self.sub_ui.textEdit_sub_name.toPlainText(),
                                       self.sub_ui.lineEdit_sub_tax.text(),
                                       str(self.sub_ui.comboBox_sub_teach.currentData()),
                                       self.sub_ui.lineEdit_sub_price.text(),
                                       str(self.sub_ui.comboBox_sub_prog.currentData()),
                                       self.sub_ui.lineEdit_sub_hours.text())
                _db.query(_sql)
                _db.close()
                self.load_db_subjects()
            elif type_post == "del":
                for i in subjects_list:
                    if i.objectName() == 'vL_sAWContent_sub_list':
                        pass
                    else:
                        if i.isChecked():
                            subjects_selected = i.objectName().split('_')[-1]
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
                    _sql = "DELETE FROM subs_in_studs WHERE id_sub=" + subjects_selected
                    _db.query(_sql)
                    _sql = "DELETE FROM subjects WHERE id_sub=" + subjects_selected
                    _db.query(_sql)
                    _db.close()
                    self.load_db_subjects()

        def students_control_db(type_post):
            students_list = self.stud_ui.sAWContent_stud_list.children()
            _set_doc_warning = 1
            students_selected = ''
            if type_post == 'save':
                for i in students_list:
                    if i.objectName() == 'vL_sAWContent_stud_list':
                        pass
                    else:
                        if i.isChecked():
                            students_selected = i.objectName().split('_')[-1]
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
                    gender = 'male' if self.stud_ui.radioButton_stud_gender_male.isChecked() else 'female'
                    _sql = "SELECT id_group FROM students WHERE id_student=" + students_selected
                    group_checker = str(_db.query(_sql)[0][0])
                    if group_checker != str(self.stud_ui.comboBox_stud_group.currentData()):
                        _sql = "UPDATE subs_in_studs SET status='0' WHERE id_student=" + students_selected
                        _db.query(_sql)
                    _sql = "UPDATE students SET " \
                           "student_name = '{0}', " \
                           "id_group = '{1}', " \
                           "student_birthday = '{2}', " \
                           "student_phone = '{3}', " \
                           "student_gender = '{4}', " \
                           "student_city = '{5}', " \
                           "student_einst = '{6}', " \
                           "student_mail = '{7}', " \
                           "student_web = '{8}' " \
                           "WHERE id_student = '{9}'".format(self.stud_ui.textEdit_stud_fullname.toPlainText(),
                                                             str(self.stud_ui.comboBox_stud_group.currentData()),
                                                             self.stud_ui.dateEdit_stud_birthday.date().toString(
                                                                 'dd.MM.yyyy'),
                                                             self.stud_ui.lineEdit_stud_phone.text(),
                                                             gender,
                                                             self.stud_ui.lineEdit_stud_city.text(),
                                                             self.stud_ui.lineEdit_stud_einst.text(),
                                                             self.stud_ui.lineEdit_stud_mail.text(),
                                                             self.stud_ui.lineEdit_stud_web.text(),
                                                             students_selected)
                    _db.query(_sql)
                    _db.close()
                    self.load_db_students()
            elif type_post == 'add':
                gender = 'male' if self.stud_ui.radioButton_stud_gender_male.isChecked() else 'female'
                _db = ARMDataBase()
                _sql = "INSERT INTO students VALUES(" \
                       "NULL," \
                       "'{0}'," \
                       "'{1}'," \
                       "'{2}'," \
                       "'{3}'," \
                       "'{4}'," \
                       "'{5}'," \
                       "'{6}'," \
                       "'{7}'," \
                       "'{8}')".format(self.stud_ui.textEdit_stud_fullname.toPlainText(),
                                       str(self.stud_ui.comboBox_stud_group.currentData()),
                                       self.stud_ui.dateEdit_stud_birthday.date().toString(
                                           'dd.MM.yyyy'),
                                       self.stud_ui.lineEdit_stud_phone.text(),
                                       gender,
                                       self.stud_ui.lineEdit_stud_city.text(),
                                       self.stud_ui.lineEdit_stud_einst.text(),
                                       self.stud_ui.lineEdit_stud_mail.text(),
                                       self.stud_ui.lineEdit_stud_web.text())
                _db.query(_sql)
                _db.close()
                self.load_db_students()
            elif type_post == "del":
                for i in students_list:
                    if i.objectName() == 'vL_sAWContent_stud_list':
                        pass
                    else:
                        if i.isChecked():
                            students_selected = i.objectName().split('_')[-1]
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
                    _sql = "DELETE FROM subs_in_studs WHERE id_student=" + students_selected
                    _db.query(_sql)
                    _sql = "DELETE FROM students WHERE id_student={0}".format(students_selected)
                    _db.query(_sql)
                    _db.close()
                    self.load_db_students()

        def enrollment_control_db():
            _db = ARMDataBase()
            enrollments_list = self.enr_ui.sAWContent_enr_list.children()
            _set_doc_warning = 1
            enrollment_selected = ''
            for i in enrollments_list:
                if i.objectName() == 'vL_sAWContent_enr_list':
                    pass
                else:
                    if i.isChecked():
                        enrollment_selected = i.objectName().split('_')[-1]
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
                for enrollment in self.enr_ui.list_cb_checked:
                    _sql = "SELECT id_sis FROM subs_in_studs WHERE id_student=" + enrollment_selected + " AND id_sub=" + \
                           enrollment[0]
                    check_sis = _db.query(_sql)
                    if check_sis != []:
                        _sql = "UPDATE subs_in_studs SET " \
                               "student_numcontract = '{0}', " \
                               "student_datecontract = '{1}', " \
                               "status = '{2}' " \
                               "WHERE id_sis = '{3}'". \
                            format(self.enr_ui.groupBox_sis_contracts.findChild(QtWidgets.QGroupBox,
                                                                                "grB_" + enrollment[0]).
                                   findChild(QtWidgets.QLineEdit, "ledit_" + "grB_" + enrollment[0]).text(),
                                   self.enr_ui.groupBox_sis_contracts.findChild(QtWidgets.QGroupBox,
                                                                                "grB_" + enrollment[0]).
                                   findChild(QtWidgets.QDateEdit, "dedit_" + "grB_" + enrollment[0]).date().
                                   toString('dd.MM.yyyy'),
                                   "1" if enrollment[1] else "0",
                                   check_sis[0][0])
                    else:
                        if enrollment[1]:
                            _sql = "INSERT INTO subs_in_studs VALUES(" \
                                   "NULL, " \
                                   "'{0}', " \
                                   "'{1}', " \
                                   "'{2}', " \
                                   "'{3}', " \
                                   "'{4}')".format(enrollment_selected,
                                                   enrollment[0],
                                                   self.enr_ui.groupBox_sis_contracts.findChild(QtWidgets.QGroupBox,
                                                                                                "grB_" + enrollment[0]).
                                                   findChild(QtWidgets.QLineEdit,
                                                             "ledit_" + "grB_" + enrollment[0]).text(),
                                                   self.enr_ui.groupBox_sis_contracts.findChild(QtWidgets.QGroupBox,
                                                                                                "grB_" + enrollment[0]).
                                                   findChild(QtWidgets.QDateEdit, "dedit_" + "grB_" + enrollment[0]).
                                                   date().toString('dd.MM.yyyy'),
                                                   "1" if enrollment[1] else "0")
                    _db.query(_sql)
                _db.close()
                self.load_db_enrollment()

        def outlay_control_db():
            self.save_calculate_values()
            self.outlay_ui.calcs_before = len(self.outlay_ui.widget_calcs.children()) - 1
            clear_widget(self.outlay_ui.widget_calcs.children())
            if self.outlay_ui.comboBox_progs.currentData() == "None" or self.outlay_ui.comboBox_progs.currentData() is None:
                self.outlay_ui.widget_col_subs.setEnabled(True)
                rb = 0
                if self.outlay_ui.radio_col_1.isChecked():
                    rb = 1
                elif self.outlay_ui.radio_col_2.isChecked():
                    rb = 2
                elif self.outlay_ui.radio_col_3.isChecked():
                    rb = 3
                elif self.outlay_ui.radio_col_4.isChecked():
                    rb = 4
                for r in range(rb):
                    if r + 1 == 1:
                        self.add_calculate_box(False, str(r + 1), 0, 0)
                    elif r + 1 == 2:
                        self.add_calculate_box(False, str(r + 1), 1, 0)
                    elif r + 1 == 3:
                        self.add_calculate_box(False, str(r + 1), 0, 1)
                    elif r + 1 == 4:
                        self.add_calculate_box(False, str(r + 1), 1, 1)
                self.load_calculate_values()
            else:
                self.outlay_ui.widget_col_subs.setEnabled(False)
                _db = ARMDataBase()
                _sql = "SELECT id_sub FROM subjects WHERE id_prog=" + str(self.outlay_ui.comboBox_progs.currentData())
                subs = _db.query(_sql)
                try:
                    self.outlay_ui.widget_col_subs.findChild(QtWidgets.QRadioButton,
                                                             "radio_col_" + str(len(subs))).setChecked(True)
                except Exception:
                    pass
                _db.close()
                a = 0
                b = 0
                for i in subs:
                    self.add_calculate_box(True, str(i[0]), a, b)
                    if a == 0 and b == 0:
                        a = 1
                        b = 0
                    elif a == 1 and b == 0:
                        a = 0
                        b = 1
                    elif a == 0 and b == 1:
                        a = 1
                        b = 1

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

        def subjects_back():
            self.ui.widget_subjects.hide()
            self.ui.widget_roster.show()

        def students_back():
            self.ui.widget_students.hide()
            self.ui.widget_roster.show()

        def enrollment_back():
            self.ui.widget_enrollment.hide()
            self.ui.widget_roster.show()

        def outlay_back():
            self.ui.widget_outlay.hide()
            self.ui.widget_roster.show()

        # SETUP BUTS
        self.ui.pushButton_print_notes.clicked.connect(lambda: notes_print())
        self.ui.pushButton_print_decree.clicked.connect(lambda: decree_print())
        self.ui.pushButton_print_timetable.clicked.connect(lambda: timetable_print())

        self.ui.pushButton_update_timetable.clicked.connect(
            lambda: self.load_db_timetable(self.ui.lineEdit_search_timetable.text()))
        self.ui.pushButton_edit_timetable.clicked.connect(lambda: self.timetable_list_exec())
        self.ui.lineEdit_search_timetable.textEdited.connect(
            lambda: self.load_db_timetable(self.ui.lineEdit_search_timetable.text()))
        self.ttable_ui.btn_set_hours.clicked.connect(lambda: self.set_hours())
        self.ttable_ui.btn_del_hours.clicked.connect(lambda: self.del_hours())
        self.ttable_ui.calendar.clicked.connect(lambda: self.select_list_el())

        self.ui.pushButton_headers_roster.clicked.connect(lambda: self.headers_win())
        self.ui.pushButton_programs_roster.clicked.connect(lambda: self.programs_win())
        self.ui.pushButton_teachers_roster.clicked.connect(lambda: self.teachers_win())
        self.ui.pushButton_groups_roster.clicked.connect(lambda: self.groups_win())
        self.ui.pushButton_subjects_roster.clicked.connect(lambda: self.subjects_win())
        self.ui.pushButton_students_roster.clicked.connect(lambda: self.students_win())
        self.ui.pushButton_enrollment_roster.clicked.connect(lambda: self.enrollment_win())
        self.ui.pushButton_outlay.clicked.connect(lambda: self.outlay_win())

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

        self.sub_ui.pushButton_sub_add.clicked.connect(lambda: subjects_control_db('add'))
        self.sub_ui.pushButton_sub_save.clicked.connect(lambda: subjects_control_db('save'))
        self.sub_ui.pushButton_sub_delete.clicked.connect(lambda: subjects_control_db('del'))
        self.sub_ui.pushButton_sub_back.clicked.connect(lambda: subjects_back())
        self.sub_ui.lineEdit_search_sub.textEdited.connect(
            lambda: self.load_db_subjects(self.sub_ui.lineEdit_search_sub.text()))

        self.stud_ui.pushButton_stud_add.clicked.connect(lambda: students_control_db('add'))
        self.stud_ui.pushButton_stud_save.clicked.connect(lambda: students_control_db('save'))
        self.stud_ui.pushButton_stud_delete.clicked.connect(lambda: students_control_db('del'))
        self.stud_ui.pushButton_stud_back.clicked.connect(lambda: students_back())
        self.stud_ui.lineEdit_search_stud.textEdited.connect(
            lambda: self.load_db_students(self.stud_ui.lineEdit_search_stud.text()))

        self.enr_ui.pushButton_enr_save.clicked.connect(lambda: enrollment_control_db())
        self.enr_ui.pushButton_enr_back.clicked.connect(lambda: enrollment_back())
        self.enr_ui.lineEdit_search_enr.textEdited.connect(
            lambda: self.load_db_enrollment(self.enr_ui.lineEdit_search_enr.text()))

        self.outlay_ui.pushButton_outlay_back.clicked.connect(lambda: outlay_back())
        self.outlay_ui.comboBox_progs.currentIndexChanged.connect(lambda: outlay_control_db())
        self.outlay_ui.pushButton_outlay_next.clicked.connect(lambda: self.outlay_printer_exec())
        self.outlay_ui.radio_col_1.clicked.connect(lambda: outlay_control_db())
        self.outlay_ui.radio_col_2.clicked.connect(lambda: outlay_control_db())
        self.outlay_ui.radio_col_3.clicked.connect(lambda: outlay_control_db())
        self.outlay_ui.radio_col_4.clicked.connect(lambda: outlay_control_db())
        self.outpr_ui.pushButton_save_doc.clicked.connect(lambda: create_outlay_doc(self.outlay_data))

    # END BUTTONS

    def clear_for_start(self):
        self.ui.widget_headers.hide()
        self.ui.widget_programs.hide()
        self.ui.widget_teachers.hide()
        self.ui.widget_groups.hide()
        self.ui.widget_subjects.hide()
        self.ui.widget_students.hide()
        self.ui.widget_enrollment.hide()
        self.ui.widget_outlay.hide()

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
        self.load_db_timetable()
        # Add normal icon
        self.ui.icon = QtGui.QIcon()
        self.ui.icon.addPixmap(QtGui.QPixmap("sfu_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(self.ui.icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sfu_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ttable.setWindowIcon(icon)
        self.outlay_printer.setWindowIcon(icon)

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
        a.setMinimumSize(len(max(text.split("\n"), key=lambda i: len(i))) * 6 + 100, text.count("\n") * 15 + 40)
        ls_Layout.addWidget(a)
        a.setText(self._translate("MainWindow", text))
        return a

    def create_combo_box_el(self, ls, index, text):
        ls.addItem(text, index)
        return ls

    def create_check_box_el(self, ls, name, text, checked=False):
        cb = QtWidgets.QCheckBox(ls)
        font = QtGui.QFont()
        font.setPointSize(11)
        cb.setFont(font)
        cb.setObjectName(name)
        cb.setChecked(checked)
        ls_Layout = ls.children()[0]
        ls_Layout.addWidget(cb)
        cb.setText(self._translate("MainWindow", text))
        return cb

    def create_sub_groupbox(self, ls, name, text, _hide):
        # GroupBox for Subject
        gb = QtWidgets.QGroupBox(ls)
        font = QtGui.QFont()
        font.setPointSize(11)
        gb.setFont(font)
        gb.setObjectName(name)
        gL_gb = QtWidgets.QGridLayout(gb)
        gL_gb.setObjectName("gL_" + name)
        gb.setTitle(self._translate("Enrollment", text))
        ls_Layout = ls.children()[0]
        ls_Layout.addWidget(gb)
        # Label for Num Contract
        lb_num = QtWidgets.QLabel(gb)
        font = QtGui.QFont()
        font.setPointSize(12)
        lb_num.setFont(font)
        lb_num.setObjectName("lb_num_" + name)
        lb_num.setText(self._translate("Enrollment", "Номер контракта"))
        gL_gb.addWidget(lb_num, 0, 0)
        # LineEdit for Num Contract
        ledit = QtWidgets.QLineEdit(gb)
        ledit.setObjectName("ledit_" + name)
        gL_gb.addWidget(ledit, 0, 1)
        # Label for Date
        lb_date = QtWidgets.QLabel(gb)
        font = QtGui.QFont()
        font.setPointSize(12)
        lb_date.setFont(font)
        lb_date.setObjectName("lb_date_" + name)
        lb_date.setText(self._translate("Enrollment", "Дата заключения контракта"))
        gL_gb.addWidget(lb_date, 1, 0)
        # DateEdit for Date
        dedit = QtWidgets.QDateEdit(gb)
        font = QtGui.QFont()
        font.setPointSize(10)
        dedit.setFont(font)
        dedit.setDate(QtCore.QDate(2000, 1, 1))
        dedit.setObjectName("dedit_" + name)
        gL_gb.addWidget(dedit, 1, 1)
        if _hide:
            gb.hide()
        return gb

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
            _db1.close()
            self.head_ui.textEdit_headers_fullname.setText(_head[0][1])
            self.head_ui.textEdit_headers_prof.setText(_head[0][5])

            if _head[0][2] is not None and _head[0][2] != '':
                self.head_ui.textEdit_headers_phone.setText(_head[0][2])
            else:
                self.head_ui.textEdit_headers_phone.setText('')

            if _head[0][3] is not None and _head[0][3] != '':
                self.head_ui.textEdit_headers_mail.setText(_head[0][3])
            else:
                self.head_ui.textEdit_headers_mail.setText('')

            if _head[0][4] is not None and _head[0][4] != '':
                self.head_ui.textEdit_headers_web.setText(_head[0][4])
            else:
                self.head_ui.textEdit_headers_web.setText('')

        _db = ARMDataBase()
        _sql = "SELECT * FROM headers"
        headers = _db.query(_sql)
        _db.close()
        head_loader = []
        for i in range(len(headers)):
            heads = []
            for h in headers[i]:
                heads.append(h)
            head_loader.append(str(heads[0])[:])
            heads[0] = 'clb_head_' + str(heads[0])
            heads[1] = 'ФИО: ' + heads[1] + '\n'
            heads[2] = 'Телефоны: ' + heads[2] + '\n' if heads[2] is not None and heads[2] != '' else ''
            heads[3] = 'Электронные почты: ' + heads[3] + '\n' if heads[3] is not None and heads[3] != '' else ''
            heads[4] = 'Социальные сети: ' + heads[4] + '\n' if heads[4] is not None and heads[4] != '' else ''
            heads[5] = 'Должность: ' + heads[5] + '\n' if heads[5] is not None and heads[5] != '' else ''
            searcher = ''
            if search_text is None or search_text == "":
                _search_text = self.head_ui.lineEdit_search_headers.text().lower()
            elif search_text is not None:
                _search_text = search_text.lower()
            else:
                _search_text = search_text
            for h in heads:
                if h is not None and h != '':
                    searcher = searcher + h.lower()
            if _search_text is not None and _search_text != '':
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
            _db1.close()
            self.prog_ui.textEdit_prog_name.setText(_prog[0][1])
            self.prog_ui.textEdit_prog_range.setText(_prog[0][2])
            dates = _prog[0][3].split("|")
            self.prog_ui.dateEdit_start_program.setDate(datetime.date(int(dates[0].split('.')[2]),
                                                                      int(dates[0].split('.')[1]),
                                                                      int(dates[0].split('.')[0])))
            self.prog_ui.dateEdit_end_program.setDate(datetime.date(int(dates[1].split('.')[2]),
                                                                    int(dates[1].split('.')[1]),
                                                                    int(dates[1].split('.')[0])))

        _db = ARMDataBase()
        _sql = "SELECT * FROM programs"
        programs = _db.query(_sql)
        _db.close()
        prog_loader = []
        for i in range(len(programs)):
            progs = []
            for h in programs[i]:
                progs.append(h)
            if str(progs[0]) != "8":
                prog_loader.append(str(progs[0])[:])
                progs[0] = 'clb_prog_' + str(progs[0])
                progs[1] = 'Программа: ' + progs[1] + '\n'
                progs[2] = 'Продолжительность: в течении ' + progs[2] + ' месяцев\n' if progs[2] is not None and progs[
                    2] != '' else ''
                progs[3] = 'Даты проведения: с ' + progs[3].split("|")[0] + " по " + progs[3].split("|")[1] + '\n'
                searcher = ''
                if search_text is None or search_text == "":
                    _search_text = self.prog_ui.lineEdit_search_programs.text().lower()
                elif search_text is not None:
                    _search_text = search_text.lower()
                else:
                    _search_text = search_text
                for h in progs:
                    if h is not None and h != '':
                        searcher = searcher + h.lower()
                if _search_text is not None and _search_text != '':
                    if _search_text in searcher:
                        prog_but = self.create_list_el(progs[0],
                                                       progs[1] + progs[2] + progs[3],
                                                       self.prog_ui.sAWContent_programs_list)
                        prog_but.clicked.connect(lambda: loader_programs_edits())
                else:
                    prog_but = self.create_list_el(progs[0],
                                                   progs[1] + progs[2] + progs[3],
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
            _db1.close()
            self.teach_ui.textEdit_teachers_fullname.setText(_teach[0][1])
            self.teach_ui.textEdit_teachers_prof.setText(_teach[0][5])

            if _teach[0][2] is not None and _teach[0][2] != '':
                self.teach_ui.textEdit_teachers_phone.setText(_teach[0][2])
            else:
                self.teach_ui.textEdit_teachers_phone.setText('')

            if _teach[0][3] is not None and _teach[0][3] != '':
                self.teach_ui.textEdit_teachers_mail.setText(_teach[0][3])
            else:
                self.teach_ui.textEdit_teachers_mail.setText('')

            if _teach[0][4] is not None and _teach[0][4] != '':
                self.teach_ui.textEdit_teachers_web.setText(_teach[0][4])
            else:
                self.teach_ui.textEdit_teachers_web.setText('')

        _db = ARMDataBase()
        _sql = "SELECT * FROM teachers"
        teachers = _db.query(_sql)
        _db.close()
        teach_loader = []
        for i in range(len(teachers)):
            teachs = []
            for h in teachers[i]:
                teachs.append(h)
            teach_loader.append(str(teachs[0])[:])
            teachs[0] = 'clb_teach_' + str(teachs[0])
            teachs[1] = 'ФИО: ' + teachs[1] + '\n'
            teachs[2] = 'Телефоны: ' + teachs[2] + '\n' if teachs[2] is not None and teachs[2] != '' else ''
            teachs[3] = 'Электронные почты: ' + teachs[3] + '\n' if teachs[3] is not None and teachs[3] != '' else ''
            teachs[4] = 'Социальные сети: ' + teachs[4] + '\n' if teachs[4] is not None and teachs[4] != '' else ''
            teachs[5] = 'Должность: ' + teachs[5] + '\n' if teachs[5] is not None and teachs[5] != '' else ''
            searcher = ''
            if search_text is None or search_text == "":
                _search_text = self.teach_ui.lineEdit_search_teachers.text().lower()
            elif search_text is not None:
                _search_text = search_text.lower()
            else:
                _search_text = search_text
            for h in teachs:
                if h is not None and h != '':
                    searcher = searcher + h.lower()
            if _search_text is not None and _search_text != '':
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
            _db1.close()
            self.groups_ui.textEdit_groups_name.setText(_grp[0][2])
            self.groups_ui.comboBox_groups_prog.setCurrentIndex(
                self.groups_ui.comboBox_groups_prog.findData(_grp[0][3]))
            if _grp[0][2] is not None and _grp[0][2] != '':
                self.groups_ui.textEdit_groups_class.setText(_grp[0][1])
            else:
                self.groups_ui.textEdit_groups_class.setText('')

        _db = ARMDataBase()
        _sql = "SELECT * FROM groups"
        groups = _db.query(_sql)
        _db.close()
        grp_loader = []

        _db = ARMDataBase()
        for i in range(len(groups)):
            grps = []
            for h in groups[i]:
                grps.append(h)
            grp_loader.append(str(grps[0])[:])

            _sql = "SELECT prog_name FROM programs WHERE id_prog=" + str(grps[3])
            group_prog = _db.query(_sql)
            if not group_prog:
                group_prog = [["Отсутствует"]]

            grps[0] = 'clb_grp_' + str(grps[0])
            grps[1] = 'Класс: ' + grps[1] + '\n' if grps[1] is not None and grps[1] != '' else ''
            grps[2] = 'Группа: ' + grps[2] + '\n'
            grps[3] = 'Программа: ' + group_prog[0][0] + '\n' if group_prog[0][0] is not None and group_prog[0][
                0] != '' else ''
            searcher = ''
            if search_text is None or search_text == "":
                _search_text = self.groups_ui.lineEdit_search_groups.text().lower()
            elif search_text is not None:
                _search_text = search_text.lower()
            else:
                _search_text = search_text
            for h in grps:
                if h is not None and h != '':
                    searcher = searcher + h.lower()
            if grps[0].split("_")[-1] != "1":
                if _search_text is not None and _search_text != '':
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
        _db.close()

        _db = ARMDataBase()
        _sql = "SELECT * FROM programs"
        programs = _db.query(_sql)
        _db.close()
        _programs = []

        self.groups_ui.comboBox_groups_prog.clear()
        for prog in programs:
            self.create_combo_box_el(self.groups_ui.comboBox_groups_prog, prog[0], str(prog[1]))

    # Loader database for subjects
    def load_db_subjects(self, search_text=None):
        clear_list(self.sub_ui.sAWContent_sub_list.children())

        def loader_sub_edits():
            selected_subject = ''
            subjects_list = self.sub_ui.sAWContent_sub_list.children()
            if len(subjects_list) != 2:
                for sub in subjects_list:
                    if sub.objectName() != 'vL_sAWContent_sub_list':
                        if sub.isChecked():
                            selected_subject = sub.objectName().split('_')[-1]
                            break
            else:
                selected_subject = self.sub_ui.sAWContent_sub_list.children()[-1].objectName().split('_')[-1]
            _db1 = ARMDataBase()
            _sql1 = "SELECT * FROM subjects WHERE id_sub=" + selected_subject
            _sub = _db1.query(_sql1)
            _db1.close()

            self.sub_ui.textEdit_sub_name.setText(_sub[0][1])
            self.sub_ui.lineEdit_sub_tax.setText(_sub[0][2])
            self.sub_ui.comboBox_sub_teach.setCurrentIndex(
                self.sub_ui.comboBox_sub_teach.findData(_sub[0][3]))
            self.sub_ui.lineEdit_sub_price.setText(_sub[0][4])
            self.sub_ui.comboBox_sub_prog.setCurrentIndex(
                self.sub_ui.comboBox_sub_prog.findData(_sub[0][5]))
            self.sub_ui.lineEdit_sub_hours.setText(_sub[0][8])

        _db = ARMDataBase()
        _sql = "SELECT * FROM subjects"
        subjects = _db.query(_sql)
        _db.close()
        sub_loader = []

        _db = ARMDataBase()
        for i in range(len(subjects)):
            subs = []
            for h in subjects[i]:
                subs.append(h)
            sub_loader.append(str(subs[0])[:])

            _sql = "SELECT teacher_name FROM teachers WHERE id_teacher=" + str(subs[3])
            sub_teach = _db.query(_sql)

            _sql = "SELECT prog_name FROM programs WHERE id_prog=" + str(subs[5])
            sub_prog = _db.query(_sql)

            subs[0] = 'clb_sub_' + str(subs[0])
            subs[1] = 'Название: ' + subs[1] + '\n' if subs[1] is not None and subs[1] != '' else ''
            subs[2] = 'Такса: ' + subs[2] + '\n' if subs[2] is not None and subs[2] != '' else ''
            subs[3] = 'Преподаватель: ' + sub_teach[0][0] + '\n' if sub_teach[0][0] is not None and sub_teach[0][
                0] != '' else ''
            subs[4] = 'Стоимость: ' + subs[4] + '\n' if subs[4] is not None and subs[4] != '' else ''
            subs[5] = 'Программа: ' + sub_prog[0][0] + '\n' if sub_prog[0][0] is not None and sub_prog[0][
                0] != '' else ''
            subs[8] = 'Всего часов: ' + subs[8] + '\n' if subs[8] is not None and subs[8] != '' else ''
            searcher = ''
            if search_text is None or search_text == "":
                _search_text = self.sub_ui.lineEdit_search_sub.text().lower()
            elif search_text is not None:
                _search_text = search_text.lower()
            else:
                _search_text = search_text
            for h in subs:
                if h is not None and h != '':
                    searcher = searcher + h.lower()
            if _search_text is not None and _search_text != '':
                if _search_text in searcher:
                    sub_but = self.create_list_el(subs[0],
                                                  subs[1] + subs[2] + subs[3] + subs[4] + subs[5] + subs[8],
                                                  self.sub_ui.sAWContent_sub_list)
                    sub_but.clicked.connect(lambda: loader_sub_edits())
            else:
                sub_but = self.create_list_el(subs[0],
                                              subs[1] + subs[2] + subs[3] + subs[4] + subs[5] + subs[8],
                                              self.sub_ui.sAWContent_sub_list)
                sub_but.clicked.connect(lambda: loader_sub_edits())
        _db.close()

        _db = ARMDataBase()

        _sql = "SELECT * FROM programs"
        programs = _db.query(_sql)
        _programs = []
        self.sub_ui.comboBox_sub_prog.clear()
        for prog in programs:
            self.create_combo_box_el(self.sub_ui.comboBox_sub_prog, prog[0], str(prog[1]))

        _sql = "SELECT * FROM teachers"
        teachers = _db.query(_sql)
        _teachers = []
        self.sub_ui.comboBox_sub_teach.clear()
        for teach in teachers:
            self.create_combo_box_el(self.sub_ui.comboBox_sub_teach, teach[0], str(teach[1]))

        _db.close()

    # Loader database for students
    def load_db_students(self, search_text=None):
        clear_list(self.stud_ui.sAWContent_stud_list.children())

        def loader_stud_edits():
            selected_students = ''
            students_list = self.stud_ui.sAWContent_stud_list.children()
            if len(students_list) != 2:
                for stud in students_list:
                    if stud.objectName() != 'vL_sAWContent_stud_list':
                        if stud.isChecked():
                            selected_students = stud.objectName().split('_')[-1]
                            break
            else:
                selected_students = self.stud_ui.sAWContent_stud_list.children()[-1].objectName().split('_')[-1]
            _db1 = ARMDataBase()
            _sql1 = "SELECT * FROM students WHERE id_student=" + selected_students
            _stud = _db1.query(_sql1)
            _db1.close()

            self.stud_ui.textEdit_stud_fullname.setText(_stud[0][1])
            self.stud_ui.dateEdit_stud_birthday.setDate(datetime.date(int(_stud[0][3].split('.')[2]),
                                                                      int(_stud[0][3].split('.')[1]),
                                                                      int(_stud[0][3].split('.')[0])))
            self.stud_ui.lineEdit_stud_phone.setText(_stud[0][4])
            if _stud[0][5] == 'male':
                self.stud_ui.radioButton_stud_gender_male.setChecked(1)
                self.stud_ui.radioButton_stud_gender_female.setChecked(0)
            else:
                self.stud_ui.radioButton_stud_gender_female.setChecked(1)
                self.stud_ui.radioButton_stud_gender_male.setChecked(0)
            self.stud_ui.lineEdit_stud_city.setText(_stud[0][6])
            self.stud_ui.lineEdit_stud_einst.setText(_stud[0][7])
            self.stud_ui.lineEdit_stud_mail.setText(_stud[0][8])
            self.stud_ui.lineEdit_stud_web.setText(_stud[0][9])
            self.stud_ui.comboBox_stud_group.setCurrentIndex(
                self.stud_ui.comboBox_stud_group.findData(_stud[0][2]))

        _db = ARMDataBase()
        _sql = "SELECT * FROM students"
        students = _db.query(_sql)
        _db.close()
        stud_loader = []

        _db = ARMDataBase()
        for i in range(len(students)):
            studs = []
            for h in students[i]:
                studs.append(h)
            stud_loader.append(str(studs[0])[:])

            if studs[2] is not None and studs[2] != '':
                _sql = "SELECT group_name FROM groups WHERE id_group=" + str(studs[2])
                stud_group = _db.query(_sql)
            else:
                stud_group = [['']]

            if studs[5] == "male":
                studs[5] = "Мужской"
            else:
                studs[5] = "Женский"

            studs[0] = 'clb_stud_' + str(studs[0])
            studs[1] = 'ФИО: ' + studs[1] + '\n' if studs[1] is not None and studs[1] != '' else ''
            studs[2] = 'Группа: ' + stud_group[0][0] + '\n' if stud_group[0][0] is not None and stud_group[0][
                0] != '' else ''
            studs[3] = 'День рождения: ' + studs[3] + '\n' if studs[3] is not None and studs[3] != '' else ''
            studs[4] = 'Телефон: ' + studs[4] + '\n' if studs[4] is not None and studs[4] != '' else ''
            studs[5] = 'Пол: ' + studs[5] + '\n' if studs[5] is not None and studs[5] != '' else ''
            studs[6] = 'Место проживания: ' + studs[6] + '\n' if studs[6] is not None and studs[6] != '' else ''
            studs[7] = 'Место обучения: ' + studs[7] + '\n' if studs[7] is not None and studs[7] != '' else ''
            studs[8] = 'Электронная почта: ' + studs[8] + '\n' if studs[8] is not None and studs[8] != '' else ''
            studs[9] = 'Социальные сети: ' + studs[9] + '\n' if studs[9] is not None and studs[9] != '' else ''
            searcher = ''
            if search_text is None or search_text == "":
                _search_text = self.stud_ui.lineEdit_search_stud.text().lower()
            elif search_text is not None:
                _search_text = search_text.lower()
            else:
                _search_text = search_text
            for h in studs:
                if h is not None and h != '':
                    searcher = searcher + h.lower()
            if _search_text is not None and _search_text != '':
                if _search_text in searcher:
                    stud_but = self.create_list_el(studs[0],
                                                   studs[1] + studs[2] + studs[3] + studs[4] + studs[5] + studs[6] +
                                                   studs[7] + studs[8] + studs[9],
                                                   self.stud_ui.sAWContent_stud_list)
                    stud_but.clicked.connect(lambda: loader_stud_edits())
            else:
                stud_but = self.create_list_el(studs[0],
                                               studs[1] + studs[2] + studs[3] + studs[4] + studs[5] + studs[6] + studs[
                                                   7] + studs[8] + studs[9],
                                               self.stud_ui.sAWContent_stud_list)
                stud_but.clicked.connect(lambda: loader_stud_edits())
        _db.close()

        _db = ARMDataBase()
        _sql = "SELECT * FROM groups"
        groups = _db.query(_sql)
        _db.close()
        _groups = []
        self.stud_ui.comboBox_stud_group.clear()
        for group in groups:
            self.create_combo_box_el(self.stud_ui.comboBox_stud_group, group[0], str(group[2]))

    # Loader database for enrollment
    def load_db_enrollment(self, search_text=None):
        clear_list(self.enr_ui.sAWContent_enr_list.children())

        def check_box_clicked():
            self.enr_ui.list_cb_check = []
            for check in self.enr_ui.groupBox_stud_subs.children():
                if "el_" in check.objectName():
                    self.enr_ui.list_cb_check.append([check.objectName().split('_')[-1], check.isChecked()])
            for o in range(len(self.enr_ui.list_cb_check)):
                if self.enr_ui.list_cb_check[o][1] is not self.enr_ui.list_cb_checked[o][1]:
                    for check in self.enr_ui.groupBox_stud_subs.children():
                        if "el_" + self.enr_ui.list_cb_check[o][0] in check.objectName():
                            if check.isChecked():
                                for child in self.enr_ui.groupBox_sis_contracts.children():
                                    if "grB_" in child.objectName() and \
                                            self.enr_ui.list_cb_check[o][0] in child.objectName():
                                        child.show()
                                        self.enr_ui.list_cb_checked[o][1] = True
                            else:
                                for child in self.enr_ui.groupBox_sis_contracts.children():
                                    if "grB_" in child.objectName() and \
                                            self.enr_ui.list_cb_check[o][0] in child.objectName():
                                        child.hide()
                                        self.enr_ui.list_cb_checked[o][1] = False

        def loader_enr_edits():
            clear_group_box(self.enr_ui.groupBox_stud_subs.children())
            clear_group_box(self.enr_ui.groupBox_sis_contracts.children())
            selected_enrollment = ''
            enrollment_list = self.enr_ui.sAWContent_enr_list.children()
            if len(enrollment_list) != 2:
                for enr in enrollment_list:
                    if enr.objectName() != 'vL_sAWContent_enr_list':
                        if enr.isChecked():
                            selected_enrollment = enr.objectName().split('_')[-1]
                            break
            else:
                selected_enrollment = self.enr_ui.sAWContent_enr_list.children()[-1].objectName().split('_')[-1]
            _db1 = ARMDataBase()
            _sql3 = "SELECT id_sub, status FROM subs_in_studs WHERE id_student=" + selected_enrollment
            list_active_subs = _db1.query(_sql3)
            _sql3 = "SELECT id_group FROM students WHERE id_student=" + selected_enrollment
            id_group_stud = _db1.query(_sql3)
            _sql3 = "SELECT id_prog FROM groups WHERE id_group=" + str(id_group_stud[0][0])
            id_prog_stud = _db1.query(_sql3)
            _sql3 = "SELECT id_sub, sub_name FROM subjects WHERE id_prog=" + str(id_prog_stud[0][0])
            list_subs = _db1.query(_sql3)
            _list_active_subs = []
            self.enr_ui.list_cb_checked = []
            for sub in range(len(list_active_subs)):
                if list_active_subs[sub][1] == "1":
                    _list_active_subs.append(str(list_active_subs[sub][0])[:])
            for l in range(len(list_subs)):
                _sql2 = "SELECT student_numcontract, student_datecontract, status FROM subs_in_studs WHERE id_sub=" + \
                        str(list_subs[l][0]) + " AND id_student=" + selected_enrollment
                contracts1 = _db1.query(_sql2)
                cb = self.create_check_box_el(self.enr_ui.groupBox_stud_subs, 'el_' + str(list_subs[l][0]),
                                              list_subs[l][1],
                                              True if str(list_subs[l][0]) in _list_active_subs else False)
                self.enr_ui.list_cb_checked.append(
                    [str(list_subs[l][0]), True if str(list_subs[l][0]) in _list_active_subs else False])
                cb.clicked.connect(lambda: check_box_clicked())
                gb = self.create_sub_groupbox(self.enr_ui.groupBox_sis_contracts,
                                              "grB_" + str(list_subs[l][0]),
                                              list_subs[l][1],
                                              False if str(list_subs[l][0]) in _list_active_subs else True)
                for chield in gb.children():
                    if "gL_" not in chield.objectName() and contracts1 != []:
                        if "ledit_grB_" in chield.objectName():
                            chield.setText(contracts1[0][0])
                        elif "dedit_grB_" in chield.objectName():
                            chield.setDate(datetime.date(int(contracts1[0][1].split('.')[2]),
                                                         int(contracts1[0][1].split('.')[1]),
                                                         int(contracts1[0][1].split('.')[0])))
            _db1.close()

        _db = ARMDataBase()
        _sql = "SELECT * FROM students"
        students = _db.query(_sql)
        _db.close()
        stud_loader = []

        _db = ARMDataBase()
        for i in range(len(students)):
            studs = []
            for h in students[i]:
                studs.append(h)
            stud_loader.append(str(studs[0])[:])

            if studs[2] is not None and studs[2] != '':
                _sql = "SELECT group_name FROM groups WHERE id_group=" + str(studs[2])
                stud_group = _db.query(_sql)
            else:
                stud_group = [['']]

            if stud_group != [['']] and stud_group is not None:
                _sql = "SELECT id_prog FROM groups WHERE id_group=" + str(studs[2])
                stud_group_prog_id = _db.query(_sql)
                _sql = "SELECT prog_name FROM programs WHERE id_prog=" + str(stud_group_prog_id[0][0])
                stud_group_prog_name = _db.query(_sql)
                _sql = "SELECT prog_range FROM programs WHERE id_prog=" + str(stud_group_prog_id[0][0])
                stud_group_prog_range = _db.query(_sql)
            else:
                stud_group_prog_name = [['']]
                stud_group_prog_range = [['']]

            _sql = "SELECT id_sub FROM subs_in_studs WHERE id_student=" + str(studs[0])
            stud_subs = _db.query(_sql)
            subjects = ''
            for s in range(len(stud_subs)):
                _sql = "SELECT sub_name FROM subjects WHERE id_sub=" + str(stud_subs[s][0])
                _sql1 = "SELECT student_numcontract, student_datecontract, status FROM subs_in_studs WHERE id_sub=" + str(
                    stud_subs[s][0]) + " AND id_student=" + str(studs[0])
                contracts = _db.query(_sql1)
                if s > 0:
                    if contracts[0][2] == "1":
                        subjects += ', ' + _db.query(_sql)[0][0] + '({}, {})'.format(contracts[0][0], contracts[0][1])
                else:
                    if contracts[0][2] == "1":
                        subjects += _db.query(_sql)[0][0] + '({}, {})'.format(contracts[0][0], contracts[0][1])

            studs[0] = 'clb_sis_' + str(studs[0])
            studs[1] = 'ФИО: ' + studs[1] + '\n' if studs[1] is not None and studs[1] != '' else ''
            studs[2] = 'Группа: ' + stud_group[0][0] + '\n' if stud_group[0][0] is not None and stud_group[0][
                0] != '' else ''
            studs[3] = 'Программа: ' + stud_group_prog_name[0][0] + '\n' if stud_group_prog_name[0][0] is not None and \
                                                                            stud_group_prog_name[0][
                                                                                0] != '' else ''
            studs[4] = 'Продолжительность обучения: ' + stud_group_prog_range[0][0] + ' месяцев\n' if \
                stud_group_prog_range[0][0] is not None and stud_group_prog_range[0][0] != '' else ''
            studs[
                5] = 'Предметы: ' + subjects + '\n' if subjects is not None and subjects != '' else 'Предметы: Отсутствуют\n'

            searcher = ''
            if search_text is None or search_text == "":
                _search_text = self.enr_ui.lineEdit_search_enr.text().lower()
            elif search_text is not None:
                _search_text = search_text.lower()
            else:
                _search_text = search_text
            for h in studs:
                if h is not None and h != '':
                    searcher = searcher + h.lower()
            if _search_text is not None and _search_text != '':
                if _search_text in searcher:
                    stud_but = self.create_list_el(studs[0],
                                                   studs[1] + studs[2] + studs[3] + studs[4] + studs[5],
                                                   self.enr_ui.sAWContent_enr_list)
                    stud_but.clicked.connect(lambda: loader_enr_edits())
            else:
                stud_but = self.create_list_el(studs[0],
                                               studs[1] + studs[2] + studs[3] + studs[4] + studs[5],
                                               self.enr_ui.sAWContent_enr_list)
                stud_but.clicked.connect(lambda: loader_enr_edits())
        _db.close()

    # Loader database for Outlay Calculator
    def load_db_outlay(self):
        _db = ARMDataBase()
        _sql = "SELECT * FROM programs"
        programs = _db.query(_sql)
        _db.close()

        self.outlay_ui.comboBox_progs.clear()
        self.create_combo_box_el(self.outlay_ui.comboBox_progs, "None", "Отсутствует")
        for prog in programs:
            if str(prog[0]) != "8":
                self.create_combo_box_el(self.outlay_ui.comboBox_progs, prog[0], str(prog[1]))
        clear_widget(self.outlay_ui.widget_calcs.children())

        self.outlay_ui.radio_col_1.setChecked(True)
        self.add_calculate_box(False, "1", 0, 0)
        # self.add_calculate_box(False, "2", 1, 0)
        # self.add_calculate_box(False, "3", 0, 1)
        # self.add_calculate_box(False, "4", 1, 1)

    # Loader database for Timetable list
    def load_db_timetable(self, search_text=None):
        clear_list(self.ui.sAWContent_timetable.children())
        _db = ARMDataBase()
        _sql = "SELECT id_sub, sub_name, id_teacher, id_prog, sub_hours, sub_hours_need FROM subjects"
        timetable_info = _db.query(_sql)
        for i in range(len(timetable_info)):
            text = "Предмет: {}\n".format(timetable_info[i][1])
            _sql = "SELECT prog_name, prog_range FROM programs WHERE id_prog=" + str(timetable_info[i][3])
            prog_info = _db.query(_sql)
            text += "Программа: {}\n".format(prog_info[0][0])
            text += "Продолжительность программы: в течении {} месяцев\n".format(prog_info[0][1])
            _sql = "SELECT teacher_name FROM teachers WHERE id_teacher=" + str(timetable_info[i][2])
            teacher_info = _db.query(_sql)
            text += "Преподаватель: {}\n".format(teacher_info[0][0])
            text += "Необходимо часов: {}\n".format(timetable_info[i][5])
            text += "Часы: {}\n".format(timetable_info[i][4])
            _search_text = search_text
            searcher = text.lower()
            if _search_text is not None and _search_text != '':
                _search_text = search_text.lower()
                if _search_text in searcher:
                    ttable_but = self.create_list_el("clb_ttible_" + str(timetable_info[i][0]),
                                                     text,
                                                     self.ui.sAWContent_timetable)
            else:
                ttable_but = self.create_list_el("clb_ttible_" + str(timetable_info[i][0]),
                                                 text,
                                                 self.ui.sAWContent_timetable)
        _db.close()

    # Loader database for exe_Timetable list
    def load_db_timetable_list(self):
        def setup_date():
            for date_ in self.ttable_ui.sAWContent_hours_list.children():
                if date_.objectName().startswith("clb_"):
                    if date_.isChecked():
                        self.ttable_ui.calendar.setSelectedDate(
                            datetime.datetime.fromtimestamp(float(date_.objectName().split("_")[-1])))
                        break

        self.ttable_list = []
        clear_list(self.ttable_ui.sAWContent_hours_list.children())
        _db = ARMDataBase()
        _sql = "SELECT sub_ttable, sub_hours FROM subjects WHERE id_sub=" + self.ttable_selected_sub
        timetable_sub = _db.query(_sql)
        self.ttable_ui.lab_sum.setText("Сумма часов: " + timetable_sub[0][1])
        parse_timetable = []
        if timetable_sub[0][0] is not None and timetable_sub[0][0] != '':
            for date in timetable_sub[0][0].split(","):
                parse_timetable.append(date)
            for i in range(len(parse_timetable)):
                parse_timetable[i] = parse_timetable[i].split("|")
                parse_timetable[i][0] = datetime.datetime.strptime(parse_timetable[i][0], "%d.%m.%Y")
                if parse_timetable[i][0].weekday() == 0:
                    parse_timetable[i].append('Понедельник')
                elif parse_timetable[i][0].weekday() == 1:
                    parse_timetable[i].append('Вторник')
                elif parse_timetable[i][0].weekday() == 2:
                    parse_timetable[i].append('Среда')
                elif parse_timetable[i][0].weekday() == 3:
                    parse_timetable[i].append('Четверг')
                elif parse_timetable[i][0].weekday() == 4:
                    parse_timetable[i].append('Пятница')
                elif parse_timetable[i][0].weekday() == 5:
                    parse_timetable[i].append('Суббота')
                elif parse_timetable[i][0].weekday() == 6:
                    parse_timetable[i].append('Воскресенье')

                if parse_timetable[i][0].strftime("%m") == "01":
                    parse_timetable[i].append('Января')
                elif parse_timetable[i][0].strftime("%m") == "02":
                    parse_timetable[i].append('Февраля')
                elif parse_timetable[i][0].strftime("%m") == "03":
                    parse_timetable[i].append('Марта')
                elif parse_timetable[i][0].strftime("%m") == "04":
                    parse_timetable[i].append('Апреля')
                elif parse_timetable[i][0].strftime("%m") == "05":
                    parse_timetable[i].append('Мая')
                elif parse_timetable[i][0].strftime("%m") == "06":
                    parse_timetable[i].append('Июня')
                elif parse_timetable[i][0].strftime("%m") == "07":
                    parse_timetable[i].append('Июля')
                elif parse_timetable[i][0].strftime("%m") == "08":
                    parse_timetable[i].append('Августа')
                elif parse_timetable[i][0].strftime("%m") == "09":
                    parse_timetable[i].append('Сентября')
                elif parse_timetable[i][0].strftime("%m") == "10":
                    parse_timetable[i].append('Октября')
                elif parse_timetable[i][0].strftime("%m") == "11":
                    parse_timetable[i].append('Ноября')
                elif parse_timetable[i][0].strftime("%m") == "12":
                    parse_timetable[i].append('Декабря')
                btn = self.create_list_el(
                    "clb_" + str(parse_timetable[i][0].timestamp()),
                    parse_timetable[i][0].strftime("%d") + " " +
                    parse_timetable[i][3] + ", " +
                    parse_timetable[i][2] + ", " +
                    parse_timetable[i][0].strftime("%Y") + ", " +
                    parse_timetable[i][1] + " часов",
                    self.ttable_ui.sAWContent_hours_list
                )
                btn.clicked.connect(lambda: setup_date())
            self.ttable_list = copy.deepcopy(parse_timetable)

    def del_hours(self):
        del_hour = datetime.datetime.strptime(self.ttable_ui.calendar.selectedDate().toString('dd.MM.yyyy'),
                                              "%d.%m.%Y")
        parsed_hours = ''
        sum_hours = 0

        for _date in self.ttable_list:
            if _date[0] == del_hour:
                self.ttable_list.remove(_date)

        for hour in self.ttable_list:
            parsed_hours += hour[0].strftime("%d.%m.%Y") + "|" + hour[1] + ','
            sum_hours += int(hour[1])
        parsed_hours = parsed_hours[:-1]
        _db = ARMDataBase()
        _sql = "UPDATE subjects SET " \
               "sub_ttable = '{0}', " \
               "sub_hours = '{1}' " \
               "WHERE id_sub = '{2}'".format(parsed_hours,
                                             str(sum_hours),
                                             self.ttable_selected_sub)
        _db.query(_sql)
        _db.close()
        self.load_db_timetable_list()

    def set_hours(self):
        parse_hour = datetime.datetime.strptime(self.ttable_ui.calendar.selectedDate().toString('dd.MM.yyyy'),
                                                "%d.%m.%Y")
        search_status = 0
        sum_hours = 0
        parsed_hours = ''
        for hour in self.ttable_list:
            if hour[0] == parse_hour:
                hour[1] = self.ttable_ui.lEdit_hours.text()
                search_status = 1
                break
            else:
                search_status = 0
        if not search_status:
            self.ttable_list.append([parse_hour, self.ttable_ui.lEdit_hours.text()])
            self.ttable_list = sorted(
                self.ttable_list,
                key=lambda x: x[0], reverse=False
            )
        for hour in self.ttable_list:
            parsed_hours += hour[0].strftime("%d.%m.%Y") + "|" + hour[1] + ','
            sum_hours += int(hour[1])
        parsed_hours = parsed_hours[:-1]
        _db = ARMDataBase()
        _sql = "UPDATE subjects SET " \
               "sub_ttable = '{0}', " \
               "sub_hours = '{1}' " \
               "WHERE id_sub = '{2}'".format(parsed_hours,
                                             str(sum_hours),
                                             self.ttable_selected_sub)
        _db.query(_sql)
        _db.close()
        self.load_db_timetable_list()

    def timetable_list_exec(self):
        for i in self.ui.sAWContent_timetable.children():
            if not i.objectName().startswith("clb_ttible_"):
                pass
            else:
                if i.isChecked():
                    self.ttable_selected_sub = i.objectName().split('_')[-1]
                    _set_doc_warning = 0
                    break
                else:
                    _set_doc_warning = 1
        if _set_doc_warning:
            set_doc_warning("Ошибка (не выбрана запись для изменения)",
                            'Сначала выберите запись для изменения.\n\nНажмите на нужную запись, '
                            'чтобы выбрать ее, а потом нажмите на кнопку '
                            '"Изменить расписание"')
        else:
            self.load_db_timetable_list()
            self.ttable.exec_()

    # Loader database for exe_OutlayPrinter
    def load_db_outlay_printer(self):
        def setup_prog_info():
            # lEdit for class load
            _db1 = ARMDataBase()
            try:
                _sql = "SELECT class FROM groups WHERE id_prog=" + str(self.outpr_ui.comboBox_prog.currentData())
                group_class = _db1.query(_sql)
                self.outpr_ui.lEdit_class.setText(group_class[0][0])
            except Exception:
                self.outpr_ui.lEdit_class.setText("10")
            try:
                _sql = "SELECT prog_range_dates FROM programs WHERE id_prog=" + str(self.outpr_ui.comboBox_prog.currentData())
                dates = _db1.query(_sql)[0][0].split("|")
                self.outpr_ui.dateEdit_date_start.setDate(datetime.date(int(dates[0].split('.')[2]),
                                                                          int(dates[0].split('.')[1]),
                                                                          int(dates[0].split('.')[0])))
                self.outpr_ui.dateEdit_date_end.setDate(datetime.date(int(dates[1].split('.')[2]),
                                                                        int(dates[1].split('.')[1]),
                                                                        int(dates[1].split('.')[0])))
            except Exception:
                pass
            _db1.close()

        if self.outlay_ui.comboBox_progs.currentData() == "None" or self.outlay_ui.comboBox_progs.currentData() is None:
            selected = False
        else:
            selected = True

        self.outpr_ui.comboBox_head.clear()
        self.outpr_ui.comboBox_prog.clear()
        self.outpr_ui.lEdit_class.setText("")
        self.outpr_ui.comboBox_pfs.clear()
        self.outpr_ui.comboBox_bookkeeper.clear()
        self.outpr_ui.comboBox_manager_cpui.clear()
        clear_widget(self.outpr_ui.widget_subs_teachs.children())
        _db = ARMDataBase()

        # comboBox for Head load
        _sql = "SELECT id_head, head_name, head_prof FROM headers"
        headers = _db.query(_sql)
        for head in headers:
            self.create_combo_box_el(self.outpr_ui.comboBox_head, head[0], str(head[2]) + " | " + str(head[1]))
            if "директор хти" in str(head[2]).lower():
                self.outpr_ui.comboBox_head.setCurrentIndex(
                    self.outpr_ui.comboBox_head.findData(head[0]))

        # DateEdit for Date Confirm
        self.outpr_ui.dateEdit_date_confirm.setDate(datetime.datetime.today())

        # comboBox for Programs load
        _sql = "SELECT id_prog, prog_name, prog_range_dates FROM programs"
        programs = _db.query(_sql)
        for prog in programs:
            self.create_combo_box_el(self.outpr_ui.comboBox_prog, prog[0], str(prog[1]))
        if selected:
            self.outpr_ui.comboBox_prog.setCurrentIndex(
                self.outpr_ui.comboBox_prog.findData(
                    self.outlay_ui.comboBox_progs.currentData()
                ))
        self.outpr_ui.comboBox_prog.currentIndexChanged.connect(lambda: setup_prog_info())
        setup_prog_info()

        # comboBox for PFS load
        for head in headers:
            self.create_combo_box_el(self.outpr_ui.comboBox_pfs, head[0], str(head[2]) + " | " + str(head[1]))
            if "пфс" in str(head[2]).lower():
                self.outpr_ui.comboBox_pfs.setCurrentIndex(
                    self.outpr_ui.comboBox_pfs.findData(head[0]))

        # comboBox for Bookkeeper load
        for head in headers:
            self.create_combo_box_el(self.outpr_ui.comboBox_bookkeeper, head[0], str(head[2]) + " | " + str(head[1]))
            if "бухгалтер" in str(head[2]).lower():
                self.outpr_ui.comboBox_bookkeeper.setCurrentIndex(
                    self.outpr_ui.comboBox_bookkeeper.findData(head[0]))

        # comboBox for manager CPUI load
        for head in headers:
            self.create_combo_box_el(self.outpr_ui.comboBox_manager_cpui, head[0], str(head[2]) + " | " + str(head[1]))
            if "цпюи" in str(head[2]).lower():
                self.outpr_ui.comboBox_manager_cpui.setCurrentIndex(
                    self.outpr_ui.comboBox_manager_cpui.findData(head[0]))

        # Widgets for subs and teachers load
        if not selected:
            rb = 0
            if self.outlay_ui.radio_col_1.isChecked():
                rb = 1
            elif self.outlay_ui.radio_col_2.isChecked():
                rb = 2
            elif self.outlay_ui.radio_col_3.isChecked():
                rb = 3
            elif self.outlay_ui.radio_col_4.isChecked():
                rb = 4
            for r in range(rb):
                if r + 1 == 1:
                    self.add_sub_teach_box(False, str(r + 1), 0, 0)
                elif r + 1 == 2:
                    self.add_sub_teach_box(False, str(r + 1), 1, 0)
                elif r + 1 == 3:
                    self.add_sub_teach_box(False, str(r + 1), 0, 1)
                elif r + 1 == 4:
                    self.add_sub_teach_box(False, str(r + 1), 1, 1)
        else:
            _sql = "SELECT id_sub FROM subjects WHERE id_prog=" + str(self.outlay_ui.comboBox_progs.currentData())
            subs = _db.query(_sql)
            a = 0
            b = 0
            for i in subs:
                self.add_sub_teach_box(True, str(i[0]), a, b)
                if a == 0 and b == 0:
                    a = 1
                    b = 0
                elif a == 1 and b == 0:
                    a = 0
                    b = 1
                elif a == 0 and b == 1:
                    a = 1
                    b = 1

        _db.close()

    def outlay_printer_exec(self):
        self.load_db_outlay_printer()
        self.outlay_printer.exec_()

    def select_list_el(self):
        if self.ttable_ui.sAWContent_hours_list.findChild(
                QtWidgets.QCommandLinkButton, "clb_" +
                                              str(datetime.datetime.timestamp(datetime.datetime.combine(
                                                  self.ttable_ui.calendar.selectedDate().toPyDate(),
                                                  datetime.datetime.min.time())))
        ) is not None:
            self.ttable_ui.sAWContent_hours_list.findChild(
                QtWidgets.QCommandLinkButton, "clb_" +
                                              str(datetime.datetime.timestamp(datetime.datetime.combine(
                                                  self.ttable_ui.calendar.selectedDate().toPyDate(),
                                                  datetime.datetime.min.time())))
            ).setChecked(1)

    def add_calculate_box(self, sel_sub=False, id_sub="", i=0, j=0):
        widget_calcbox = QtWidgets.QGroupBox(self.outlay_ui.widget_calcs)
        widget_calcbox.setObjectName("widget_calcbox_" + id_sub)
        gL_widget_calcbox = QtWidgets.QGridLayout(widget_calcbox)
        gL_widget_calcbox.setObjectName("gL_widget_calcbox_" + id_sub)
        studs_col = [['0']]

        if sel_sub:
            _db = ARMDataBase()
            _sql = "SELECT sub_name, sub_price_hour, sub_price_month, sub_hours_need FROM subjects WHERE id_sub=" + id_sub
            sub_info = _db.query(_sql)

            widget_calcbox.setTitle(sub_info[0][0])

            _sql = "SELECT COUNT(*) FROM subs_in_studs WHERE id_sub={0} AND status=1".format(id_sub)
            studs_col = _db.query(_sql)

            _db.close()
        else:
            widget_calcbox.setTitle("Предмет " + id_sub)

        lab_studs = QtWidgets.QLabel(widget_calcbox)
        lab_studs.setObjectName("lab_studs_" + id_sub)
        lab_studs.setText(self._translate("Outlay", "Слушатели: "))
        gL_widget_calcbox.addWidget(lab_studs, 1, 0)

        check_auto = QtWidgets.QCheckBox(widget_calcbox)
        check_auto.setObjectName("check_auto_" + id_sub)
        check_auto.setChecked(True)
        check_auto.setText(self._translate("Outlay", "Автоматически"))
        gL_widget_calcbox.addWidget(check_auto, 0, 2)

        spin_studs = QtWidgets.QSpinBox(widget_calcbox)
        spin_studs.setObjectName("spin_studs_" + id_sub)
        spin_studs.setMaximum(100000)
        spin_studs.setSingleStep(1)
        gL_widget_calcbox.addWidget(spin_studs, 1, 1)

        radio_variability_studs = QtWidgets.QRadioButton(widget_calcbox)
        radio_variability_studs.setObjectName("radio_variability_studs_" + id_sub)
        gL_widget_calcbox.addWidget(radio_variability_studs, 1, 2)

        lab_price = QtWidgets.QLabel(widget_calcbox)
        lab_price.setObjectName("lab_price_" + id_sub)
        lab_price.setText(self._translate("Outlay", "Стоимость: "))
        gL_widget_calcbox.addWidget(lab_price, 2, 0)

        spin_price = QtWidgets.QSpinBox(widget_calcbox)
        spin_price.setObjectName("spin_price_" + id_sub)
        spin_price.setMaximum(1000000000)
        spin_price.setSingleStep(100)
        gL_widget_calcbox.addWidget(spin_price, 2, 1)

        radio_variability_price = QtWidgets.QRadioButton(widget_calcbox)
        radio_variability_price.setObjectName("radio_variability_price_" + id_sub)
        radio_variability_price.setChecked(True)
        gL_widget_calcbox.addWidget(radio_variability_price, 2, 2)

        lab_tax = QtWidgets.QLabel(widget_calcbox)
        lab_tax.setObjectName("lab_tax_" + id_sub)
        lab_tax.setText(self._translate("Outlay", "Часовая стоимость: "))
        gL_widget_calcbox.addWidget(lab_tax, 3, 0)

        spin_tax = QtWidgets.QSpinBox(widget_calcbox)
        spin_tax.setObjectName("spin_tax_" + id_sub)
        spin_tax.setMaximum(1000000000)
        spin_tax.setSingleStep(50)
        gL_widget_calcbox.addWidget(spin_tax, 3, 1)

        radio_variability_tax = QtWidgets.QRadioButton(widget_calcbox)
        radio_variability_tax.setObjectName("radio_variability_tax_" + id_sub)
        gL_widget_calcbox.addWidget(radio_variability_tax, 3, 2)

        lab_hours = QtWidgets.QLabel(widget_calcbox)
        lab_hours.setObjectName("lab_hours_" + id_sub)
        lab_hours.setText(self._translate("Outlay", "Часы: "))
        gL_widget_calcbox.addWidget(lab_hours, 4, 0)

        spin_hours = QtWidgets.QSpinBox(widget_calcbox)
        spin_hours.setObjectName("spin_hours_" + id_sub)
        spin_hours.setMaximum(1000)
        spin_hours.setSingleStep(2)
        gL_widget_calcbox.addWidget(spin_hours, 4, 1)

        spin_studs.valueChanged.connect(lambda: self.calculate_values())
        spin_hours.valueChanged.connect(lambda: self.calculate_values())
        spin_tax.valueChanged.connect(lambda: self.calculate_values())
        spin_price.valueChanged.connect(lambda: self.calculate_values())
        check_auto.clicked.connect(lambda: self.outlay_check_click())

        if sel_sub:
            spin_studs.setValue(studs_col[0][0])
            spin_price.setValue(int(sub_info[0][2]))
            spin_tax.setValue(int(sub_info[0][1]))
            spin_hours.setValue(int(sub_info[0][3]))

        self.outlay_ui.gL_widget_calcs.addWidget(widget_calcbox, i, j)
        return widget_calcbox

    def add_sub_teach_box(self, sel_sub=False, id_sub="", i=0, j=0):
        widget_sub_teach = QtWidgets.QWidget(self.outpr_ui.widget_subs_teachs)
        widget_sub_teach.setObjectName("widget_sub_teach_" + id_sub)
        gL_widget_sub_teach = QtWidgets.QGridLayout(widget_sub_teach)
        gL_widget_sub_teach.setObjectName("gL_widget_sub_teach_" + id_sub)

        lab_sub_name = QtWidgets.QLabel(widget_sub_teach)
        lab_sub_name.setObjectName("lab_sub_name_" + id_sub)
        if sel_sub:
            lab_sub_name.setText(self._translate("OutlayPrinter", "Предмет: "))
        else:
            lab_sub_name.setText(self._translate("OutlayPrinter", "Предмет {}: ".format(id_sub)))
        gL_widget_sub_teach.addWidget(lab_sub_name, 0, 0)

        lEdit_sub_name = QtWidgets.QLineEdit(widget_sub_teach)
        lEdit_sub_name.setObjectName("lEdit_sub_name_" + id_sub)
        gL_widget_sub_teach.addWidget(lEdit_sub_name, 0, 1)

        lab_teach_name = QtWidgets.QLabel(widget_sub_teach)
        lab_teach_name.setObjectName("lab_teach_name_" + id_sub)
        if sel_sub:
            lab_teach_name.setText(self._translate("OutlayPrinter", "Преподаватель: "))
        else:
            lab_teach_name.setText(self._translate("OutlayPrinter", "Преподаватель {}: ".format(id_sub)))
        gL_widget_sub_teach.addWidget(lab_teach_name, 1, 0)

        lEdit_teach_name = QtWidgets.QLineEdit(widget_sub_teach)
        lEdit_teach_name.setObjectName("lEdit_teach_name_" + id_sub)
        gL_widget_sub_teach.addWidget(lEdit_teach_name, 1, 1)

        if sel_sub:
            _db = ARMDataBase()
            _sql = "SELECT sub_name, id_teacher FROM subjects WHERE id_sub=" + id_sub
            sub_info = _db.query(_sql)
            lEdit_sub_name.setText(sub_info[0][0])

            _sql = "SELECT teacher_name FROM teachers WHERE id_teacher=" + str(sub_info[0][1])
            teach_info = _db.query(_sql)
            lEdit_teach_name.setText(teach_info[0][0])

            _db.close()

        self.outpr_ui.gL_widget_subs_teachs.addWidget(widget_sub_teach, i, j)

        return widget_sub_teach

    def save_calculate_values(self):
        i = 0
        for widget_calcbox in self.outlay_ui.widget_calcs.children():
            if widget_calcbox.objectName().startswith("widget_calcbox_") and i < 4:
                for child in widget_calcbox.children():
                    if child.objectName().startswith("spin_studs_"):
                        self.outlay_ui.variability_list[i][0] = child.value()
                    elif child.objectName().startswith("spin_price_"):
                        self.outlay_ui.variability_list[i][1] = child.value()
                    elif child.objectName().startswith("spin_tax_"):
                        self.outlay_ui.variability_list[i][2] = child.value()
                    elif child.objectName().startswith("spin_hours_"):
                        self.outlay_ui.variability_list[i][3] = child.value()
                    elif child.objectName().startswith("radio_variability_studs_") and child.isChecked():
                        self.outlay_ui.variability_list[i][4] = "radio_variability_studs_"
                    elif child.objectName().startswith("radio_variability_price_") and child.isChecked():
                        self.outlay_ui.variability_list[i][4] = "radio_variability_price_"
                    elif child.objectName().startswith("radio_variability_tax_") and child.isChecked():
                        self.outlay_ui.variability_list[i][4] = "radio_variability_tax_"
                    elif child.objectName().startswith("check_auto_"):
                        self.outlay_ui.variability_list[i][5] = child.isChecked()
                i += 1

    def load_calculate_values(self):
        i = 0
        j = 0
        for widget_calcbox in self.outlay_ui.widget_calcs.children():
            if widget_calcbox.objectName().startswith("widget_calcbox_"):
                if j < self.outlay_ui.calcs_before:
                    j += 1
                else:
                    for child in widget_calcbox.children():
                        if child.objectName().startswith("spin_studs_") and self.outlay_ui.variability_list[i][0] != "":
                            child.setValue(self.outlay_ui.variability_list[i][0])
                        elif child.objectName().startswith("spin_price_") and self.outlay_ui.variability_list[i][1] != "":
                            child.setValue(self.outlay_ui.variability_list[i][1])
                        elif child.objectName().startswith("spin_tax_") and self.outlay_ui.variability_list[i][2] != "":
                            child.setValue(self.outlay_ui.variability_list[i][2])
                        elif child.objectName().startswith("spin_hours_") and self.outlay_ui.variability_list[i][3] != "":
                            child.setValue(self.outlay_ui.variability_list[i][3])
                        elif self.outlay_ui.variability_list[i][4] in child.objectName() and self.outlay_ui.variability_list[i][4] != "":
                            child.setChecked(True)
                        elif child.objectName().startswith("check_auto_") and self.outlay_ui.variability_list[i][5] != "":
                            child.setChecked(self.outlay_ui.variability_list[i][5])
                    i += 1
        self.outlay_check_click()

    def calculate_values(self):
        price = [0, 0, 0, 0]
        studs = [0, 0, 0, 0]
        hours = [0, 0, 0, 0]
        tax = [0, 0, 0, 0]
        profit = 0
        cost = 0
        i = 0
        for widget_calcbox in self.outlay_ui.widget_calcs.children():
            if widget_calcbox.objectName().startswith("widget_calcbox_") and i < 4:
                if widget_calcbox.findChild(QtWidgets.QCheckBox, "check_auto_" + widget_calcbox.objectName().split("_")[-1]).isChecked():
                    for child in widget_calcbox.children():
                        if child.objectName().startswith("radio_variability_tax_") \
                                and child.isChecked() \
                                and widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_hours_" + widget_calcbox.objectName().split("_")[-1]).value() != 0:
                            widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_tax_" + widget_calcbox.objectName().split("_")[-1]).setValue(round(
                                (1/2*
                                 widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_price_" + widget_calcbox.objectName().split("_")[-1]).value() *
                                 widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_studs_" + widget_calcbox.objectName().split("_")[-1]).value()) /
                                widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_hours_" + widget_calcbox.objectName().split("_")[-1]).value()))
                        elif child.objectName().startswith("radio_variability_price_") \
                                and child.isChecked() \
                                and widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_studs_" + widget_calcbox.objectName().split("_")[-1]).value() != 0:
                            widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_price_" + widget_calcbox.objectName().split("_")[-1]).setValue(round(
                                (2*
                                 widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_tax_" + widget_calcbox.objectName().split("_")[-1]).value() *
                                 widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_hours_" + widget_calcbox.objectName().split("_")[-1]).value()) /
                                widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_studs_" + widget_calcbox.objectName().split("_")[-1]).value()))
                        elif child.objectName().startswith("radio_variability_studs_") \
                                and child.isChecked() \
                                and widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_price_" + widget_calcbox.objectName().split("_")[-1]).value() != 0:
                            widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_studs_" + widget_calcbox.objectName().split("_")[-1]).setValue(round(
                                (2*
                                 widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_hours_" + widget_calcbox.objectName().split("_")[-1]).value() *
                                 widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_tax_" + widget_calcbox.objectName().split("_")[-1]).value()) /
                                widget_calcbox.findChild(QtWidgets.QSpinBox, "spin_price_" + widget_calcbox.objectName().split("_")[-1]).value()))
                i += 1
        i = 0
        for widget_calcbox in self.outlay_ui.widget_calcs.children():
            if widget_calcbox.objectName().startswith("widget_calcbox_") and i < 4:
                for child in widget_calcbox.children():
                    if child.objectName().startswith("spin_studs_"):
                        studs[i] = child.value()
                    elif child.objectName().startswith("spin_price_"):
                        price[i] = child.value()
                    elif child.objectName().startswith("spin_tax_"):
                        tax[i] = child.value()
                    elif child.objectName().startswith("spin_hours_"):
                        hours[i] = child.value()
                i += 1
        for j in range(i):
            profit += price[j] * studs[j]
            cost += (hours[j] * tax[j]) * 1.302
        self.outlay_ui.label_profit.setText("Доходы = " + str(profit) + " рублей")
        self.outlay_ui.label_cost.setText("Оплата часов + ФОТ = " + str(round(cost, 2)) + " рублей")
        if profit != 0:
            self.outlay_ui.label_otfot.setText("Оплата часов + ФОТ % = " + str(round(cost / profit * 100, 2)) + "%")

    def outlay_check_click(self):
        for widget_calcbox in self.outlay_ui.widget_calcs.children():
            if widget_calcbox.objectName().startswith("widget_calcbox_"):
                for child in widget_calcbox.children():
                    if child.objectName().startswith("check_auto_") \
                            and child.isChecked():
                        widget_calcbox.findChild(QtWidgets.QRadioButton, "radio_variability_tax_" + widget_calcbox.objectName().split("_")[-1]).setEnabled(True)
                        widget_calcbox.findChild(QtWidgets.QRadioButton, "radio_variability_price_" + widget_calcbox.objectName().split("_")[-1]).setEnabled(True)
                        widget_calcbox.findChild(QtWidgets.QRadioButton, "radio_variability_studs_" + widget_calcbox.objectName().split("_")[-1]).setEnabled(True)
                    elif child.objectName().startswith("check_auto_") \
                            and not child.isChecked():
                        widget_calcbox.findChild(QtWidgets.QRadioButton, "radio_variability_tax_" + widget_calcbox.objectName().split("_")[-1]).setEnabled(False)
                        widget_calcbox.findChild(QtWidgets.QRadioButton, "radio_variability_price_" + widget_calcbox.objectName().split("_")[-1]).setEnabled(False)
                        widget_calcbox.findChild(QtWidgets.QRadioButton, "radio_variability_studs_" + widget_calcbox.objectName().split("_")[-1]).setEnabled(False)


def create_outlay(outlay_data):
    thread_list = []
    task = threading.Thread(target=OutlayCreate(), args=(outlay_data,))
    thread_list.append(task)
    task.deamon = True
    task.start()


class OutlayCreate:
    def __call__(self, outlay_data):
        path, filename = create_outlay_doc(outlay_data)


def create_outlay_doc(outlay_data):
    path = os.getcwd() + r"/Документы/Прочие/"

    _db = ARMDataBase('arm_db.db')

    _db.close()

    doc = docx.Document()

    doc.sections[-1].orientation = docx.enum.section.WD_ORIENTATION.PORTRAIT
    doc.sections[-1].page_height = docx.shared.Cm(21)
    doc.sections[-1].page_width = docx.shared.Cm(29.7)
    doc.sections[-1].top_margin = docx.shared.Cm(1.3)
    doc.sections[-1].right_margin = docx.shared.Cm(1)
    doc.sections[-1].left_margin = docx.shared.Cm(1)
    doc.sections[-1].bottom_margin = docx.shared.Cm(1)

    doc.add_paragraph(group_name + " " + timetable[0][1])
    doc.paragraphs[0].runs[0].bold = True
    doc.paragraphs[0].runs[0].font.name = "Times New Roman"
    doc.paragraphs[0].runs[0].font.size = docx.shared.Pt(14)

    properties = doc.core_properties
    properties.author = "ЦПЮИ ХТИ"

    doc.save(path + filename)
    return path, filename


def create_timetable(sub):
    thread_list = []
    task = threading.Thread(target=TimetableCreate(), args=(sub,))
    thread_list.append(task)
    task.deamon = True
    task.start()


class TimetableCreate:
    def __call__(self, sub):
        path, filename = create_timetable_doc(sub)


def create_timetable_doc(_sub):
    path = os.getcwd() + r"/Документы/Прочие/"

    _db = ARMDataBase('arm_db.db')

    _sql = "SELECT sub_ttable, sub_name, id_prog FROM subjects WHERE id_sub=" + _sub
    timetable = _db.query(_sql)

    _sql = "SELECT group_name FROM groups WHERE id_prog=" + str(timetable[0][2])
    group_name = _db.query(_sql)[0][0]

    _sql = "SELECT id_student FROM subs_in_studs WHERE id_sub=" + _sub
    students_q = _db.query(_sql)
    students = []

    copy_index = 0
    filename = "Расписание " + group_name + " " + timetable[0][1] + ".docx"
    desk_list_dir = os.listdir(path)
    while filename in desk_list_dir:
        copy_index += 1
        filename = "Расписание " + group_name + " " + timetable[0][1] + " (" + str(copy_index) + ").docx"

    for i in range(len(students_q)):
        students.append([str(students_q[i][0])])
        _sql = "SELECT student_name FROM students WHERE id_student=" + str(students_q[i][0])
        students[i].append(_db.query(_sql)[0][0])

    _db.close()

    students.sort(key=lambda x: x[1])

    parse_timetable = []
    if timetable[0][0] is not None and timetable[0][0] != '':
        for date in timetable[0][0].split(","):
            parse_timetable.append(date)
        for i in range(len(parse_timetable)):
            parse_timetable[i] = parse_timetable[i].split("|")
            parse_timetable[i][0] = datetime.datetime.strptime(parse_timetable[i][0], "%d.%m.%Y")
            if parse_timetable[i][0].weekday() == 0:
                parse_timetable[i].append('Понедельник')
            elif parse_timetable[i][0].weekday() == 1:
                parse_timetable[i].append('Вторник')
            elif parse_timetable[i][0].weekday() == 2:
                parse_timetable[i].append('Среда')
            elif parse_timetable[i][0].weekday() == 3:
                parse_timetable[i].append('Четверг')
            elif parse_timetable[i][0].weekday() == 4:
                parse_timetable[i].append('Пятница')
            elif parse_timetable[i][0].weekday() == 5:
                parse_timetable[i].append('Суббота')
            elif parse_timetable[i][0].weekday() == 6:
                parse_timetable[i].append('Воскресенье')

            if parse_timetable[i][0].strftime("%m") == "01":
                parse_timetable[i].append('Января')
            elif parse_timetable[i][0].strftime("%m") == "02":
                parse_timetable[i].append('Февраля')
            elif parse_timetable[i][0].strftime("%m") == "03":
                parse_timetable[i].append('Марта')
            elif parse_timetable[i][0].strftime("%m") == "04":
                parse_timetable[i].append('Апреля')
            elif parse_timetable[i][0].strftime("%m") == "05":
                parse_timetable[i].append('Мая')
            elif parse_timetable[i][0].strftime("%m") == "06":
                parse_timetable[i].append('Июня')
            elif parse_timetable[i][0].strftime("%m") == "07":
                parse_timetable[i].append('Июля')
            elif parse_timetable[i][0].strftime("%m") == "08":
                parse_timetable[i].append('Августа')
            elif parse_timetable[i][0].strftime("%m") == "09":
                parse_timetable[i].append('Сентября')
            elif parse_timetable[i][0].strftime("%m") == "10":
                parse_timetable[i].append('Октября')
            elif parse_timetable[i][0].strftime("%m") == "11":
                parse_timetable[i].append('Ноября')
            elif parse_timetable[i][0].strftime("%m") == "12":
                parse_timetable[i].append('Декабря')

    doc = docx.Document()

    doc.sections[-1].orientation = docx.enum.section.WD_ORIENTATION.PORTRAIT
    doc.sections[-1].page_height = docx.shared.Cm(21)
    doc.sections[-1].page_width = docx.shared.Cm(29.7)
    doc.sections[-1].top_margin = docx.shared.Cm(1.3)
    doc.sections[-1].right_margin = docx.shared.Cm(1)
    doc.sections[-1].left_margin = docx.shared.Cm(1)
    doc.sections[-1].bottom_margin = docx.shared.Cm(1)

    doc.add_paragraph(group_name + " " + timetable[0][1])
    doc.paragraphs[0].runs[0].bold = True
    doc.paragraphs[0].runs[0].font.name = "Times New Roman"
    doc.paragraphs[0].runs[0].font.size = docx.shared.Pt(14)

    tabs_c = str(len(parse_timetable) / 22).split(".")

    if tabs_c[1] != "0":
        tabs_c = int(tabs_c[0]) + 1
    else:
        tabs_c = int(tabs_c[0])

    if len(parse_timetable) - (22 * (tabs_c - 1)) <= 10:
        len_date = 27
    else:
        len_date = 22

    tabs_c = str(len(parse_timetable) / len_date).split(".")

    if tabs_c[1] != "0":
        tabs_c = int(tabs_c[0]) + 1
    else:
        tabs_c = int(tabs_c[0])

    table_timetable_list = []

    for i in range(tabs_c):
        if tabs_c == 1:
            table_timetable = doc.add_table(rows=1 + len(students), cols=2 + len(parse_timetable), style='Table Grid')
            table_timetable_list.append(table_timetable)
        elif i + 1 != tabs_c:
            table_timetable = doc.add_table(rows=1 + len(students), cols=2 + len_date, style='Table Grid')
            table_timetable_list.append(table_timetable)
            par = doc.add_paragraph('_')
            if len(students) > 13:
                par.runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)
            else:
                par.runs[0].font.size = docx.shared.Pt(1)
                par.paragraph_format.space_after = docx.shared.Pt(0)
                par.paragraph_format.line_spacing_rule = docx.enum.text.WD_LINE_SPACING.SINGLE
        else:
            table_timetable = doc.add_table(rows=1 + len(students),
                                            cols=2 + len(parse_timetable) - (len_date * (tabs_c - 1)),
                                            style='Table Grid')
            table_timetable_list.append(table_timetable)

    for i in range(len(table_timetable_list)):
        for row in range(len(table_timetable_list[i].rows)):
            for col in range(len(table_timetable_list[i].columns)):
                cell = table_timetable_list[i].cell(row, col)
                if row == 0 and col == 0:
                    cell.text = "№\nп\\п"
                    cell.paragraphs[0].runs[0].bold = True
                    cell.paragraphs[0].runs[0].font.name = "Times New Roman"
                    cell.paragraphs[0].runs[0].font.size = docx.shared.Pt(10)
                    cell.paragraphs[0].paragraph_format.line_spacing_rule = docx.enum.text.WD_LINE_SPACING.SINGLE
                    cell.paragraphs[0].alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
                    cell.paragraphs[0].paragraph_format.space_after = docx.shared.Pt(0)
                    cell.width = docx.shared.Cm(0.89)
                    cell.vertical_alignment = docx.enum.table.WD_ALIGN_VERTICAL.CENTER
                elif row == 0 and col == 1:
                    cell.text = "ФИО"
                    cell.paragraphs[0].runs[0].bold = True
                    cell.paragraphs[0].runs[0].font.name = "Times New Roman"
                    cell.paragraphs[0].runs[0].font.size = docx.shared.Pt(10)
                    cell.paragraphs[0].paragraph_format.line_spacing_rule = docx.enum.text.WD_LINE_SPACING.SINGLE
                    cell.paragraphs[0].alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
                    cell.paragraphs[0].paragraph_format.space_after = docx.shared.Pt(0)
                    cell.width = docx.shared.Cm(5.5)
                    cell.vertical_alignment = docx.enum.table.WD_ALIGN_VERTICAL.CENTER
                elif row > 0 and col == 0:
                    cell.text = str(row) + "."
                    cell.paragraphs[0].runs[0].font.name = "Times New Roman"
                    cell.paragraphs[0].runs[0].font.size = docx.shared.Pt(10)
                    cell.paragraphs[0].paragraph_format.line_spacing_rule = docx.enum.text.WD_LINE_SPACING.SINGLE
                    cell.paragraphs[0].paragraph_format.space_after = docx.shared.Pt(0)
                    cell.width = docx.shared.Cm(0.89)
                    table_timetable_list[i].rows[row].height = docx.shared.Cm(0.4)
                    cell.vertical_alignment = docx.enum.table.WD_ALIGN_VERTICAL.CENTER
                elif row > 0 and col == 1:
                    cell.text = students[row - 1][1]
                    cell.paragraphs[0].runs[0].font.name = "Times New Roman"
                    cell.paragraphs[0].runs[0].font.size = docx.shared.Pt(10)
                    cell.paragraphs[0].paragraph_format.line_spacing_rule = docx.enum.text.WD_LINE_SPACING.SINGLE
                    cell.paragraphs[0].paragraph_format.space_after = docx.shared.Pt(0)
                    cell.width = docx.shared.Cm(5.8)
                    cell.vertical_alignment = docx.enum.table.WD_ALIGN_VERTICAL.TOP
                elif row == 0 and col > 1:
                    cell.text = parse_timetable[0][0].strftime("%d")[1:] \
                        if parse_timetable[0][0].strftime("%d").startswith("0") \
                        else parse_timetable[0][0].strftime("%d")
                    cell.text += " " + parse_timetable[0][3]
                    parse_timetable.pop(0)
                    cell.paragraphs[0].runs[0].bold = True
                    cell.paragraphs[0].runs[0].font.name = "Times New Roman"
                    cell.paragraphs[0].runs[0].font.size = docx.shared.Pt(10)
                    cell.paragraphs[0].paragraph_format.line_spacing_rule = docx.enum.text.WD_LINE_SPACING.SINGLE
                    cell.paragraphs[0].paragraph_format.space_after = docx.shared.Pt(0)
                    cell.paragraphs[0].paragraph_format.left_indent = docx.shared.Cm(0.2)
                    cell.paragraphs[0].paragraph_format.right_indent = docx.shared.Cm(0.2)
                    cell.width = docx.shared.Cm(0.81)
                    table_timetable_list[i].rows[row].height = docx.shared.Cm(2.5)
                    cell.vertical_alignment = docx.enum.table.WD_ALIGN_VERTICAL.CENTER
                    set_vertical_cell_direction(cell, "btLr")
                else:
                    cell.text = ""
                    cell.paragraphs[0].runs[0].font.name = "Times New Roman"
                    cell.paragraphs[0].runs[0].font.size = docx.shared.Pt(10)
                    cell.paragraphs[0].paragraph_format.line_spacing_rule = docx.enum.text.WD_LINE_SPACING.SINGLE
                    cell.paragraphs[0].paragraph_format.space_after = docx.shared.Pt(0)
                    cell.width = docx.shared.Cm(0.81)
                    table_timetable_list[i].rows[row].height = docx.shared.Cm(0.4)
                    cell.vertical_alignment = docx.enum.table.WD_ALIGN_VERTICAL.CENTER

    properties = doc.core_properties
    properties.author = "ЦПЮИ ХТИ"

    doc.save(path + filename)
    return path, filename


# Set font vertical direction in docx
def set_vertical_cell_direction(cell: _Cell, direction: str):
    # direction: tbRl -- top to bottom, btLr -- bottom to top
    assert direction in ("tbRl", "btLr")
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    textDirection = OxmlElement('w:textDirection')
    textDirection.set(qn('w:val'), direction)  # btLr tbRl
    tcPr.append(textDirection)


# Clearing edit list
def clear_list(children_list):
    for i in children_list:
        if i.objectName().startswith('clb_'):
            i.setAttribute(55, 1)
            i.close()


# Clearing edit groupBox
def clear_group_box(group_box):
    for i in group_box:
        if i.objectName().startswith('el_') or i.objectName().startswith('grB_'):
            i.setAttribute(55, 1)
            i.close()


# Clearing widget
def clear_widget(widget):
    for i in widget:
        if i.objectName().startswith('widget_'):
            i.setAttribute(55, 1)
            i.close()


# Func for print docs
def print_doc(filepath, filename):
    f = '"' + filepath + filename + '"'
    win32api.ShellExecute(0, "printto", f, '"%s"' % win32print.GetDefaultPrinter(), ".", 0)


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
