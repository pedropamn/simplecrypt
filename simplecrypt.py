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
        pyAesCrypt.encryptFile(fullfilepath, fullfilepath + ".aes", password, bufferSize)
        done = True
        
        #Delete original file
        import os
        os.remove(fullfilepath)
        
        #Rename .aes file to original extension
        #os.rename(fullfilepath + ".aes", 'encryptedssss')
        
    except Exception as e:
        done = False

    
    return done



#Decrypt Function
def decrypt(password, fullfilepath):
    import pyAesCrypt

    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    # encrypt
    try:
        pyAesCrypt.decryptFile(fullfilepath, fullfilepath + '.temp', password, bufferSize)
        done = True

        #Delete encrypted file
        import os
        os.remove(fullfilepath)

        #Rename .temp file to original extension
        import os.path
        original_path_and_name = os.path.splitext(fullfilepath)[0] #/path/to/file.ext
        os.rename(fullfilepath + '.temp', original_path_and_name)
        
        
    except Exception as e:
        done = False
        
    return done
    


