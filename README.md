<h1 align="center">Simple Crypt Tool </h1>

<p align="center">
  <img src="https://i2.paste.pics/b5522d91c384aea814e2680da4067d71.png?trs=ab5d135b7e6e342fe4664ea6a07c633b2714c968bb8fef32aa717ffe3ed74fc3" />
</p>

&rarr; __Description__ 
* A simple program that encrypt and decrypt any file with password

&rarr; __Usage__ 
* Just run executables available in [Releases section](https://github.com/pedropamn/simplecrypt/releases) (Windows and Linux)

&rarr; __Contribute & Build__
* You must install pyAesCrypt in order to script work. PyInstaller is a good option to create a build. You can install both via pip 
(```pip install pyAesCrypt``` | ```pip install PyInstaller```)
* GUI is made with [PAGE](https://sourceforge.net/projects/page/)(.tcl files). Check the [PAGE documentation](http://page.sourceforge.net/html/index.html) to know more
* Do not touch on ```about.py``` and ```main.py```. These files are dinamically created by PAGE
* To test, just call ```main_support.py```. To create executable file, run ```pyinstaller --onefile --windowed --icon=padlock.ico main_support.py```
