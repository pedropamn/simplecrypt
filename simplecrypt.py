#Crypt Function
def crypt(password, fullfilepath):
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
        
        
        #Delete original file
        import os
        os.remove(fullfilepath)
        
        #Rename .aes file to original extension
        os.rename(fullfilepath + ".aes", fullfilepath)
        
    except Exception as e:
        done = False

    
    return done



#Decrypt Function
def decrypt(password, fullfilepathtodecrypt):
    import pyAesCrypt

    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    # encrypt
    try:
        done = True
        
        #import os.path
        #new_file_path_and_name = os.path.splitext(fullfilepathtodecrypt)[0] #everything before .aes        
        
        pyAesCrypt.decryptFile(fullfilepathtodecrypt, fullfilepathtodecrypt + '.temp', password, bufferSize)
        
        #Delete original file
        import os
        os.remove(fullfilepathtodecrypt)
        
        #Rename .temp file to original extension
        os.rename(fullfilepathtodecrypt + ".temp", fullfilepathtodecrypt)

    except Exception as e: 
        done = False
        
    return done

    
    
    


