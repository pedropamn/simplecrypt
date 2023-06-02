<h1 align="center">Simple Crypt Tool </h1>

<p align="center">
  <img src="https://github.com/pedropamn/simplecrypt/blob/main/screen-simplecrypt.png?raw=true" />
</p>

&rarr; __Description__ 
* A simple program that encrypt and decrypt any file with password using AES256-CBC, via [PyAesCrypt](https://pypi.org/project/pyAesCrypt/)

&rarr; __Usage__ 
* Just run executables available in [Releases section](https://github.com/pedropamn/simplecrypt/releases) (Windows and Linux)

&rarr; __Contribute & Build__
* If you are a developer and would like to contribute, install all dependencies in ```requeriments.txt```, via
 
 ```pip install -r requeriments.txt```
*  PyInstaller is a good option to create a .exe file. You can install it via pip 

```pip install PyInstaller```
* GUI is made entirely with PyQt5
* The```start.py``` is the main file and ```simplecrypt.py``` is the script that encrypt and decrypt files.
*  To create executable file, run ```pyinstaller --onefile --windowed --icon=padlock.ico start.py```
