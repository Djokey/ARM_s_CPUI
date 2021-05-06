import win32api
import win32print


def print_file(filename, filepath):
    f = filepath + filename
    win32api.ShellExecute(0, "printto", f, '"%s"' % win32print.GetDefaultPrinter(), ".", 0)


print_file(r'служебная записка на пароли.docx"', r'"D:/Projects/ARM_s_CPUI/docx/')

