# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(367, 478)
        self.b1 = QtGui.QPushButton(Dialog)
        self.b1.setGeometry(QtCore.QRect(10, 230, 61, 51))
        self.b1.setObjectName(_fromUtf8("b1"))
        self.b3 = QtGui.QPushButton(Dialog)
        self.b3.setGeometry(QtCore.QRect(150, 230, 61, 51))
        self.b3.setObjectName(_fromUtf8("b3"))
        self.b2 = QtGui.QPushButton(Dialog)
        self.b2.setGeometry(QtCore.QRect(80, 230, 61, 51))
        self.b2.setObjectName(_fromUtf8("b2"))
        self.b6 = QtGui.QPushButton(Dialog)
        self.b6.setGeometry(QtCore.QRect(150, 170, 61, 51))
        self.b6.setObjectName(_fromUtf8("b6"))
        self.b5 = QtGui.QPushButton(Dialog)
        self.b5.setGeometry(QtCore.QRect(80, 170, 61, 51))
        self.b5.setObjectName(_fromUtf8("b5"))
        self.b4 = QtGui.QPushButton(Dialog)
        self.b4.setGeometry(QtCore.QRect(10, 170, 61, 51))
        self.b4.setObjectName(_fromUtf8("b4"))
        self.b9 = QtGui.QPushButton(Dialog)
        self.b9.setGeometry(QtCore.QRect(150, 110, 61, 51))
        self.b9.setObjectName(_fromUtf8("b9"))
        self.b8 = QtGui.QPushButton(Dialog)
        self.b8.setGeometry(QtCore.QRect(80, 110, 61, 51))
        self.b8.setObjectName(_fromUtf8("b8"))
        self.b7 = QtGui.QPushButton(Dialog)
        self.b7.setGeometry(QtCore.QRect(10, 110, 61, 51))
        self.b7.setObjectName(_fromUtf8("b7"))
        self.plus_minus = QtGui.QPushButton(Dialog)
        self.plus_minus.setGeometry(QtCore.QRect(80, 290, 61, 51))
        self.plus_minus.setObjectName(_fromUtf8("plus_minus"))
        self.b0 = QtGui.QPushButton(Dialog)
        self.b0.setGeometry(QtCore.QRect(10, 290, 61, 51))
        self.b0.setObjectName(_fromUtf8("b0"))
        self.decimal = QtGui.QPushButton(Dialog)
        self.decimal.setGeometry(QtCore.QRect(150, 290, 61, 51))
        self.decimal.setObjectName(_fromUtf8("decimal"))
        self.display = QtGui.QLineEdit(Dialog)
        self.display.setGeometry(QtCore.QRect(10, 20, 341, 71))
        self.display.setObjectName(_fromUtf8("display"))
        self.equal = QtGui.QPushButton(Dialog)
        self.equal.setGeometry(QtCore.QRect(220, 290, 61, 51))
        self.equal.setObjectName(_fromUtf8("equal"))
        self.clear = QtGui.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(220, 110, 131, 51))
        self.clear.setObjectName(_fromUtf8("clear"))
        self.add = QtGui.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(220, 170, 61, 51))
        self.add.setObjectName(_fromUtf8("add"))
        self.substract = QtGui.QPushButton(Dialog)
        self.substract.setGeometry(QtCore.QRect(220, 230, 61, 51))
        self.substract.setObjectName(_fromUtf8("substract"))
        self.divide = QtGui.QPushButton(Dialog)
        self.divide.setGeometry(QtCore.QRect(290, 230, 61, 51))
        self.divide.setObjectName(_fromUtf8("divide"))
        self.multiply = QtGui.QPushButton(Dialog)
        self.multiply.setGeometry(QtCore.QRect(290, 170, 61, 51))
        self.multiply.setObjectName(_fromUtf8("multiply"))
        self.sq_root = QtGui.QPushButton(Dialog)
        self.sq_root.setGeometry(QtCore.QRect(290, 290, 61, 51))
        self.sq_root.setObjectName(_fromUtf8("sq_root"))
        self.sin = QtGui.QPushButton(Dialog)
        self.sin.setGeometry(QtCore.QRect(10, 350, 61, 51))
        self.sin.setObjectName(_fromUtf8("sin"))
        self.cos = QtGui.QPushButton(Dialog)
        self.cos.setGeometry(QtCore.QRect(80, 350, 61, 51))
        self.cos.setObjectName(_fromUtf8("cos"))
        self.tan = QtGui.QPushButton(Dialog)
        self.tan.setGeometry(QtCore.QRect(150, 350, 61, 51))
        self.tan.setObjectName(_fromUtf8("tan"))
        self.power = QtGui.QPushButton(Dialog)
        self.power.setGeometry(QtCore.QRect(220, 350, 61, 51))
        self.power.setObjectName(_fromUtf8("power"))
        self.log = QtGui.QPushButton(Dialog)
        self.log.setGeometry(QtCore.QRect(290, 350, 61, 51))
        self.log.setObjectName(_fromUtf8("log"))
        self.b_open = QtGui.QPushButton(Dialog)
        self.b_open.setGeometry(QtCore.QRect(10, 410, 61, 51))
        self.b_open.setObjectName(_fromUtf8("b_open"))
        self.b_close = QtGui.QPushButton(Dialog)
        self.b_close.setGeometry(QtCore.QRect(80, 410, 61, 51))
        self.b_close.setObjectName(_fromUtf8("b_close"))
        self.ln = QtGui.QPushButton(Dialog)
        self.ln.setGeometry(QtCore.QRect(150, 410, 61, 51))
        self.ln.setObjectName(_fromUtf8("ln"))
        self.e = QtGui.QPushButton(Dialog)
        self.e.setGeometry(QtCore.QRect(220, 410, 61, 51))
        self.e.setObjectName(_fromUtf8("e"))
        self.pi = QtGui.QPushButton(Dialog)
        self.pi.setGeometry(QtCore.QRect(290, 410, 61, 51))
        self.pi.setObjectName(_fromUtf8("pi"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.b1.setText(_translate("Dialog", "1", None))
        self.b3.setText(_translate("Dialog", "3", None))
        self.b2.setText(_translate("Dialog", "2", None))
        self.b6.setText(_translate("Dialog", "6", None))
        self.b5.setText(_translate("Dialog", "5", None))
        self.b4.setText(_translate("Dialog", "4", None))
        self.b9.setText(_translate("Dialog", "9", None))
        self.b8.setText(_translate("Dialog", "8", None))
        self.b7.setText(_translate("Dialog", "7", None))
        self.plus_minus.setText(_translate("Dialog", "+/-", None))
        self.b0.setText(_translate("Dialog", "0", None))
        self.decimal.setText(_translate("Dialog", ".", None))
        self.equal.setText(_translate("Dialog", "=", None))
        self.clear.setText(_translate("Dialog", "AC", None))
        self.add.setText(_translate("Dialog", "+", None))
        self.substract.setText(_translate("Dialog", "-", None))
        self.divide.setText(_translate("Dialog", "/", None))
        self.multiply.setText(_translate("Dialog", "X", None))
        self.sq_root.setText(_translate("Dialog", "Sqrt", None))
        self.sin.setText(_translate("Dialog", "sin", None))
        self.cos.setText(_translate("Dialog", "cos", None))
        self.tan.setText(_translate("Dialog", "tan", None))
        self.power.setText(_translate("Dialog", "^", None))
        self.log.setText(_translate("Dialog", "log", None))
        self.b_open.setText(_translate("Dialog", "(", None))
        self.b_close.setText(_translate("Dialog", ")", None))
        self.ln.setText(_translate("Dialog", "ln", None))
        self.e.setText(_translate("Dialog", "e", None))
        self.pi.setText(_translate("Dialog", "π", None))
