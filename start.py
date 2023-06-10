from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QApplication
from PyQt5.QtGui import QMovie
from ui.main import Ui_MainWindow
from ui.update import Ui_updateDialog
from ui.about import Ui_aboutDialog
import simplecrypt
import ui.resource_rc
from functools import partial #To pass arguments inside clicked.connect
#import threading


current_version = '2.0'


def openFolder(fullpath): #input: The full path, including the file. If folder, returns the folder
    import os
    import subprocess
    
    path = os.path.dirname(fullpath)
    print(path)
    if os.name == 'nt':  # Windows
        os.startfile(path)
    elif os.name == 'posix':  # Linux or macOS
        subprocess.Popen(['xdg-open', path])
    else:
        print("OS not supported")

def showMessageBox(title, message, type = 'QMessageBox.Information', buttons=('QMessageBox::Ok', None)):

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
    
    #Get password, path/file and checkbox about keep original file
    password = ui.password.text()
    fullpath = ui.fullfilepath.text()
    keep_original = ui.keepOriginalFile.isChecked()
    
    if password == "" or fullpath == "":
            showMessageBox("Ops", "Fill all fields", 'QMessageBox.Warning', 'QMessageBox::Ok')
    else:


        msgBox = QMessageBox()
        msgBox.setWindowTitle("Are you sure?")
        msgBox.setText("If encrypted, your files will be secure, but not openable, unless you use the same password to decrypt it. Proceed?")

        # Add custom buttons
        yes_proceed = msgBox.addButton("✅ Yes", QMessageBox.ActionRole)
        no_proceed = msgBox.addButton("❌ No", QMessageBox.ActionRole)
            
        # Define MessageBox Icon
        msgBox.setIcon(QMessageBox.Information)

        # Show the MessageBox and save the 'result'
        result = msgBox.exec()
        

        
        if msgBox.clickedButton() == yes_proceed:
            ui.btn_crypt.setText('Crypting...')
            ui.btn_crypt.setEnabled(False)
            QApplication.processEvents() #To force the interface update
            import os
            
            #########################################
            # It's a file 
            #########################################
            if os.path.isfile(fullpath):  
                freturn = simplecrypt.crypt(password, fullpath, keep_original)
                if freturn == True:
                    
                    #Change button text
                     #Change button text
                    ui.btn_crypt.setText('🔒 Crypt')
                    ui.btn_crypt.setEnabled(True)
                    QApplication.processEvents()

            
                    #ui.status.clear()
                    #showMessageBox("Yeah", "Done!\n\nSaved in ", 'QMessageBox.Information', 'QMessageBox::Open')
                    # Create a QMessageBox
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("Done!")
                    msgBox.setText("File encrypted successfully!")
                    #msgBox.setStandardButtons(QMessageBox.Open | QMessageBox.Close)

                    # Add custom buttons
                    open_button = msgBox.addButton("🗂 Open folder", QMessageBox.ActionRole)
                    close_button = msgBox.addButton("❌ Close", QMessageBox.ActionRole)
                        
                    # Associate functions with parameters
                    open_button.clicked.connect(partial(openFolder, fullpath))

                    # Define MessageBox Icon
                    msgBox.setIcon(QMessageBox.Information)

                    # Show the MessageBox
                    msgBox.exec()
                else:
                    ui.btn_crypt.setText('🔒 Crypt')
                    ui.btn_decrypt.setEnabled(True)
                    QApplication.processEvents() #To force the interface update
                    showMessageBox("Ops", "Something went wrong. Check the path and file permissions", 'QMessageBox.Warning', 'QMessageBox::Ok')
            
            #########################################
            # It's a folder 
            #########################################
            else:
                error_list = []
                done_list = []
                
                #If 'isfile' fails, throw the 'else' (go here). So, if it's not a file, firstly check if the path to the supposed folder exists
                if not os.path.exists(fullpath):
                    #It's not a file or folder
                    showMessageBox("Ops", "This file or folder doesn't exists", 'QMessageBox.Warning', 'QMessageBox::Ok')
                    ui.btn_crypt.setText('🔒 Crypt')
                    ui.btn_crypt.setEnabled(True)
                    QApplication.processEvents() #To force the interface update
                else:
                    #Loop all folder content (will list subfolder, but will not enter on it. os.walk enter in subfolders) and run the crypt function on each file
                    folder_content = os.listdir(fullpath)
                    
                    #Check if folder is empty
                    if folder_content == []:
                        showMessageBox("Ops", "Folder is empty", 'QMessageBox.Warning', 'QMessageBox::Ok')
                        ui.btn_crypt.setText('🔒 Crypt')
                        ui.btn_crypt.setEnabled(True)
                        QApplication.processEvents() #To force the interface update
                    else:
                        #Loop
                        for item in folder_content:
                            
                            #Get whole item path (path/to/item)
                            file_path = os.path.join(fullpath, item)
                            
                            #Ignore subfolders
                            if os.path.isfile(file_path):
                                freturn = simplecrypt.crypt(password, file_path, keep_original)
                                if freturn == False:
                                    error_list.append(item)
                                else:
                                    done_list.append(item)
                        
                        if len(error_list) == 0:                
                            #showMessageBox("Done!", "Files encrypted successfully! ", 'QMessageBox.Ok', 'QMessageBox::Ok')
                            ui.btn_crypt.setText('🔒 Crypt')
                            ui.btn_crypt.setEnabled(True)
                            QApplication.processEvents()
                    
                            # Create a QMessageBox
                            msgBox = QMessageBox()
                            msgBox.setWindowTitle("Done!")
                            msgBox.setText("All files were encrypted successfully!")

                            # Add custom buttons
                            open_button = msgBox.addButton("🗂 Open folder", QMessageBox.ActionRole)
                            close_button = msgBox.addButton("❌ Close", QMessageBox.ActionRole)
                            
                            #Check for dir separator (/ or \) on the end of 'fullpath'. "Select folder" option not include it and, even if it included, it could be removed by the user. Separator is necessary on the end of path for "Open folder" button to open the correct folder, not the parent one
                            if not fullpath.endswith(os.sep):
                                # Concats a empty string. It will add dir separator at the end (/ or \)
                                fullpath = os.path.join(fullpath, "")
                            
                            # Associate functions with parameters
                            open_button.clicked.connect(partial(openFolder, fullpath))

                            # Define MessageBox Icon
                            msgBox.setIcon(QMessageBox.Information)

                            # Show the MessageBox
                            msgBox.exec()
                            
                        else:
                            all_errors = '\n'
                            all_dones = '\n'
                            for error in error_list:
                                all_errors = all_errors + str(error) + '\n'
                                
                            for done in done_list:
                                all_dones = all_dones + str(done) + '\n'
                                    
                               #showMessageBox("Ops", "We got problems on following files:\n "+all_errors+'\n\n Check their permissions', 'QMessageBox.Warning', 'QMessageBox::Ok')
                            ui.btn_decrypt.setText('🔐 Decrypt')
                            ui.btn_decrypt.setEnabled(True)
                            QApplication.processEvents() #To force the interface update
                            
                            # Create a QMessageBox
                            msgBox = QMessageBox()
                            msgBox.setWindowTitle("Ops!")
                            msgBox.setText("❌ We got problems on following files:\n "+all_errors+"\n Check their permissions\n\n✅ The following files were encrypted successfully\n"+all_dones)

                            # Add custom buttons
                            open_button = msgBox.addButton("🗂 Open folder", QMessageBox.ActionRole)
                            close_button = msgBox.addButton("❌ Close", QMessageBox.ActionRole)

                            # Associate functions with parameters
                            open_button.clicked.connect(partial(openFolder, fullpath))

                            # Define MessageBox Icon
                            msgBox.setIcon(QMessageBox.Warning)

                            # Show the MessageBox
                            msgBox.exec()



