import sys
from colorama import Fore, Style, init, Back
init(autoreset=True)


def checklib(lib):
    import importlib
    import subprocess
    try:
        importlib.import_module(lib)
        return True
    except ImportError:
        #return False
        try:
            subprocess.check_call(["pip", "install", lib])
            print("The lib" +lib+ " was installed successfully.")
            return True
        except subprocess.CalledProcessError:
            print("Wasn't possible to install the lib " +lib+". Check your environment and try again mannualy.")
            return False
           

def print_help():
    
   

    
    txt = fr"""
       
                             .--------.
                            / .------. \
                           / /        \ \
                           | |        | |
                          _| |________| |_
                        .' |_|        |_| '.
                        '._____ ____ _____.'
                        |     .'____'.     |
                        '.__.'.'    '.'.__.'
                        '.__ SIMPLECRYPT   |
                        |   '.'. 2.0.'.'   |
                        '.____'.____.'____.'
                        '.________________.'
                              
                https://github.com/pedropamn/simplecrypt

    Usage: 

    For files:
        {Fore.GREEN}python simplecrypt-cli.py [--encrypt | --decrypt] /path/to/file.ext{Style.RESET_ALL}

    For folders:
        {Fore.GREEN}python simplecrypt-cli.py [--encrypt | --decrypt] /path/to/folder/{Style.RESET_ALL}
    """
    print(txt)
    
#Crypt Function
def crypt(password, fullfilepath, keepOriginal):
    import pyAesCrypt

    #get file extension
    #filename = fullfilepath.splitext(f)[0]
    #extension = fullfilepath.splitext(f)[1]


    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    # encrypt
    try:
        done = True
        
        #Must be firstly generated as .aes. Other extensions fail on decrypt
        pyAesCrypt.encryptFile(fullfilepath, fullfilepath + ".aes", password, bufferSize)
        
        import os
        
        if keepOriginal == False:
        
            #Delete original file            
            os.remove(fullfilepath)
            
            #Rename .aes file to original extension
            os.rename(fullfilepath + ".aes", fullfilepath)
        else:
            #Get original extension
            original_ext = get_file_extension(fullfilepath) #returns '.txt, .doc, etc...'
            #print(original_ext)
            
            #File path without extension
            file_path_without_ext = os.path.splitext(fullfilepath)[0]
            #print(file_path_without_ext)
            
            #Put timestamp on file name to make it unique. If user keeps the original file and already have a 'file_encrypted.extension' on folder, it will overwrite it.
            timestamp = str(getTimestamp())
            
            #Rename encrypted file
            os.rename(fullfilepath + ".aes", file_path_without_ext + "_encrypted_" + timestamp + original_ext)
        
    except Exception as e:
        done = False

    
    return done



#Decrypt Function
def decrypt(password, fullfilepathtodecrypt, keepOriginal):
    import pyAesCrypt
    import os
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    # encrypt
    try:
        done = True
        
        #import os.path
        #new_file_path_and_name = os.path.splitext(fullfilepathtodecrypt)[0] #everything before .aes        
        
        pyAesCrypt.decryptFile(fullfilepathtodecrypt, fullfilepathtodecrypt + '.temp', password, bufferSize)
       
        if keepOriginal == False:
            #Delete original file
            
            os.remove(fullfilepathtodecrypt)
            
            #Rename .temp file to original extension
            os.rename(fullfilepathtodecrypt + ".temp", fullfilepathtodecrypt)
        else:
            #Get original extension
            original_ext = get_file_extension(fullfilepathtodecrypt) #returns '.txt, .doc, etc...'
            
            #File path without extension
            file_path_without_ext = os.path.splitext(fullfilepathtodecrypt)[0]
            
            #Replace the 'encrypted' word for "decrypted", if any (by default, the 'encrypted' word is attached to the file if encrypted with SimpleCrypt)
            file_path_without_ext_replace = file_path_without_ext.replace('_encrypted','_decrypted')
            
            #If replaced...
            if file_path_without_ext_replace != file_path_without_ext:
                
                #"Decrypted" word was on filename. Just add timestamp on it 
                timestamp = str(getTimestamp())
            else: 
                
                #"Decrypted" word was not on file name. Add it (and timestamp too)
                timestamp = str(getTimestamp()) + '_decrypted'
            
            #Rename decrypted file
            os.rename(fullfilepathtodecrypt + '.temp', file_path_without_ext_replace + "_" + timestamp + original_ext) 

    except Exception as e: 
        done = False
        
    return done

    
    
def get_file_extension(file_path):
    import os

    if '.' in os.path.basename(file_path):
        file_extension = os.path.splitext(file_path)[1]
    else:
        file_extension = ""

    return file_extension   

def getTimestamp():
    import time
    timestamp = int(time.time())
    return timestamp

##### START #####

#Check libs
check = False
modules = ["colorama","pyAesCrypt", "getpass"]
for module in modules:
    check = checklib(module)
    

        

