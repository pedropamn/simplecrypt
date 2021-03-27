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
import os
password_crypt = 'testing'

#Create path if not exists
def create_folder_if_not_exists(path):
	check = os.path.isdir(path)
	if check == False:
		try:
			os.mkdir(path)
		except OSError:
			print ("Creation of the directory %s failed" % path)
		else:
			print ("Successfully created the directory %s " % path)
	else:
		print(path + " already exists")

	
#Crypt Function
def crypt(password):
	import pyAesCrypt
	
	files = os.listdir(path)
	
	for f in files:
		#get file extension
		filename = os.path.splitext(f)[0]
		extension = os.path.splitext(f)[1]
		
		
		# encryption/decryption buffer size - 64K
		bufferSize = 64 * 1024
		
		# encrypt
		pyAesCrypt.encryptFile(path + "/" + filename + extension,path + "/" +  filename + extension + ".aes", password, bufferSize)
		
		#Delete original file
		os.remove(path + "/" + filename + extension)
	


#Decrypt Function
def decrypt(password):
	import pyAesCrypt
	
	files = os.listdir(path)
	
	for f in files:
		
		#get file extension
		filename = os.path.splitext(f)[0]
		extension = os.path.splitext(f)[1] #At this point, .aes
		
		orig_ext = filename.split(".")[0]
		
		extension = os.path.splitext(f)[1] #.aes
	
		# encryption/decryption buffer size - 64K
		bufferSize = 64 * 1024
		
		# encrypt
		pyAesCrypt.decryptFile(path + "/" + filename + extension, path + "/" +  filename, password, bufferSize)

		#Delete encrypted file
		os.remove(path + "/" + filename + extension)

#Get all files from folder
def get_all_files_from_folder(path):
	files = os.listdir(path)
	for f in files:
		print(f)

#Login or Register Screen
def login_register_screen():
	print("Choose your option:")
	print("[1] Login")
	print("[2] Register")
	option = int(input('Option:'))
	
	if option == 1:
		login()
	elif option == 2:
		register()
	else:
		print("Invalid option")
		login_register_screen()

#Login - To do: Implement MySql connection
def login():
	os.system('cls')
	username = str(input('Username:'))
	password = str(input('Password:'))
	
	if username == 'user' and password == 'pass':
		main_screen()
	else:
		print("Go away")
		exit();

#Register - To do: Implement MySql connection
def register():
	print("Not implemented...")
	exit();
	
#The main screen with all options
def main_screen():
	create_folder_if_not_exists(path)
	print("Choose your option:")
	print("[1] Crypt")
	print("[2] Decrypt")
	option = int(input('Option:'))
	if option == 1:
		crypt(password_crypt)
	if option == 2:
		decrypt(password_crypt)
def main():	

	#Everything start in login and register screen
	login_register_screen()
		
main()