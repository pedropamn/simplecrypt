<h1 align="center">Simple Crypt Tool </h1>

<p align="center">
  <img src="https://github.com/pedropamn/simplecrypt/blob/main/simplecrypt.png?raw=true" />
</p>

&rarr; __Description__ 
* A simple program that encrypt and decrypt any file with password

&rarr; __Usage__ 
* Just run executables available in [Releases section](https://github.com/pedropamn/simplecrypt/releases) (Windows and Linux)

&rarr; __Contribute & Build__
* You must install pyAesCrypt in order to script work. PyInstaller is a good option to create a build. You can install both via pip 
(```pip install pyAesCrypt``` | ```pip install PyInstaller```)
* GUI is made with [PAGE](https://sourceforge.net/projects/page/)(.tcl files). Check the [PAGE documentation](http://page.sourceforge.net/html/index.html) to learn more
* Do not touch on ```about.py``` and ```main.py```. These files are dinamically created by PAGE
* To test, just call ```main_support.py```. To create executable file, run ```pyinstaller --onefile --windowed --icon=padlock.ico main_support.py```
