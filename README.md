# auto_ZONA_translator

Project for translating all Ukrainian or Russian texts of the following Steam games:
- 'Z.O.N.A Origin' by AGaming+
- 'Z.O.N.A Project X' by AGaming+
- 'CONVRGENCE' by NikZ
- 'Paradox of Hope' by NikZ
And enjoy Ukrainian or Russian voices while having all the texts in your native language!

<!-- TOC -->
- [Discord](#Discord)
- [Prerequisites](#Prerequisites)
- [Currently supported languages](#Currently-supported-languages)
- [Usage from executable installer](#Usage-from-executable-installer)
- [Usage from python sources](#Usage-from-python-sources)
- [Release notes](#Release-notes)
<!-- /TOC -->

# Discord

[Welcome to #zona-translate-deepl!](https://discord.com/channels/1113935727202410691/1302585407308955690)

# Prerequisites

- Your 'Z.O.N.A' or 'CONVRGENCE' game must be up to date.
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

## Download the EXE installer '**auto_ZONA_translator_installer.exe**' from the release assets

The '**auto_ZONA_translator_installer.exe**' installer can be used for all **Z.O.N.A**, **CONVRGENCE** and **Paradox of Hope** games.

Choose your preferred language:
- **auto_ZONA_translator_installer_CS.exe** embedding texts and subtitles for **Czech** only
- **auto_ZONA_translator_installer_DE.exe** embedding texts and subtitles for **German** only
- **auto_ZONA_translator_installer_EN.exe** embedding texts and subtitles for **English** only
- **auto_ZONA_translator_installer_FR.exe** embedding texts and subtitles for **French** only
- **auto_ZONA_translator_installer_FR.exe** embedding texts and subtitles for **Polish** only
- **auto_ZONA_translator_installer_FR.exe** embedding texts and subtitles for **Romanian** only

Or choose the default installer for all other languages:
- **auto_ZONA_translator_installer.exe** embedding texts and subtitles for **all supported languages**

## Copy the downloaded EXE installer into game folder

- Copy it to your **Z.O.N.A Project X** or **Z.O.N.A Origin** or **CONVRGENCE** game folder in your Steam library.
  By default in :
    - **Z.O.N.A Project X** :arrow_right: C:\Program Files (x86)\Steam\steamapps\common\ZONA\
    - **Z.O.N.A Origin** :arrow_right: C:\Program Files (x86)\Steam\steamapps\common\ZONAORIGIN\
    - **CONVRGENCE** :arrow_right: C:\Program Files (x86)\Steam\steamapps\common\CONVRGENCE\

   NB: If your Z.O.N.A game is installed on a drive other than the C: system drive, your game folder could be in the following location:
    - **Z.O.N.A Project X** :arrow_right: E:\SteamLibrary\steamapps\common\ZONA\
    - **Z.O.N.A Origin** :arrow_right: E:\Steam\Library\steamapps\common\ZONAORIGIN\
    - **CONVRGENCE** :arrow_right: E:\Steam\Library\steamapps\common\CONVRGENCE\

   If you want to retrieve your game folder, go to your library in Steam and:
    - Right-click on your game in your list of games in the left-hand panel.
    - Click on 'Properties...'
    - Click on 'Browse...'
   An explorer window will appear showing the folder for your game.
 
## Go to your game directory.

## Double-clic on EXE installer

- Tick the box corresponding to the language of the TEXT and SUBTITLES you wish to read in the game: *(Only for non specific language installer)*
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
- Clic on "Next" button *(Only for non specific language installer)*

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
        1. Just launch your game from Steam as usual.
        2. Be sure to select 'Ukrainian/Russian' language in your game's settings.

    /!\ Over the next few days:
        If your translated game no longer launches correctly or if a new update has been made by AGaming+ or NikZ
        You will need to run this script again to update the translation.

    Press Enter to exit...
```
- Press Enter to exit

## Enjoy Ukrainian or Russian voices while having all the texts in your native language!

- Just launch your game from Steam as usual.
- Make sure you select the '**Ukrainian**' or '**Russian**' language in your your game settings according to your choice of VOICES in the installation executable.

## Restoring original subtitles

- There are two methods available:
  - Either select '**English**' in your game settings,
  - Or run the shortcut '**auto_ZONA_translator (restore)**' created by the executable in your game directory, and confirm that you want to restore the original translation by typing '**y**'.
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
pip install tqdm deepl googletrans==3.1.0a0 legacy-cgi nltk unidecode pywin32 pyinstaller pygetwindow
```

## Go to the Latest release:

- [Latest release](https://github.com/peurKe/auto_ZONA_translator/releases)

## Download the sources ZIP archive from the release assets.

- "**Source code (zip)**"

## Extract the **Source code (zip)** archive

- Extract it into your **Z.O.N.A Project X** or **Z.O.N.A Origin** or **CONVRGENCE** game folder in your Steam library.
  By default in :
    - **Z.O.N.A Project X** :arrow_right: C:\Program Files (x86)\Steam\steamapps\common\ZONA\
    - **Z.O.N.A Origin** :arrow_right: C:\Program Files (x86)\Steam\steamapps\common\ZONAORIGIN\
    - **CONVRGENCE** :arrow_right: C:\Program Files (x86)\Steam\steamapps\common\CONVRGENCE\

   NB: If your Z.O.N.A game is installed on a drive other than the C: system drive, your game folder could be in the following location:
    - **Z.O.N.A Project X** :arrow_right: E:\SteamLibrary\steamapps\common\ZONA\
    - **Z.O.N.A Origin** :arrow_right: E:\Steam\Library\steamapps\common\ZONAORIGIN\
    - **CONVRGENCE** :arrow_right: E:\Steam\Library\steamapps\common\CONVRGENCE\

   If you want to retrieve your game folder, go to your library in Steam and:
    - Right-click on your game in your list of games in the left-hand panel.
    - Click on 'Properties...'
    - Click on 'Browse...'
   An explorer window will appear showing the folder for your game.

## IMPORTANT Be sure your game directory contains:

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

- Select the VOICE language you wish to hear in the game:
```
 Supported source languages:
   uk (ukrainian)
   ru (russian)

 Language to translate from (specify the 2-letter language code):
```

- Select the language of the TEXT and SUBTITLES you wish to read in the game:
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
        1. Just launch your game from Steam as usual.
        2. Be sure to select 'Ukrainian/Russian' language in your game's settings.

    /!\ Over the next few days:
        If your translated game no longer launches correctly or if a new update has been made by AGaming+
        You will need to run this script again to update the translation.

    Press Enter to exit...
```

## Enjoy Russian voices while having all the texts in your native language!

- Just launch your game from Steam as usual.
- Make sure you select the '**Ukrainian**' or '**Russian**' language in your game settings according to your choice of source language during the python script execution.

## Restoring original subtitles

- There are two methods available:
  - Either select '**English**' in your game settings,
  - Or run the shortcut '**auto_ZONA_translator (restore)**' created by the executable in your game directory, and confirm that you want to restore the original translation by typing '**y**'.
```
 Confirm you want to restore all '0.045' backup binary files (y/n): 
```

# Release notes

- v0.1.0
  - initial update

- v0.1.1
  - Now, you can choose your preferred VOICES in the game between Ukrainian (Prypriat's native language) and Russian.

- v0.1.2
  - This release focuses on improving French translations, mainly to correct a few automatic translations. (Thanks to @cameleons for his help)

- v0.1.3
  - For all text languages: A separate database for each language (easier maintenance).

- v0.1.4
  - Only for french text language: faction names are no longer translated to maintain immersion. (Thanks to @cameleons for testing)

- v0.1.5
  - Great improvement in English translations + faction names are no longer translated to maintain immersion.
  - Innosetup's dedicated French installer now offers a French-language interface.
  - Innosetup's dedicated Czech installer has been added, with a Czech-language interface.
  - Innosetup's dedicated German installer has been added, with a German-language interface.
  - Innosetup's dedicated English installer has been added, with an English-language interface.
  - Innosetup's dedicated Polish installer has been added, with a Polish-language interface.

- v0.2.0
  - Added support for **CONVRGENCE** and **Paradox of Hope** games.
  - If the game's save files are invalid, the Steam game file integrity check is now automatically performed by the Steam console, with no manual action required.
  - When the translation is successful, the installation window closes automatically (new behavior).
  - If the translation fails, the installation window waits for user intervention with an error message (as usual).

- v0.2.1
  - Fixed wrong installer name in **README.md** documentation (Thanks @cameleons).
  - Improve **README.md** documentation and format.

- v0.2.2
  - Fixed a bug in the backup game files function that forced Steam game files to be validated even if the game files were valid.