def btn_decrypt_click():
    
    
    #Get password and path/file
    password = ui.password.text()
    fullpath = ui.fullfilepath.text()
    keep_original = ui.keepOriginalFile.isChecked()
    
    if password == "" or fullpath == "":
            showMessageBox("Ops", "Fill all fields", 'QMessageBox.Warning', 'QMessageBox::Ok')
    else:
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Are you sure?")
        msgBox.setText("Your files will be decrypted and can be opened by anyone. Proceed?")

        # Add custom buttons
        yes_proceed = msgBox.addButton("✅ Yes", QMessageBox.ActionRole)
        no_proceed = msgBox.addButton("❌ No", QMessageBox.ActionRole)
            
        # Define MessageBox Icon
        msgBox.setIcon(QMessageBox.Information)

        # Show the MessageBox and save the 'result'
        result = msgBox.exec()
        

        
        if msgBox.clickedButton() == yes_proceed:
            ui.btn_decrypt.setText('Decrypting...')
            ui.btn_decrypt.setEnabled(False)
            QApplication.processEvents() #To force the interface update
        
            import os
            
            #########################################
            # It's a file 
            #########################################
            if os.path.isfile(fullpath):  
                freturn = simplecrypt.decrypt(password, fullpath, keep_original)
                if freturn == True:
                    ui.btn_decrypt.setText('🔐 Decrypt')
                    ui.btn_decrypt.setEnabled(True)
                    QApplication.processEvents() #To force the interface update
                    
                    #showMessageBox("Yeah", "Done!", 'QMessageBox.Information', 'QMessageBox::Ok')
                    
                    # Create a QMessageBox
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle("Done!")
                    msgBox.setText("File decrypted successfully!")

                    # Add custom buttons
                    open_button = msgBox.addButton("🗂 Open folder", QMessageBox.ActionRole)
                    close_button = msgBox.addButton("❌ Close", QMessageBox.ActionRole)

                    # Associate functions with parameters
                    open_button.clicked.connect(partial(openFolder, fullpath))

                    # Define MessageBox Icon
                    msgBox.setIcon(QMessageBox.Information)

                    # Show the MessageBox
                    msgBox.exec()
                else:
                    ui.btn_decrypt.setText('🔐 Decrypt')
                    ui.btn_decrypt.setEnabled(True)
                    QApplication.processEvents() #To force the interface update
                    showMessageBox("Ops", "Something went wrong. Check the password, path and file permissions", 'QMessageBox.Warning', 'QMessageBox::Ok')
            
            #########################################
            # It's a folder 
            #########################################
            else:
                error_list = []
                done_list = []
                
                 #If 'isfile' fails, throw the 'else' (go here). So, if it's not a file, firstly check if the path to the supposed folder exists
                if not os.path.exists(fullpath):
                    #It's not a file or folder
                    showMessageBox("Ops", "This file or folder doesn't exists", 'QMessageBox.Warning', 'QMessageBox::Ok')
                    ui.btn_decrypt.setText('🔐 Decrypt')
                    ui.btn_decrypt.setEnabled(True)
                    QApplication.processEvents() #To force the interface update
                else:
                    
                    #It's a folder. Loop all files (without enter in subfolders) and run the crypt function on each file
                    folder_content = os.listdir(fullpath)
                    
                     #Check if folder is empty
                    if folder_content == []:
                        showMessageBox("Ops", "Folder is empty", 'QMessageBox.Warning', 'QMessageBox::Ok')
                        ui.btn_decrypt.setText('🔐 Decrypt')
                        ui.btn_decrypt.setEnabled(True)
                        QApplication.processEvents() #To force the interface update
                    else:
                        #Loop
                        for item in folder_content:
                            
                            #Get file path
                            file_path = os.path.join(fullpath, item)
                            
                            #It's a file?
                            if os.path.isfile(file_path):
                                freturn = simplecrypt.decrypt(password, file_path, keep_original)
                                if freturn == False:
                                    error_list.append(item)
                                else:
                                    done_list.append(item)
                        
                        if len(error_list) == 0:
                            #ui.status.setText("")
                            #showMessageBox("Done!", "Files decrypted successfully! ", 'QMessageBox.Ok', 'QMessageBox::Ok')
                            
                            ui.btn_decrypt.setText('🔐 Decrypt')
                            ui.btn_decrypt.setEnabled(True)
                            QApplication.processEvents() #To force the interface update
                            
                            # Create a QMessageBox
                            msgBox = QMessageBox()
                            msgBox.setWindowTitle("Done!")
                            msgBox.setText("All files were decrypted successfully!")


                            # Add custom buttons
                            open_button = msgBox.addButton("🗂 Open folder", QMessageBox.ActionRole)
                            close_button = msgBox.addButton("❌ Close", QMessageBox.ActionRole)
                            
                            #Check for dir separator (/ or \) on the end of 'fullpath'. "Select folder" option not include it and, even if it included, it could be removed by the user. Separator is necessary on the end of path for "Open folder" button to open the correct folder, not the parent one
                            if not fullpath.endswith(os.sep):
                                # Concats a empty string. It will add dir separator at the end (/ or \)
                                fullpath = os.path.join(fullpath, "")
                                
                            # Associate functions with parameters
                            open_button.clicked.connect(partial(openFolder, fullpath))

                            # Define MessageBox Icon
                            msgBox.setIcon(QMessageBox.Information)

                            # Show the MessageBox
                            msgBox.exec()
                        else:
                            all_errors = '\n'
                            all_dones = '\n'
                            for error in error_list:
                                all_errors = all_errors + str(error) + '\n'
                                
                            for done in done_list:
                                all_dones = all_dones + str(done) + '\n'
                                
                            #showMessageBox("Ops", "We got problems on following files:\n "+all_errors+'\n\n Check if they were encrypted with the password you entered. Other files are decrypted successfully', 'QMessageBox.Warning', 'QMessageBox::Ok')
                            
                            ui.btn_decrypt.setText('🔐 Decrypt')
                            ui.btn_decrypt.setEnabled(True)
                            QApplication.processEvents() #To force the interface update
                            
                             # Create a QMessageBox
                            msgBox = QMessageBox()
                            msgBox.setWindowTitle("Ops!")
                            msgBox.setText("❌ We got problems on following files:\n "+all_errors+"\n Check their permissions and if they were encrypted with the provided password\n\n✅ The following files were decrypted successfully\n"+all_dones)

                            # Add custom buttons
                            open_button = msgBox.addButton("🗂 Open folder", QMessageBox.ActionRole)
                            close_button = msgBox.addButton("❌ Close", QMessageBox.ActionRole)
                            
                            #Check for dir separator (/ or \) on the end of 'fullpath'. "Select folder" option not include it and, even if it included, it could be removed by the user. Separator is necessary on the end of path for "Open folder" button to open the correct folder, not the parent one
                            if not fullpath.endswith(os.sep):
                                # Concats a empty string. It will add dir separator at the end (/ or \)
                                fullpath = os.path.join(fullpath, "")
                                
                            # Associate functions with parameters
                            open_button.clicked.connect(partial(openFolder, fullpath))

                            # Define MessageBox Icon
                            msgBox.setIcon(QMessageBox.Warning)

                            # Show the MessageBox
                            msgBox.exec()
                
                


