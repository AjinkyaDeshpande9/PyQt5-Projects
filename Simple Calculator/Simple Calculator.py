from cgitb import text
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 516)
        MainWindow.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(156, 156, 156);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 190, 39);\n"
"    border-radius:20px;\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 5, 3, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)
        self.btn_mod = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_mod.sizePolicy().hasHeightForWidth())
        self.btn_mod.setSizePolicy(sizePolicy)
        self.btn_mod.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(156, 156, 156);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 190, 39);\n"
"    border-radius:20px;\n"
"}")
        self.btn_mod.setObjectName("btn_mod")
        self.gridLayout.addWidget(self.btn_mod, 1, 2, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy)
        self.btn_equal.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(156, 156, 156);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 190, 39);\n"
"    border-radius:20px;\n"
"}")
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout.addWidget(self.btn_equal, 6, 3, 1, 1)
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy)
        self.btn_sub.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(156, 156, 156);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 190, 39);\n"
"    border-radius:20px;\n"
"}")
        self.btn_sub.setObjectName("btn_sub")
        self.gridLayout.addWidget(self.btn_sub, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";\n"
"color  :rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 4, 2, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 4, 0, 1, 1)
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy)
        self.btn_mul.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(156, 156, 156);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 190, 39);\n"
"    border-radius:20px;\n"
"}")
        self.btn_mul.setObjectName("btn_mul")
        self.gridLayout.addWidget(self.btn_mul, 3, 3, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 4, 1, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 6, 0, 1, 2)
        self.btn_decimal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_decimal.sizePolicy().hasHeightForWidth())
        self.btn_decimal.setSizePolicy(sizePolicy)
        self.btn_decimal.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_decimal.setObjectName("btn_decimal")
        self.gridLayout.addWidget(self.btn_decimal, 6, 2, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(156, 156, 156);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 190, 39);\n"
"    border-radius:20px;\n"
"}\n"
"")
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 1, 3, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 5, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(156, 156, 156);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(85, 0, 127);\n"
"    border-radius:20px;\n"
"}")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 1, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 5, 1, 1, 1)
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        self.btn_del.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(156, 156, 156);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(85, 0, 127);\n"
"    border-radius:20px;\n"
"}")
        self.btn_del.setObjectName("btn_del")
        self.gridLayout.addWidget(self.btn_del, 1, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setStyleSheet("QPushButton{\n"
"    font: 18pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(193, 193, 193);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(24, 116, 255);\n"
"    border-radius:20px;\n"
"}")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_1.clicked.connect(self.method_1)
        self.btn_2.clicked.connect(self.method_2)
        self.btn_3.clicked.connect(self.method_3)
        self.btn_4.clicked.connect(self.method_4)
        self.btn_5.clicked.connect(self.method_5)
        self.btn_6.clicked.connect(self.method_6)
        self.btn_7.clicked.connect(self.method_7)
        self.btn_8.clicked.connect(self.method_8)
        self.btn_9.clicked.connect(self.method_9)
        self.btn_0.clicked.connect(self.method_0)
        self.btn_decimal.clicked.connect(self.method_decimal)
        self.btn_equal.clicked.connect(self.method_equal)
        self.btn_add.clicked.connect(self.method_add)
        self.btn_sub.clicked.connect(self.method_sub)
        self.btn_mul.clicked.connect(self.method_mul)
        self.btn_div.clicked.connect(self.method_div)
        self.btn_mod.clicked.connect(self.method_mod)
        self.btn_clear.clicked.connect(self.method_clear)
        self.btn_del.clicked.connect(self.method_del)

    def method_1(self):
                text=self.label.text()
                self.label.setText(text+"1")

    def method_2(self):
                text=self.label.text()
                self.label.setText(text+"2")
        
    def method_3(self):
                text=self.label.text()
                self.label.setText(text+"3")
        
    def method_4(self):
                text=self.label.text()
                self.label.setText(text+"4")
        
    def method_5(self):
                text=self.label.text()
                self.label.setText(text+"5")

    def method_6(self):
                text=self.label.text()
                self.label.setText(text+"6")
        
    def method_7(self):
                text=self.label.text()
                self.label.setText(text+"7")

    def method_8(self):
                text=self.label.text()
                self.label.setText(text+"8")

    def method_9(self):
                text=self.label.text()
                self.label.setText(text+"9")

    def method_0(self):
                text=self.label.text()
                self.label.setText(text+"0")
    def method_decimal(self):
                text=self.label.text()
                self.label.setText(text+".")
        
    def method_add(self):
                text=self.label.text()
                self.label.setText(text+"+")
        
    def method_sub(self):
                text=self.label.text()
                self.label.setText(text+"-")
        
    def method_mul(self):
                text=self.label.text()
                self.label.setText(text+"*")
        
    def method_div(self):
                text=self.label.text()
                self.label.setText(text+"/")
        
    def method_mod(self):
                text=self.label.text()
                self.label.setText(text+"%")
        
    def method_clear(self):
                self.label.setText("")
        
    def method_del(self):
                text=self.label.text()
                self.label.setText(text[:len(text)-1])
        
    def method_equal(self):
                text=self.label.text()

                try:
                        ans = eval((text))
                        self.label.setText(str(ans))
                except:
                        self.label.setText("Error")
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_add.setShortcut(_translate("MainWindow", "+"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_mod.setText(_translate("MainWindow", "mod"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_sub.setShortcut(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_mul.setText(_translate("MainWindow", "x"))
        self.btn_mul.setShortcut(_translate("MainWindow", "*"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_decimal.setText(_translate("MainWindow", "."))
        self.btn_div.setText(_translate("MainWindow", "÷"))
        self.btn_div.setShortcut(_translate("MainWindow", "/"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_clear.setText(_translate("MainWindow", "AC"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_del.setText(_translate("MainWindow", "Del"))
        self.btn_del.setShortcut(_translate("MainWindow", "Backspace"))
        self.btn_3.setText(_translate("MainWindow", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
