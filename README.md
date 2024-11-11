# auto_ZONA_translator

Project for translating all Ukrainian or Russian texts of the Steam games '**Z.O.N.A Origin**' and '**Z.O.N.A Project X**' by **AGaming+** and enjoy Ukrainian or Russian voices while having all the texts in your native language!

<!-- TOC -->
- [Discord](#Discord)
- [Prerequisites](#Prerequisites)
- [Currently supported languages](#Currently-supported-languages)
- [Usage from binary release](#Usage-from-binary-release)
- [Usage from sources](#Usage-from-sources)
<!-- /TOC -->

# Discord

[Welcome to #zona-translate-deepl!](https://discord.com/channels/1113935727202410691/1302585407308955690)

# Prerequisites

- Your 'Z.O.N.A' game must be up to date.
- Your PC must have an Internet connection for Google Translator or Deepl API requests.
- You must have a valid API auth key if you use Deepl API requests with the "-t 'deepl'" and "-ta 'xxx'" parameters.

# Currently supported languages

- Čeština (Czech)
- Dansk (Danish)
- English (English)
- Español (Spanish)
- Français (French)
- German (German)
- Italiano (Italian)
- Magyar (Hungarian)
- Nederlands (Dutch)
- Polski (Polish)
- Português (Portuguese)
- Română (Romanian)
- Suomi (Finnish)
- Svenska (Swedish)

# Usage from executable installer

## Go to the Latest release:

- [Latest release](https://github.com/peurKe/auto_ZONA_translator/releases)

## Download the EXE installer "**auto_ZONA_translator_installer.exe**" from the release assets.

## Copy the EXE installer "**auto_ZONA_translator_installer.exe**"

- Copy it to your **Z.O.N.A Project X** or **Z.O.N.A Origin** game folder in your Steam library.
  By default in :
    - **Z.O.N.A Project X** :arrow_right: C:\Program Files (x86)\Steam\steamapps\common\ZONA\
    - **Z.O.N.A Origin** :arrow_right: C:\Program Files (x86)\Steam\steamapps\common\ZONAORIGIN\

   NB: If your Z.O.N.A game is installed on a drive other than the C: system drive, your game folder could be in the following location:
    - **Z.O.N.A Project X** :arrow_right: E:\SteamLibrary\steamapps\common\ZONA\
    - **Z.O.N.A Origin** :arrow_right: E:\Steam\Library\steamapps\common\ZONAORIGIN\

   If you want to retrieve your Z.O.N.A game folder, go to your library in Steam and:
    - Right-click on your Z.O.N.A. game in your list of games in the left-hand panel.
    - Click on 'Properties...'
    - Click on 'Browse...'
   An explorer window will appear showing the folder for your Z.O.N.A. game.
 
## Go to your game directory.

## Double-clic on '**auto_ZONA_translator_installer.exe**'

- Tick the box corresponding to the language of the TEXT and SUBTITLES you wish to read in the game:
```
  Choose your preferred language for TEXTS and SUBTITLES:
    ( ) Čeština
    ( ) Dansk
    ( ) English
    ( ) Español
    (X) Français
    ( ) German
    ( ) Italiano
    ( ) Magyar
    ( ) Nederlands
    ( ) Polski
    ( ) Português
    ( ) Română
    ( ) Suomi
    ( ) Svenska
```
- Clic on "Next" button

- Tick the box corresponding to the VOICE language you wish to hear in the game:
```
  Choose your preferred language for VOICES:
    (X)  Ukrainian
    ( )  Russian
```
- Clic on "Next" button

## Installer show the destination location

- If the destination location corresponds to the installation of your Z.O.N.A. game, click on the "Next" button.
  Alternatively, click the 'Browse' button to define the correct destination location, then click the 'Next' button.

## The installer indicates that the destination location already exists

- That's normal, this is because the installer is installing in an existing game. Confirm by clicking on the 'Yes' button.

## The installer displays the main information about the installation process that will be carried out.

- Clic on 'Install' button.

## The installation python script then starts automatically

## Wait for the translation ending

- If installation succeed then this message will appears.
```
    To play with this translation:
        1. Just launch 'Z.O.N.A' game from Steam as usual.
        2. Be sure to select 'Ukrainian/Russian' language in 'Z.O.N.A' game's settings.

    /!\ Over the next few days:
        If 'Z.O.N.A' no longer launches correctly or if a new update has been made by AGaming+
        You will need to run this script again to update the translation.

    Press Enter to exit...
```
- Press Enter to exit

## Enjoy Ukrainian or Russian voices while having all the texts in your native language!

- Just launch 'Z.O.N.A' game from Steam as usual.
- Make sure you select the 'Ukrainian' or 'Russian' language in your 'Z.O.N.A' game settings according to your choice of VOICES in the installation executable.

## Restoring original subtitles

- There are two methods available:
  - Either select 'English' in your Z.O.N.A game settings,
  - Or run the shortcut '**auto_ZONA_translator (restore)**' created by the executable in your Z.O.N.A game directory, and confirm that you want to restore the original translation by typing 'y'.
```
 Confirm you want to restore all '0.045' backup binary files (y/n): 
```

# Usage from python sources

## Download the **latest** version of Python for windows for your PC architecture

- [**Windows installer (64-bit)** or **Windows installer (32-bit)**](https://www.python.org/downloads/windows/) 

## Run the installer and follow the prompts to install Python.

## Open python installed console, upgrade pip package and install all following additional packages
```
pip install --upgrade pip
pip install tqdm deepl googletrans==3.1.0a0 legacy-cgi nltk unidecode pywin32
```

## Go to the Latest release:

- [Latest release](https://github.com/peurKe/auto_ZONA_translator/releases)

## Download the sources ZIP archive from the release assets.

- "**Source code (zip)**"

## Extract the **Source code (zip)** archive

- Extract it into your **Z.O.N.A Project X** or **Z.O.N.A Origin** game folder in your Steam library.
  By default in :
    - **Z.O.N.A Project X** :arrow_right: C:\Program Files (x86)\Steam\steamapps\common\ZONA\
    - **Z.O.N.A Origin** :arrow_right: C:\Program Files (x86)\Steam\steamapps\common\ZONAORIGIN\

   NB: if your Z.O.N.A game is installed on a drive other than the C: system drive, your game folder could be in the following location:
    - **Z.O.N.A Project X** :arrow_right: E:\SteamLibrary\steamapps\common\ZONA\
    - **Z.O.N.A Origin** :arrow_right: E:\Steam\Library\steamapps\common\ZONAORIGIN\

   If you want to retrieve your Z.O.N.A game folder, go to your library in Steam and:
    - Right-click on your Z.O.N.A. game in your list of games in the left-hand panel.
    - Click on 'Properties...'
    - Click on 'Browse...'
   An explorer window will appear showing the folder for your Z.O.N.A. game.

## IMPORTANT Be sure your 'Z.O.N.A' game directory contains:

- \\_ auto_ZONA\\ (folder)
- \\_ auto_ZONA_translator\\ (folder)
- \\_ auto_ZONA_translator.py (file)

Not:
- \\_ auto_ZONA_translator-0.x.y-alpha\\ (folder)
    - \\_ auto_ZONA\\ (folder)
    - \\_ auto_ZONA_translator\\ (folder)
    - \\_ auto_ZONA_translator.py (file)

## Go to your game directory.

### Double clic on '**auto_ZONA_translator.py**' to execute python script

## The installation python script then starts automatically

- Select the language you want to translate English from:
```
 Supported source languages:
   uk (ukrainian)
   ru (russian)

 Language to translate from (specify the 2-letter language code):
```

- Select the language you want to translate English to:
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

## Wait for the translation ending, if installation succeed then this message will appears.
```
    To play with this translation:
        1. Just launch 'Z.O.N.A' game from Steam as usual.
        2. Be sure to select 'Ukrainian/Russian' language in 'Z.O.N.A' game's settings.

    /!\ Over the next few days:
        If 'Z.O.N.A' no longer launches correctly or if a new update has been made by AGaming+
        You will need to run this script again to update the translation.

    Press Enter to exit...
```

## Enjoy Russian voices while having all the texts in your native language!

- Just launch 'Z.O.N.A' game from Steam as usual.
- Make sure you select the 'Ukrainian' or 'Russian' language in your 'Z.O.N.A' game settings according to your choice of source language during the python script execution.

## Restoring original subtitles

- There are two methods available:
  - Either select 'English' in your Z.O.N.A game settings,
  - Or run the shortcut '**auto_ZONA_translator (restore)**' created by the executable in your Z.O.N.A game directory, and confirm that you want to restore the original translation by typing 'y'.
```
 Confirm you want to restore all '0.045' backup binary files (y/n): 
```
