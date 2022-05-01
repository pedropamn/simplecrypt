<h1 align="center">Simple Crypt Tool </h1>

<p align="center">
  <img src="https://github.com/pedropamn/simplecrypt/blob/main/screen-simplecrypt.png?raw=true" />
</p>

&rarr; __Description__ 
* A simple program that encrypt and decrypt any file with password using AES256-CBC, via [PyAesCrypt](https://pypi.org/project/pyAesCrypt/)

&rarr; __Usage__ 
* Just run executables available in [Releases section](https://github.com/pedropamn/simplecrypt/releases) (Windows and Linux)

&rarr; __Contribute & Build__
* If you are a developer and would like to contribute, you must install pyAesCrypt in order to script work. PyInstaller is a good option to create a build. You can install both via pip 
(```pip install pyAesCrypt``` | ```pip install PyInstaller```)
* GUI is made entirely with PyQt5
* The```start.py``` is the main file and ```simplecrypt.py``` is the script that encrypt and decrypt files.
*  To create executable file, run ```pyinstaller --onefile --windowed --icon=padlock.ico start.py```
