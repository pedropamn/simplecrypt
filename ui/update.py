# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_updateDialog(object):
    def setupUi(self, updateDialog):
        updateDialog.setObjectName("updateDialog")
        updateDialog.resize(503, 484)
        self.downloadButton = QtWidgets.QPushButton(updateDialog)
        self.downloadButton.setGeometry(QtCore.QRect(160, 390, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.downloadButton.setFont(font)
        self.downloadButton.setObjectName("downloadButton")
        self.labelArea = QtWidgets.QLabel(updateDialog)
        self.labelArea.setGeometry(QtCore.QRect(30, 20, 431, 321))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelArea.setFont(font)
        self.labelArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelArea.setObjectName("labelArea")

        self.retranslateUi(updateDialog)
        QtCore.QMetaObject.connectSlotsByName(updateDialog)

    def retranslateUi(self, updateDialog):
        _translate = QtCore.QCoreApplication.translate
        updateDialog.setWindowTitle(_translate("updateDialog", "SimpleCrypt Update"))
        self.downloadButton.setText(_translate("updateDialog", "⬇️ Download now!"))
        self.labelArea.setText(_translate("updateDialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    updateDialog = QtWidgets.QDialog()
    ui = Ui_updateDialog()
    ui.setupUi(updateDialog)
    updateDialog.show()
    sys.exit(app.exec_())
