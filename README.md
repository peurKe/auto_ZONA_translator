# auto_ZONA_translator

Script for translating all Ukrainian or Russian texts of the Steam games '**Z.O.N.A Origin**' and '**Z.O.N.A Project X**' by **AGaming+** and enjoy Russian voices while having all the texts in your native language!

## Prerequisites

- Your 'Z.O.N.A' game must be up to date.
- Your PC must have an Internet connection for Google Translator or Deepl API requests.
- You must have a valid API auth key if you use Deepl API requests with the "-t 'deepl'" and "-ta 'xxx'" parameters.

## Currently supported languages

- English, Čeština, Dansk, Español, Suomi, Français, Magyar, Italiano, Nederlands, Polski, Português, Română, Svenska

# Usage from binary release

## Go to the Latest release:

- [Latest release](https://github.com/peurKe/auto_ZONA_translator/releases)

## Download the EXE installer "**auto_ZONA_translator_installer.exe**"

## Copy the EXE installer "**auto_ZONA_translator_installer.exe**"

- Copy it into your **Z.O.N.A Project X** or **Z.O.N.A Origin** game directory in your Steam Library.
  By default in: 
     - **Z.O.N.A Project X**: C:\SteamLibrary\steamapps\common\ZONA
     - **Z.O.N.A Origin**: C:\SteamLibrary\steamapps\common\ZONAORIGIN

   NB: If your games are installed on D: drive then the drive will be D:
 
### Go to your game directory.

### Double-clic on '**auto_ZONA_translator_installer.exe**'

  • Check the box for language you want to translate to:
```
 Choose your preferred language for ZONA subtitles
 Please select one of the following options:
   ( )  en (English)
   ( )  cs (Čeština)
   ( )  da (Dansk)
   ( )  es (Español)
   ( )  fi (Suomi)
   ( )  fr (Français)
   ( )  hu (Magyar)
   ( )  it (Italiano)
   ( )  nl (Nederlands)
   ( )  pl (Polski)
   ( )  pt (Português)
   ( )  ro (Română)
   ( )  sv (Svenska)
```
  • Clic on "Next" button

### Installer show the destination location

  • If destination location correspond to your Z.O.N.A game installation, then clic on "Next" button

  • Else clic on 'Browse' button to set the correct destination location,  then clic on "Next" button

### Installer indicate destination location already exists

  • It is normal. It is beacause installer install in an existing game, so confirm by clic on 'Yes' button.

### Installer show the main information about installation process that will be executed

  • Clic on 'Install' button.

### Then installation python script starts automatically

  • Prerequisites appears on screen and let you update your Z.O.N.A game before start to translate it.
```
    • Your 'Z.O.N.A' game must be up to date.
    • Your PC must have an Internet connection for Google Translator or Deepl API requests.
    • You must have a valid API auth key if you use Deepl API requests with the \"-t 'deepl'\" and \"-ta 'xxx'\" parameters.

      If needed you can update now your '{DEFAULT_ZONA_GAME_NAME}' game before begin translation.
      Then press Enter to translate your '{DEFAULT_ZONA_GAME_NAME}' game...\n", bcolors.ASK)
```

  • Try to update your Z.O.N.A game from Steam, and press Enter to translate your Z.O.N.A game.

  • Or directly press Enter to translate your Z.O.N.A game without update it.

### Wait for the translation ending, if installation succeed then this message will appears.
```
    To play with this translation:
        1. Just launch 'Z.O.N.A' game from Steam as usual.
        2. Be sure to select 'Ukrainian' language in 'Z.O.N.A' game's settings.

    /!\ Over the next few days:
        If 'Z.O.N.A' no longer launches correctly or if a new update has been made by AGaming+
        You will need to run this script again to update the translation.

    Press Enter to exit...
```

 Press Enter to exit...

### Enjoy Russian voices while having all the texts in your native language!

  • Just launch 'Z.O.N.A' game from Steam as usual.

  • Be sure to select 'Ukrainian' language in 'Z.O.N.A' game's settings.

### Restoring original subtitles

2 ways :

  • Either select 'English' language in 'Z.O.N.A' game's settings.

  • Or either execute the shortcut '**auto_ZONA_translator (restore)**' created by the executable into your Z.O.N.A game directory, and confirm you want to restore original translation (y/n)
```
 Confirm you want to restore all '0.035' backup binary files (y/n): 
```

## Usage from sources

### Download the **latest** version of Python for windows for your PC architecture :

  • [**Windows installer (64-bit)** or **Windows installer (32-bit)**](https://www.python.org/downloads/windows/) 

### Run the installer and follow the prompts to install Python.

### Open python installed console, upgrade pip package and install all following additional packages:

    pip install --upgrade pip
    pip install tqdm deepl googletrans==3.1.0a0 legacy-cgi nltk unidecode pywin32

### Download the sources ZIP archive

  • "**auto_ZONA_translator_SRC.zip**".

### Extract the archive content into your game directory.

### Go to your game directory.

### Double clic on '**auto_ZONA_translator.py**' to execute script

  • Press Enter if prerequisites displayed on the screen are correct:
```
    • Your 'Z.O.N.A Origin' game must be up to date.
    • Your PC has an Internet connection for Google Translator or Deepl API requests.
    • You have a valid API auth key if you use Deepl API requests with the "-t 'deepl'" and "-ta 'xxx'" parameters.
```
  • Select the language you want to translate English to:
```
 Supported languages:
   en (English)
   cs (Čeština)
   da (Dansk)
   es (Español)
   fi (Suomi)
   fr (Français)
   hu (Magyar)
   it (Italiano)
   nl (Nederlands)
   pl (Polski)
   pt (Português)
   ro (Română)
   sv (Svenska)

 Language to translate to (specify the 2-letter language code):
```

### Wait for the translation ending, if installation succeed then this message will appears.
```
    To play with this translation:
        1. Just launch 'Z.O.N.A' game from Steam as usual.
        2. Be sure to select 'Ukrainian' language in 'Z.O.N.A' game's settings.

    /!\ Over the next few days:
        If 'Z.O.N.A' no longer launches correctly or if a new update has been made by AGaming+
        You will need to run this script again to update the translation.

    Press Enter to exit...
```

### Enjoy Russian voices while having all the texts in your native language!

  • Just launch 'Z.O.N.A' game from Steam as usual.

  • Be sure to select 'Ukrainian' language in 'Z.O.N.A' game's settings.

### Restoring original subtitles

2 ways :

  • Either select 'English' language in 'Z.O.N.A' game's settings.

  • Or either execute the shortcut '**auto_ZONA_translator (restore)**' created by the executable into your Z.O.N.A game directory, and confirm you want to restore original translation (y/n)
```
 Confirm you want to restore all '0.035' backup binary files (y/n): 
```

