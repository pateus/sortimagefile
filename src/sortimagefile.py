import gettext
import locale
import os
import shutil
import sys
from datetime import datetime
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from win32_setctime import setctime

from mydesign import Ui_MainWindow

loc = locale.getlocale()
extDataDir = os.getcwd()

try:
    extDataDir = sys._MEIPASS
except Exception:
    extDataDir = os.getcwd()
localedir = os.path.join(extDataDir, 'locale')
if loc[0] == 'Russian_Russia':
    ru = gettext.translation('sortimagefile', localedir, languages=['ru'])
    ru.install()
    _ = ru.gettext
else:
    en = gettext.translation('sortimagefile', localedir, languages=['en'])
    en.install()
    _ = en.gettext

error_log = list()
directory = set()
image_list = (
    'jpg', 'png', 'bmp', 'ai', 'psd', 'jpeg', 'ps', 'svg', 'tif', 'tiff', 'mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp',
    '3g2',
    'mpg', 'mpeg', 'm4v',
    'h264', 'flv', 'rm', 'swf', 'vob')

def read_catalogs(self, dir_name):
    try:

        count = 0  # счетчик файлов в директории

        files = os.scandir(dir_name)
        for file in files:
            if file.is_file() and str(file.name).endswith(image_list):
                c_time = os.path.getctime(file)  # дата создания файла
                datafile = datetime.fromtimestamp(c_time).strftime("%Y %m %d")
                datafile_list = datafile.split()
                # print(datafile_list)

                newfile = self.ui.lineEdit_2.text()
                if self.ui.checkBox_2.isChecked():
                    newfile = os.path.join(newfile, datafile_list[0])
                    if not dir_c(newfile):
                        return
                if self.ui.checkBox_3.isChecked():
                    newfile = os.path.join(newfile, datafile_list[0] + '-' + datafile_list[1])
                    if not dir_c(newfile):
                        return
                if self.ui.checkBox_4.isChecked():
                    newfile = os.path.join(newfile,
                                           datafile_list[0] + '-' + datafile_list[1] + '-' + datafile_list[2])
                    if not dir_c(newfile):
                        return

                # print(newfile)
                shutil.copy2(file, newfile)
                newfile = os.path.join(newfile, str(file.name))
                setctime(newfile, c_time)
                # Выводим в статусбар имя обрабатываемой директории и количество обработанных файлов в ней
                count = count + 1
                self.statusBar().clearMessage()
                if len(dir_name) < 60:
                    self.statusBar().showMessage(dir_name + ': ' + str(count))
                else:
                    self.statusBar().showMessage('*' + dir_name[-60:] + ': ' + str(count))
                app.processEvents()
            # ------------------------------------------------------------------------------------------
            if file.is_dir() and self.ui.checkBox.isChecked():  # обработка вложенных директорий
                read_catalogs(file.path, self)

        files.close()
    except Exception as err:
        error_log.append(str(datetime.now()) + ' ' + str(err))


def dir_c(d):
    try:
        if d in directory:
            return True
        else:
            if os.path.exists(d):

                directory.add(d)
                return True
            else:
                try:
                    os.mkdir(d)
                except OSError:
                    error_log.append(str(datetime.now()) + _(" Failed to create directory %s") % d)
                else:
                    directory.add(d)
                    error_log.append(str(datetime.now()) + _(" Directory %s created") % d)
                    return True
    except Exception as err:
        error_log.append(str(datetime.now()) + ' ' + str(err))
        return False


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        icon = QtGui.QIcon("icon.ico")
        self.setWindowIcon(icon)

        self.setWindowTitle(_("Sort image and video files by time"))
        self.ui.groupBox.setTitle(_("Directory with source files"))
        self.ui.pushButton.setText(_("Directory selection"))
        self.ui.checkBox.setText(_("Including sub directories"))
        self.ui.groupBox_2.setTitle(_("Directory for saving files"))
        self.ui.pushButton_2.setText(_("Directory selection"))
        self.ui.checkBox_2.setText(_("years"))
        self.ui.checkBox_3.setText(_("months"))
        self.ui.checkBox_4.setText(_("days"))
        self.ui.label.setText(_("Sort files by"))
        self.ui.pushButton_3.setText(_("Start sorting"))
        self.ui.checkBox_5.setText(_("Create log.txt"))

        # События для кнопок
        self.ui.pushButton.clicked.connect(self.on_click1)
        self.ui.pushButton_2.clicked.connect(self.on_click2)
        self.ui.pushButton_3.clicked.connect(self.on_click3)

    def on_click1(self):
        dir1 = QFileDialog.getExistingDirectory(self, _("Select a directory with source files"))
        if dir1:
            dir1 = QtCore.QDir.toNativeSeparators(dir1)
            self.ui.lineEdit.setText(dir1)

    def on_click2(self):
        dir2 = QFileDialog.getExistingDirectory(self, _("Choose a directory to save files"))
        if dir2:
            dir2 = QtCore.QDir.toNativeSeparators(dir2)
            self.ui.lineEdit_2.setText(dir2)

    def on_click3(self):
        self.statusBar().clearMessage()
        dir1 = self.ui.lineEdit.text()
        dir2 = self.ui.lineEdit_2.text()
        ln1 = len(dir1)
        ln2 = len(dir2)
        if ln1 == 0:
            self.statusBar().showMessage(_("Source files directory not selected"))
            return
        if ln2 == 0:
            self.statusBar().showMessage(_("The directory for saving files is not selected"))
            return

        if os.path.commonpath([dir1, dir2]) == dir1:
            self.statusBar().showMessage(_("Directories match"))
            return

        if not (self.ui.checkBox_2.isChecked() or self.ui.checkBox_3.isChecked() or self.ui.checkBox_4.isChecked()):
            self.statusBar().showMessage(_("Select temporary sort options"))
            return
        error_log.clear()
        directory.clear()
        error_log.append(str(datetime.now()) + _(" Start sorting ") + dir1)
        read_catalogs(self, dir1)
        # print(error_log)
        try:
            if self.ui.checkBox_5.isChecked():
                file = open(os.path.join(self.ui.lineEdit_2.text(), "log.txt"), "w")
                for line in error_log:
                    file.write(line + "\n")
                file.close()
        except Exception as err:
            print(str(err))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