if check == True:
    arg = ""

    #Is there any args in command line?
    try:
     
        if sys.argv[1] == "--encrypt": 
            
            fullpath = sys.argv[2]
            import getpass
            password = getpass.getpass("Type the password: ")
            
            while True:
                answer = input("\n\nKeep Original file(s)? \nIf no, it will overwrite the file (be careful) (Y/N): ").strip().upper()
                if answer in ("Y", "N"):
                    if answer == "Y":
                        keep_original = True
                    else:
                        keep_original = False
                    break
                else:
                    print(f"{Fore.YELLOW}Invalid answer. Please, type 'Y' or'N' ")
            
            import os
            if os.path.isfile(fullpath):
                freturn = crypt(password, fullpath, keep_original)
                if freturn == True:
                    print(Fore.GREEN+Back.YELLOW+Style.BRIGHT+"File encrypted successfully!")
                else:
                    print(Fore.RED+Back.YELLOW+Style.BRIGHT+"Something went wrong. Check the path, password and file permissions")
            
            
            #It's a folder
            else:  
                error_list = []
                done_list = []
                
                #If 'isfile' fails, throw the 'else' (go here). So, if it's not a file, firstly check if the path to the supposed folder exists
                if not os.path.exists(fullpath):
                    #It's not a file or folder
                    print(Fore.RED+Back.YELLOW+Style.BRIGHT+"This file or folder doesn't exists")

                else:
                    #Loop all folder content (will list subfolder, but will not enter on it. os.walk enter in subfolders) and run the crypt function on each file
                    folder_content = os.listdir(fullpath)
                    
                    #Check if folder is empty
                    if folder_content == []:
                        print(Fore.RED+Back.YELLOW+Style.BRIGHT+"Folder is empty")
                    else:
                        #Loop
                        for item in folder_content:
                            
                            #Get whole item path (path/to/item)
                            file_path = os.path.join(fullpath, item)
                            
                            #Ignore subfolders
                            if os.path.isfile(file_path):
                                freturn = crypt(password, file_path, keep_original)
                                if freturn == False:
                                    error_list.append(item)
                                else:
                                    done_list.append(item)
                        
                        if len(error_list) == 0:                
                    
                            print(Fore.GREEN+Back.YELLOW+Style.BRIGHT+"All files were encrypted successfully!")


                            
                            #Check for dir separator (/ or \) on the end of 'fullpath'. "Select folder" option not include it and, even if it included, it could be removed by the user. Separator is necessary on the end of path for "Open folder" button to open the correct folder, not the parent one
                            if not fullpath.endswith(os.sep):
                                # Concats a empty string. It will add dir separator at the end (/ or \)
                                fullpath = os.path.join(fullpath, "")
                            
                        else:
                            all_errors = '\n'
                            all_dones = '\n'
                            for error in error_list:
                                all_errors = all_errors + str(error) + '\n'
                                
                            for done in done_list:
                                all_dones = all_dones + str(done) + '\n'

       
                            print(Fore.RED+Back.YELLOW+Style.BRIGHT+"We got problems on following files:\n "+all_errors+"\n Check their permissions and password\n\n✅ In addition, the following files were encrypted successfully\n"+all_dones)

        elif sys.argv[1] == "--decrypt": 
            
            fullpath = sys.argv[2]
            import getpass
            password = getpass.getpass("Type the password: ")
            
            while True:
                answer = input("\n\nKeep Original file(s)? \nIf no, it will overwrite the file (be careful) (Y/N): ").strip().upper()
                if answer in ("Y", "N"):
                    if answer == "Y":
                        keep_original = True
                    else:
                        keep_original = False
                    break
                else:
                    print(f"{Fore.YELLOW}Invalid answer. Please, type 'Y' or'N' ")
            
            import os
            if os.path.isfile(fullpath):
                freturn = decrypt(password, fullpath, keep_original)
                if freturn == True:
                    print(Fore.GREEN+Back.YELLOW+Style.BRIGHT+"File decrypted successfully!")
                else:
                    print(Fore.RED+Back.YELLOW+Style.BRIGHT+"Something went wrong. Check the path, password and file permissions")
            
            
            #It's a folder
            else:  
                error_list = []
                done_list = []
                
                #If 'isfile' fails, throw the 'else' (go here). So, if it's not a file, firstly check if the path to the supposed folder exists
                if not os.path.exists(fullpath):
                    #It's not a file or folder
                    print(Fore.RED+Back.YELLOW+Style.BRIGHT+"This file or folder doesn't exists")

                else:
                    #Loop all folder content (will list subfolder, but will not enter on it. os.walk enter in subfolders) and run the crypt function on each file
                    folder_content = os.listdir(fullpath)
                    
                    #Check if folder is empty
                    if folder_content == []:
                        print(Fore.RED+Back.YELLOW+Style.BRIGHT+"Folder is empty")
                    else:
                        #Loop
                        for item in folder_content:
                            
                            #Get whole item path (path/to/item)
                            file_path = os.path.join(fullpath, item)
                            
                            #Ignore subfolders
                            if os.path.isfile(file_path):
                                freturn = decrypt(password, file_path, keep_original)
                                if freturn == False:
                                    error_list.append(item)
                                else:
                                    done_list.append(item)
                        
                        if len(error_list) == 0:                
                    
                            print(Fore.GREEN+Back.YELLOW+Style.BRIGHT+"All files were decrypted successfully!")


                            
                            #Check for dir separator (/ or \) on the end of 'fullpath'. "Select folder" option not include it and, even if it included, it could be removed by the user. Separator is necessary on the end of path for "Open folder" button to open the correct folder, not the parent one
                            if not fullpath.endswith(os.sep):
                                # Concats a empty string. It will add dir separator at the end (/ or \)
                                fullpath = os.path.join(fullpath, "")
                            
                        else:
                            all_errors = '\n'
                            all_dones = '\n'
                            for error in error_list:
                                all_errors = all_errors + str(error) + '\n'
                                
                            for done in done_list:
                                all_dones = all_dones + str(done) + '\n'

       
                            print(Fore.RED+Back.YELLOW+Style.BRIGHT+"We got problems on following files:\n "+all_errors+"\n Check their permissions and password\n\n✅ In addition, the following files were decrypted successfully\n"+all_dones)
            

        #Not acceptable or malformed args
        else:
            print_help()

    #No args        
    except IndexError as e:
        print_help()
else:
    print("Some libs could'n be imported. Install it mannualy via pip")
