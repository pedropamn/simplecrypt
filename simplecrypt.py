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
            print(original_ext)
            
            #File path without extension
            file_path_without_ext = os.path.splitext(fullfilepath)[0]
            print(file_path_without_ext)
            
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