def openFileNameDialog():
    file , check = QFileDialog.getOpenFileName(None, "Choose your file","", "All Files (*);;Text Files (*.txt)")
    if check:
        #Insert file path into input field
        ui.fullfilepath.setText(file)
        
        #Get file size
        import os
        size = os.path.getsize(file)
        
        if size >= 104857600: #100 MB
            showMessageBox("Big File", "This is a big file and it's normal take some time to encrypt/decrypt", 'QMessageBox.Warning', 'QMessageBox::Ok')

        
        #print(file)

def openFolderDialog():
    folder  = QFileDialog.getExistingDirectory(None, "Choose your folder")
    if folder:
    
        has_big_file = False
        
        #Insert file path into input field
        ui.fullfilepath.setText(folder)
        
        #Check the file size of all files inside the folder
        import os 
        
        #List all (files and folders)
        folder_content = os.listdir(folder)
        
        #Loop
        for item in folder_content:
            
            #Get file path
            file_path = os.path.join(folder, item)
            
            #Is file?
            if os.path.isfile(file_path):  

                    #Get the size
                    file_size = os.path.getsize(file_path)
                    if file_size >= 104857600: #100 MB
                        has_big_file = True
                    
            
        if has_big_file == True:
            showMessageBox("Big Files", "This folder has one or more files that are very large. It's normal take some time to encrypt/decrypt them", 'QMessageBox.Warning', 'QMessageBox::Ok')
        #print(file)
