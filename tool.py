print("""
 ______  __ __    ___       ____  ____     ___   ____  ______      ____   __ __  ______  __ __   ___   ____       ______   ___    ___   _     
|      ||  |  |  /  _]     /    ||    \   /  _] /    ||      |    |    \ |  |  ||      ||  |  | /   \ |    \     |      | /   \  /   \ | |    
|      ||  |  | /  [_     |   __||  D  ) /  [_ |  o  ||      |    |  o  )|  |  ||      ||  |  ||     ||  _  |    |      ||     ||     || |    
|_|  |_||  _  ||    _]    |  |  ||    / |    _]|     ||_|  |_|    |   _/ |  ~  ||_|  |_||  _  ||  O  ||  |  |    |_|  |_||  O  ||  O  || |___ 
  |  |  |  |  ||   [_     |  |_ ||    \ |   [_ |  _  |  |  |      |  |   |___, |  |  |  |  |  ||     ||  |  |      |  |  |     ||     ||     |
  |  |  |  |  ||     |    |     ||  .  \|     ||  |  |  |  |      |  |   |     |  |  |  |  |  ||     ||  |  |      |  |  |     ||     ||     |
  |__|  |__|__||_____|    |___,_||__|\_||_____||__|__|  |__|      |__|   |____/   |__|  |__|__| \___/ |__|__|      |__|   \___/  \___/ |_____|
   
by @pedropamn and @alcantaralbeatriz   
""")

path = "C:/crypt_this_folder"

#Create path if not exists
def create_folder_if_not_exists(path):
	import os
	check = os.path.isdir(path)
	if check == False:
		try:
			os.mkdir(path)
		except OSError:
			print ("Creation of the directory %s failed" % path)
		else:
			print ("Successfully created the directory %s " % path)

	
#Crypt Function
def crypt(file, password):
	import pyAesCrypt
	# encryption/decryption buffer size - 64K
	bufferSize = 64 * 1024
	# encrypt
	pyAesCrypt.encryptFile(file, file + ".aes", password, bufferSize)	


#Decrypt Function
def decrypt(file, password):
	import pyAesCrypt
	# encryption/decryption buffer size - 64K
	bufferSize = 64 * 1024
	# decrypt
	pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)

#Get all files from folder
def get_all_files_from_folder(path):
	import os
	files = os.listdir(path)
	for f in files:
		print(f)

#To do: Implement MySql connection
def ask_for_credentials():
	username = str(input('Username:'))
	password = str(input('Password:'))
	
	if username == 'user' and password == 'pass':
		return True
	else:
		print("Go away")
		exit();

def main():
	
	#Get Credentials
	credentials = ask_for_credentials()	
	
	#Check
	if credentials == True:
	
		#Call functions for logged users
		create_folder_if_not_exists(path)
	else:
		exit()
		
main()