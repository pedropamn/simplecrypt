from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from ui.main import Ui_MainWindow
import simplecrypt
import ui.resource_rc
#import messagebox

'''
To do:

warning for long files
not an .aes file	

'''

def showMessageBox(title, message, type = 'QMessageBox.Information', buttons = 'QMessageBox::Ok'):

    msgBox = QMessageBox()        
    msgBox.setWindowTitle(title)
    msgBox.setText(message)
    
    if(type == 'QMessageBox.Question'):
        msgBox.setIcon(QMessageBox.Question)
    elif(type == 'QMessageBox.Information'):
        msgBox.setIcon(QMessageBox.Information)
    elif(type == 'QMessageBox.Warning'):
        msgBox.setIcon(QMessageBox.Warning)
    elif(type == 'QMessageBox.Critical'):
        msgBox.setIcon(QMessageBox.Critical)
    else:
        msgBox.setIcon(QMessageBox.NoIcon)
        
    
    if(buttons == 'QMessageBox::Ok'):
        msgBox.setStandardButtons(QMessageBox.Ok)
    elif(buttons == 'QMessageBox::Open'):
        msgBox.setStandardButtons(QMessageBox.Open)
    elif(buttons == 'QMessageBox::Save'):
        msgBox.setStandardButtons(QMessageBox.Save)
    elif(buttons == 'QMessageBox::Cancel'):
        msgBox.setStandardButtons(QMessageBox.Cancel)
    elif(buttons == 'QMessageBox::Close'):
        msgBox.setStandardButtons(QMessageBox.Close)    
    elif(buttons == 'QMessageBox::Discard'):
        msgBox.setStandardButtons(QMessageBox.Discard)
    elif(buttons == 'QMessageBox::Apply'):
        msgBox.setStandardButtons(QMessageBox.Apply)
    elif(buttons == 'QMessageBox::Reset'):
        msgBox.setStandardButtons(QMessageBox.Reset)
    elif(buttons == 'QMessageBox::RestoreDefaults'):
        msgBox.setStandardButtons(QMessageBox.RestoreDefaults)
    elif(buttons == 'QMessageBox::Help'):
        msgBox.setStandardButtons(QMessageBox.Help)
    elif(buttons == 'QMessageBox::SaveAll'):
        msgBox.setStandardButtons(QMessageBox.SaveAll)
    elif(buttons == 'QMessageBox::Yes'):
        msgBox.setStandardButtons(QMessageBox.Yes)
    elif(buttons == 'QMessageBox::YesToAll'):
        msgBox.setStandardButtons(QMessageBox.YesToAll)
    elif(buttons == 'QMessageBox::Abort'):
        msgBox.setStandardButtons(QMessageBox.Abort)
    elif(buttons == 'QMessageBox::Retry'):
        msgBox.setStandardButtons(QMessageBox.Retry)
    elif(buttons == 'QMessageBox::Ignore'):
        msgBox.setStandardButtons(QMessageBox.Ignore)
    elif(buttons == 'QMessageBox::NoButton'):
        msgBox.setStandardButtons(QMessageBox.NoButton) 
    
    msgBox.exec()
    
def btn_crypt_click():
    
    password = ui.password.text()
    fullfilepath = ui.fullfilepath.text()
    
    if password == "" or fullfilepath == "":
        showMessageBox("Ops", "Fill all fields", 'QMessageBox.Warning', 'QMessageBox::Ok')
    else:
        freturn = simplecrypt.crypt(password, fullfilepath)
        if freturn == True:
            showMessageBox("Yeah", "Done!", 'QMessageBox.Information', 'QMessageBox::Ok')
        else:
            showMessageBox("Ops", "Something went wrong. Check the path and file permissions", 'QMessageBox.Warning', 'QMessageBox::Ok')
        
def btn_decrypt_click():
    
    password = ui.password.text()
    fullfilepathtodecrypt = ui.fullfilepath.text()
    
    if password == "" or fullfilepathtodecrypt == "":
        showMessageBox("Ops", "Fill all fields",'QMessageBox.Warning', 'QMessageBox::Ok')
    else:
        freturn = simplecrypt.decrypt(password, fullfilepathtodecrypt)
        if freturn == True:
            showMessageBox("Yeah", "Done!", 'QMessageBox.Information', 'QMessageBox::Ok')
        else:
            showMessageBox("Ops", "Something went wrong. Check path, file permissions and password", 'QMessageBox.Warning', 'QMessageBox::Ok')


def openFileNameDialog():
    file , check = QFileDialog.getOpenFileName(None, "Choose your file","", "All Files (*);;Text Files (*.txt)")
    if check:
        #Insert file path into input field
        ui.fullfilepath.setText(file)
        
        #Get file size
        import os
        size = os.path.getsize(file)
        
        if size >= 104857600: #100 MB
            showMessageBox("Info", "This is a big file and it's normal take some time to encrypt/decrypt", 'QMessageBox.Warning', 'QMessageBox::Ok')

        
        #print(file)
 
def infomsg():
    showMessageBox("Info", "SimpleCrypt v1.0\n\n Developed by Pedro Neto\n\n https://www.pedronetoweb.com.br", 'QMessageBox.Info', 'QMessageBox::Ok')

def toggleEchoMode(self):
    current_echo_mode = ui.password.echoMode()
        
    if current_echo_mode == 2: #Password
        ui.password.setEchoMode(0) #Normal
    else:
        ui.password.setEchoMode(2) #Password
    
if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
        
    #Clicks 
    ui.btn_crypt.clicked.connect(btn_crypt_click)
    ui.btn_decrypt.clicked.connect(btn_decrypt_click)
    ui.choose_btn.clicked.connect(openFileNameDialog)
    ui.info.triggered.connect(infomsg)
    ui.eye.mousePressEvent = toggleEchoMode

    sys.exit(app.exec_())