def help_keep_original_file_func(event):
    showMessageBox("Info", "You can keep the original file, encrypted or decrypted.\n\n If checked: \n\n-> If encrypting, the original file will remain intact and a encrypted one will be generated. \n\n-> If decrypting, the encrypted file will remain intact and a decrypted one will be generated\n\n If unchecked, original file will be deleted. (BE CAREFUL)", 'QMessageBox.Information', 'QMessageBox::Ok')

def openPage(url, event):
    import webbrowser
    webbrowser.open(url)
    
def infomsg():    
    aboutDialog.show()
    
def checkForUpdates(method = 'auto'):
 #Check for Updates
    
    
    import requests
    try:
        response = requests.get('https://raw.githubusercontent.com/pedropamn/simplecrypt/main/update.json')
        if response.status_code == 200:
            data = response.json()
            import json
            most_recent_version = data["most_recent_version"]
            download_page = data["download_page"]
            whats_new = data["whats_new"]
            
            
            
            if most_recent_version > current_version:
                ui_update.labelArea.setText("🔥 Update Available!\n\n👉 You have the version "+current_version+" and the version "+most_recent_version+" is available\n\n🆕 Whats new:\n\n"+whats_new+"\n\n")
                
                
                ui_update.downloadButton.disconnect()
                ui_update.downloadButton.clicked.connect(partial(openPage, download_page))
                updateDialog.show()
                
            else:
                if method == 'menu':
                    showMessageBox("Info", "Good news! You have the most recent version :)", 'QMessageBox.Info', 'QMessageBox::Ok')
    except Exception as e:
        if method == 'menu':
            showMessageBox("Info", "Unable to check for updates. Check your internet connection", 'QMessageBox.Info', 'QMessageBox::Ok')
        else:
            #Do nothing
            return

