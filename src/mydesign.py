# Form implementation generated from reading ui file 'sortimagefile.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(476, 240))
        MainWindow.setMaximumSize(QtCore.QSize(476, 240))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon.fromTheme("icon.ico")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 441, 71))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 421, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(300, 40, 131, 23))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 40, 201, 17))
        self.checkBox.setObjectName("checkBox")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 441, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 421, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 40, 131, 23))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 70, 61, 17))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setTristate(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(90, 70, 71, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.checkBox_4.setGeometry(QtCore.QRect(180, 70, 61, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 50, 151, 16))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 190, 131, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox_5 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 180, 211, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #def retranslateUi(self, MainWindow):
        #_translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_("Sort image and video files by time"))
        #self.groupBox.setTitle(_( "Directory with source files"))
        #self.pushButton.setText(_( "Directory selection"))
        #self.checkBox.setText(_( "Including sub directories"))
        #self.groupBox_2.setTitle(_( "Directory for saving files"))
        #self.pushButton_2.setText(_( "Directory selection"))
        #self.checkBox_2.setText(_(, "years"))
        #self.checkBox_3.setText(_(, "months"))
        #self.checkBox_4.setText(_(, "days"))
        #self.label.setText(_( "Sort files by"))
        #self.pushButton_3.setText(_( "Start sorting"))
        #self.checkBox_5.setText(_( "Create log.txt"))
#self.checkBox_5.setText(_translate("MainWindow", "Create log.txt"))