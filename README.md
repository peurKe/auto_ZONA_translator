# auto_ZONA_translator
Script for translating all Ukrainian or Russian texts of the Steam games '**Z.O.N.A Origin**' and '**Z.O.N.A Project X**' by **AGaming+** and enjoy Russian voices while having all the texts in your native language!

## Prerequisites

  • Your 'Z.O.N.A Origin' or 'Z.O.N.A Project X' game must be up to date.
  
  • Your PC has an Internet connection for Google Translator or Deepl API requests.
  
  • You have a valid API auth key if you use Deepl API requests with the "-t 'deepl'" and "-ta 'xxx'" parameters.

## Currently supported languages

  • **fr** = français
  
  • **cs** = čeština (Not yet validated)
  
  • **da** = dansk (Not yet validated)
  
  • **es** = español (Not yet validated)
  
  • **fi** = suomi (Not yet validated)

  • **hu** = magyar (Not yet validated)
  
  • **it** = italiano (Not yet validated)
  
  • **nl** = Nederlands (Not yet validated)
  
  • **pl** = polski (Not yet validated)
  
  • **pt** = português (Not yet validated)
  
  • **ro** = română (Not yet validated)
  
  • **sv** = svenska (Not yet validated)

## Usage from binary release

• Go to the latest release:

  https://github.com/peurKe/auto_ZONA_translator/releases

• Download the archive "**auto_ZONA_translator_[GAME]_[LANGUAGE].zip**" corresponding to your game and language.

• Extract the archive content into your game directory.

• Go to your game directory.

• Execute '**auto_ZONA_translator.exe**'

  1. Press Enter if prerequisites displayed on the screen are correct:
```
    • Your 'Z.O.N.A Origin' game must be up to date.
    • Your PC has an Internet connection for Google Translator or Deepl API requests.
    • You have a valid API auth key if you use Deepl API requests with the "-t 'deepl'" and "-ta 'xxx'" parameters.
```
  2. Select the language you want to translate English to:
```
 Supported languages:
   cs (čeština)
   da (dansk)
   es (español)
   fi (suomi)
   fr (français)
   hu (magyar)
   it (italiano)
   nl (Nederlands)
   pl (polski)
   pt (português)
   ro (română)
   sv (svenska)

 Language to translate to (specify the 2-letter language code):
```

  3. Wait for the translation ending.

  4. Enjoy Russian voices while having all the texts in your native language!

• To restore original translation, execute the shortcut '**auto_ZONA_translator (restore)**' created by the executable

  Confirm you want to restore original translation (y/n)
```
 Confirm you want to restore all '0.035' backup binary files (y/n):
```

## Usage from sources

• Download the **latest** version of Python for windows for your PC architecture :

   **Windows installer (64-bit)** or **Windows installer (32-bit)**
   
   https://www.python.org/downloads/windows/
        
• Run the installer and follow the prompts to install Python.

• Open python installed console, upgrade pip package and install all following additional packages:

    pip install --upgrade pip
    pip install tqdm deepl googletrans==3.1.0a0 legacy-cgi nltk unidecode pywin32

• Download the archive "**auto_ZONA_translator_SRC.zip**".

• Extract the archive content into your game directory.

• Go to your game directory.

• Double clic on '**auto_ZONA_translator.py**' to execute script

  1. Press Enter if prerequisites displayed on the screen are correct:
```
    • Your 'Z.O.N.A Origin' game must be up to date.
    • Your PC has an Internet connection for Google Translator or Deepl API requests.
    • You have a valid API auth key if you use Deepl API requests with the "-t 'deepl'" and "-ta 'xxx'" parameters.
```
  2. Select the language you want to translate English to:
```
 Supported languages:
   cs (čeština)
   da (dansk)
   es (español)
   fi (suomi)
   fr (français)
   hu (magyar)
   it (italiano)
   nl (Nederlands)
   pl (polski)
   pt (português)
   ro (română)
   sv (svenska)

 Language to translate to (specify the 2-letter language code):
```

  3. Wait for the translation ending.

  4. Enjoy Russian voices while having all the texts in your native language!

• To restore original translation, execute the shortcut '**auto_ZONA_translator (restore)**' created by the executable

  Confirm you want to restore original translation (y/n)
```
 Confirm you want to restore all '0.035' backup binary files (y/n):
```