def toggleEchoMode(self):
    current_echo_mode = ui.password.echoMode()
        
    if current_echo_mode == 2: #Password
        ui.password.setEchoMode(0) #Normal
    else:
        ui.password.setEchoMode(2) #Password


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    
    #Main Window
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    QtCore.QTimer.singleShot(500, checkForUpdates)
    
    '''
    #Starting new thread for checkForUpdates()
    class UpdateThread(threading.Thread):
        def run(self):
            checkForUpdates()
    
    update_thread = UpdateThread()
    update_thread.start()
    '''
    
    #Update Dialog (without showing)
    updateDialog = QtWidgets.QDialog()
    ui_update = Ui_updateDialog()
    ui_update.setupUi(updateDialog)
    
    #About Dialog (without showing)
    aboutDialog = QtWidgets.QDialog()
    ui_about = Ui_aboutDialog()
    ui_about.setupUi(aboutDialog)

        
    
    
    #Clicks 
 
    
    #Main UI
    ui.btn_crypt.clicked.connect(btn_crypt_click)
    ui.btn_decrypt.clicked.connect(btn_decrypt_click)
    ui.choose_file_btn.clicked.connect(openFileNameDialog)
    ui.choose_folder_btn.clicked.connect(openFolderDialog)
    ui.help_keep_original_file.mousePressEvent = help_keep_original_file_func
    ui.info.triggered.connect(infomsg)
    ui.actionCheck_for_Updates.triggered.connect(partial(checkForUpdates, 'menu'))
    ui.eye.mousePressEvent = toggleEchoMode

    
    #About UI
    ui_about.githubProjectLink.mousePressEvent = partial(openPage, "https://github.com/pedropamn/simplecrypt")
    ui_about.githubProfileLink.mousePressEvent = partial(openPage,"https://github.com/pedropamn")
    ui_about.websiteLink.mousePressEvent = partial(openPage,"https://www.pedronetoweb.com.br")
    
    sys.exit(app.exec_())
