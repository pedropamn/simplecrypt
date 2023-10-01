<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="https://github.com/pedropamn/simplecrypt/blob/main/screen-simplecrypt.png?raw=true" width="60%" />



  <h1 align="center">SimpleCrypt</h1>

  <p align="center">
    Protect your files encrypting them with password, on Windows and Linux! 
   </p> 
    <a href="https://github.com/pedropamn/simplecrypt/releases"><img width="300" src="https://www.pngall.com/wp-content/uploads/2/Download-Button-Transparent.png" /></a><br>
    .
    <a href="https://github.com/pedropamn/simplecrypt/issues">Report a  Bug</a>
    ·
    <a href="https://github.com/pedropamn/simplecrypt/issues">Suggest a feature</a>
 
</div>




<!-- ABOUT THE PROJECT -->
## About the project

SimpleCrypt is a simple program that encrypt and decrypt any file with password using AES256-CBC, via [PyAesCrypt](https://pypi.org/project/pyAesCrypt/). You can encrypt a file or a entire folder with a password and protect your important ones!



<br><br>



<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation

* [Download from Releases section](https://github.com/pedropamn/simplecrypt/releases) 
## Built with

<img src="https://img.shields.io/badge/-Python-green?style=for-the-badge&logo=python&logoColor=white"></img>


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap


- [ ] Make it Installable
- [ ] Cloud Storage
- [ ] Stats
- [ ] CLI version  
- [ ] New Algorithms
- [ ] Increase compatibility (see Compatibility Notes below)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- NOTES -->
## Compatibility notes
* <img src="https://img.shields.io/badge/-Windows-blue?style=for-the-badge&logo=windows&logoColor=white"></img>
  - Tested on Windows 10 and Windows 11. Not tested on 8 and 8.1, but it should work too. Windows 7 is not compatible (should not work on earlier versions)

* <img src="https://img.shields.io/badge/-Linux-green?style=for-the-badge&logo=linux&logoColor=white"></img>
  - Tested and builded on Ubuntu 22.04.2. This system comes with glibc 2.35 and it was required by the executable when testing on other machines (Ubuntu 20.04 and Kali Linux 2021.4a). So, should work fine on system containing this library, for example:
    - Ubuntu 21.10+
    - Fedora 35+
    - Arch Linux (rolling release)
  
  Glibc version can be checked by ```ldd --version``` command


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contribute

* If you are a developer and would like to contribute, install all dependencies in ```requeriments.txt```, via
 
    ```pip install -r requeriments.txt```

* GUI is made entirely with PyQt5 and Qt Designer. You can edit the .ui files using it. After each change, remember to regenerate .py files. For example, after editing ```main.ui```:

    ```pyuic5 -x main.ui -o main.py``` 
 
    After it, comment the line ```#import resource_rc``` (it's already imported on ```start.py```)

* The```start.py``` is the main file and ```simplecrypt.py``` is the script that encrypt and decrypt files.

*  PyInstaller is a good option to create a executable files. You can install it via pip 

    ```pip install PyInstaller```
*  To create executable file, run ```pyinstaller --onefile --windowed --icon=padlock.ico start.py```

To contribute with a Pull Request:
1. Fork
2. Create a Branch of the feature (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add some AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Open a Pull Request




<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

apps@pedronetoweb.com.br


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
