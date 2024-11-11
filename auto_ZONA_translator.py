#!python
# -*- coding: utf-8 -*-
"""
Title : auto_ZONA_translator.py
Description : Script for translating all Ukrainian or Russian texts of the Steam games 'Z.O.N.A Origin' and 'Z.O.N.A Project X' by AGaming+ and enjoy Ukrainian voices while having all the texts in your native language!
Author: peurKe
Creation Date: 2024-10-31
Last Modified: 2024-11-11
Version: 0.1.1-alpha
License: MIT
"""

# https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe
# https://www.python.org/ftp/python/3.13.0/python-3.13.0.exe
# https://gist.github.com/williballenthin/8e3913358a7996eab9b96bd57fc59df2 (broken)
# https://gist.github.com/jedimasterbot/39ef35bc4324e4b4338a210298526cd0 (fixed)
# https://github.com/ssut/py-googletrans/issues/280
# https://medium.com/analytics-vidhya/removing-stop-words-with-nltk-library-in-python-f33f53556cc1

# pip install --upgrade pip
# pip install tqdm googletrans==3.1.0a0 legacy-cgi nltk unidecode pywin32 pyinstaller
# pip install tqdm
# pip install googletrans==3.1.0a0
# pip install legacy-cgi
# pip install nltk
# pip install unidecode
# pip install pywin32
# pip install pyinstaller

# Error: The read operation timed out --> Problem with google translator API = Relaunch script
# Error: _ssl.c:1003: The handshake operation timed out --> Problem with google translator API = Relaunch script
# Error: [Errno 11001] getaddrinfo failed --> Internet connection problem = Check Internet connection and relanch script
# Error: [WinError 10013] An attempt has been made to access a socket in a way prohibited by its access authorisations. --> Internet connection problem = Check Internet connection and relanch script
# Error: bytes must be in range(0, 256) --> There is unicode character somewhere in element['translation'] string

import argparse
import sys
from os import path as os_path, makedirs as os_makedirs, listdir as os_listdir, rename as os_rename, rmdir as os_rmdir, remove as os_remove, getcwd as os_getcwd
from datetime import datetime
from inspect import currentframe
import re
from time import sleep as time_sleep, time as time_time
from tqdm import tqdm
from unidecode import unidecode
from json import dumps as json_dumps
import shutil
from collections import namedtuple
from auto_ZONA.utils.DBManager import DBManager
try:
    # from nltk.corpus import stopwords
    from nltk import download as nltk_download
    from nltk.tokenize import word_tokenize
    from deepl import Translator as deepl_Translator, AuthorizationException as AuthorizationException_deepl
    from googletrans import Translator as googletrans_Translator
    from win32com.client import Dispatch as w32_dispatch
    import getpass
    from msvcrt import getch as msvcrt_getch
except Exception as e:
    print(f" Error: {e}")
    input(f" Press Enter to exit...")
    sys.exit(-1)

class bcolors:
    OK = '\033[92m'
    INFO = '\033[93m'
    WARN = '\033[38;5;208m'
    FAIL = '\033[91m'
    ASK = '\033[96m'
    NOTIF = '\033[42m'
    ENDC = '\033[0m'

# # /!\ By default, binary files are now retrieved dynamically.
# DEFAULT_FILES = [
#     'level0', 'level1', 'level2', 'level3', 'level4', 'level5', 'level6', 'level7',
#     'level8', 'level9', 'level10', 'level11', 'level12', 'level13', 'level14', 'level15',
#     'level16', 'level17', 'level18', 'level19', 'level20', 'level21', 'level22', 'level23',
#     'level24', 'level25', 'level26', 'level27', 'level28', 'level29', 'resources.assets'
# ]
# # FOR TESTING PURPOSES ONLY
# # DEFAULT_FILES = [ 'level0' ]

# BEGIN auto_ZONA_translator
DEFAULT_ZONA_TRANSLATE_NAME = 'auto_ZONA_translator'
DEFAULT_ZONA_TRANSLATE_DIR_NAME = DEFAULT_ZONA_TRANSLATE_NAME
DEFAULT_ZONA_TRANSLATE_DIR = f"./{DEFAULT_ZONA_TRANSLATE_DIR_NAME}"
DEFAULT_ZONA_TRANSLATE_CFG_FILE = f"./{DEFAULT_ZONA_TRANSLATE_DIR_NAME}/{DEFAULT_ZONA_TRANSLATE_NAME}.cfg"
DEFAULT_ZONA_TRANSLATE_DIR = f"./{DEFAULT_ZONA_TRANSLATE_DIR_NAME}"
DEFAULT_ZONA_TRANSLATE_DB_DIR_NAME = ''
DEFAULT_ZONA_TRANSLATE_DB_DIR = f"{DEFAULT_ZONA_TRANSLATE_DIR}/{DEFAULT_ZONA_TRANSLATE_DB_DIR_NAME}"
DEFAULT_ZONA_TRANSLATE_DB_NAME = { "zona": "ZONA_ProjectX.db", "zonaorigin": "ZONA_Origin.db" }  # Keys are based on game directory in 'DEFAULT_ZONA_DIR_NAME'
DEFAULT_ZONA_TRANSLATE_BACKUP_DIR_NAME = 'BACKUP'
# '@PLACEHOLDER_VERSION_DIR' will be replaced with current game version
DEFAULT_ZONA_TRANSLATE_BACKUP_DIR = f"{DEFAULT_ZONA_TRANSLATE_DIR}/@PLACEHOLDER_VERSION_DIR/{DEFAULT_ZONA_TRANSLATE_BACKUP_DIR_NAME}"
# Flag for data binary file translated
DEFAULT_ZONA_TRANSLATE_STR_IN_BINARY = f"THIS_FILE_WAS_TRANSLATED_WITH_{DEFAULT_ZONA_TRANSLATE_NAME}"
DEFAULT_ZONA_TRANSLATE_SUCCEED_FILE = 'done.txt'
DEFAULT_ZONA_TRANSLATE_RESTORE_SHORTCUT = f"{DEFAULT_ZONA_TRANSLATE_NAME} (restore).lnk"
DEFAULT_ZONA_TRANSLATE_DEBUG_FILE = f"{DEFAULT_ZONA_TRANSLATE_NAME}.log"
DEFAULT_ZONA_TRANSLATE_WITH_AUTHENT = ['deepl']
DEFAULT_ZONA_TRANSLATE_LANG_SRC = 'uk'
DEFAULT_TRANSLATE_FUNCTION = 'dialog_translate_google'
# END auto_ZONA_translator

# List for checking executable presence
DEFAULT_ZONA_FILENAME_LIST = [ 'ZONAORIGIN.exe', 'ZONA.exe' ]

# # BEGIN Z.O.N.A ORIGIN
# DEFAULT_ZONA_GAME_NAME = 'Z.O.N.A Origin'
# DEFAULT_ZONA_DIR_NAME = 'ZONAORIGIN'
# DEFAULT_ZONA_DIR_EXAMPLE = f"C:\\SteamLibrary\\steamapps\\common\\{DEFAULT_ZONA_DIR_NAME}"
# DEFAULT_ZONA_DATA_DIR_NAME = 'ZONAORIGIN_Data'
# DEFAULT_ZONA_DATA_DIR = f"./{DEFAULT_ZONA_DATA_DIR_NAME}"
# DEFAULT_ZONA_GLOBAL_GM = 'globalgamemanagers'
# DEFAULT_ZONA_VERSION_REGEX = rb'(0\.0[0-9][0-9])'
# DEFAULT_ZONA_TRANSLATE_LANG_SRC = 'ru'
# # END Z.O.N.A ORIGIN

# BEGIN Z.O.N.A PROJECT X
DEFAULT_ZONA_GAME_NAME = 'Z.O.N.A Project X'
DEFAULT_ZONA_DIR_NAME = 'ZONA'
DEFAULT_ZONA_DIR_EXAMPLE = f"C:\\SteamLibrary\\steamapps\\common\\{DEFAULT_ZONA_DIR_NAME}"
DEFAULT_ZONA_DATA_DIR_NAME = 'ZONA_Data'
DEFAULT_ZONA_DATA_DIR = f"./{DEFAULT_ZONA_DATA_DIR_NAME}"
DEFAULT_ZONA_GLOBAL_GM = 'globalgamemanagers'
DEFAULT_ZONA_VERSION_REGEX = rb'(1\.0[0-9]\.[0-9][0-9])'
DEFAULT_ZONA_TRANSLATE_LANG_SRC = 'uk'
# END Z.O.N.A PROJECT X

ALL_SUPPORTED_SOURCE_LANGS = ['uk', 'ru']
ALL_SUPPORTED_LANGS = ['cs', 'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'nl', 'pl', 'pt', 'ro', 'sv']
ALL_SUPPORTED_LANGS_DB = {
    "cs": "Čeština",
    "da": "Dansk",
    "de": "German",
    "en": "English",
    "es": "Español",
    "fi": "Suomi",
    "fr": "Français",
    "hu": "Magyar",
    "it": "Italiano",
    "nl": "Nederlands",
    "pl": "Polski",
    "pt": "Português",
    "ro": "Română",
    "sv": "Svenska",
    "ru": "Russian",  # Source language
    "uk": "Ukrainian"  # Source language
}
# Supported sources languages
ALL_SUPPORTED_SOURCE_LANGS_DESCRIPTION_LIST = [
    f"   {bcolors.ASK}uk{bcolors.ENDC} {bcolors.INFO}(ukrainian){bcolors.ENDC}\n",
    f"   {bcolors.ASK}ru{bcolors.ENDC} {bcolors.INFO}(russian){bcolors.ENDC}\n"
]
ALL_SUPPORTED_SOURCE_LANGS_DESCRIPTION = " Supported source languages:\n" + ''.join(ALL_SUPPORTED_SOURCE_LANGS_DESCRIPTION_LIST)
# Supported translated languages
ALL_SUPPORTED_LANGS_DESCRIPTION_LIST = [
    f"   {bcolors.ASK}cs{bcolors.ENDC} {bcolors.INFO}(čeština){bcolors.ENDC}\n",
    f"   {bcolors.ASK}da{bcolors.ENDC} {bcolors.INFO}(dansk){bcolors.ENDC}\n",
    f"   {bcolors.ASK}es{bcolors.ENDC} {bcolors.INFO}(español){bcolors.ENDC}\n",
    f"   {bcolors.ASK}fi{bcolors.ENDC} {bcolors.INFO}(suomi){bcolors.ENDC}\n",
    f"   {bcolors.ASK}fr{bcolors.ENDC} {bcolors.INFO}(français){bcolors.ENDC}\n",
    f"   {bcolors.ASK}hu{bcolors.ENDC} {bcolors.INFO}(magyar){bcolors.ENDC}\n",
    f"   {bcolors.ASK}it{bcolors.ENDC} {bcolors.INFO}(italiano){bcolors.ENDC}\n",
    f"   {bcolors.ASK}nl{bcolors.ENDC} {bcolors.INFO}(Nederlands){bcolors.ENDC}\n",
    f"   {bcolors.ASK}pl{bcolors.ENDC} {bcolors.INFO}(polski){bcolors.ENDC}\n",
    f"   {bcolors.ASK}pt{bcolors.ENDC} {bcolors.INFO}(português){bcolors.ENDC}\n",
    f"   {bcolors.ASK}ro{bcolors.ENDC} {bcolors.INFO}(română){bcolors.ENDC}\n",
    f"   {bcolors.ASK}sv{bcolors.ENDC} {bcolors.INFO}(svenska){bcolors.ENDC}\n"
]
ALL_SUPPORTED_LANGS_DESCRIPTION = " Supported languages:\n" + ''.join(ALL_SUPPORTED_LANGS_DESCRIPTION_LIST)
ALL_SUPPORTED_LANGS_SRC = ['empty', 'uk', 'ru']

# Regular expression for Cyrillic bytes (Russian + Specific + Ukrainian pattern)
# CYRILLIC_BYTES = rb'\xD0[\x90-\xBF]|\xD1[\x80-\x8F]'  # OK
# CYRILLIC_BYTES = rb'\xD0[\x80-\xBF]|\xD1[\x80-\xBF]|\xD2[\x80-\xBF]|\xD3[\x80-\xBF]'  # BETTER
CYRILLIC_BYTES = {
    'ru': rb'\xD0[\x80-\xBF]|\xD1[\x80-\xBF]|\xD2[\x80-\xBF]|\xD3[\x80-\xBF]|\xD4[\x80-\x8F]',  # TO BE VALIDATED
    # 'uk': rb'\xD0[\x90-\xBF]|\xD0[\xA0-\xFF]|\xD1[\x00-\x8F]',  # NOK (too short list)
    'uk': rb'\xD0[\x80-\xBF]|\xD0[\xA0-\xFF]|\xD1[\x00-\xBF]|\xD3[\x80-\xBF]|\xD4[\x80-\x8F]',  # TO BE VALIDATED
}

# Specific Cyrillic bytes
SPECIFIC_CYRILLIC_BYTES_VR = rb'\x56\x52\x3F\x20'  # 'VR? '
# SPECIFIC_BYTES_NO = rb'\xE2\x84\x96'  # '№' (finally not translated because translation in french is quite bad: no)
# SPECIFIC_BYTES_DASH = rb'\xE2\x80\x94'  # '—' (long dash) (finally not translated because translation in french is not usefull: no)

# Latin punctuation bytes
LATIN_PUNCTUATION_BYTES = rb'\x0a|\x20|\x21|\x22|\x27|\x28|\x29|\x2B|\x2C|\x2D|\x2E|\x2F|\x3A|\x3F|\x5C|\x5F'

# Regular expression for Cyrillic characters (Russian + Specific + Ukrainian pattern) and Latin punctuation
# CYRILLIC_PATTERN = rb'(\xD0[\x90-\xBF]|\xD1[\x80-\x8F]|\x0a|\x20|\x21|\x22|\x27|\x28|\x29|\x2B|\x2C|\x2D|\x2E|\x2F|\x5C|\x5F)'
# CYRILLIC_PATTERN = rb'(\xE2\x80\x94|\xD0[\x81\x86-\xBF]|\xD1[\x80-\x8F]|\xD2[\x90-\x91]|\xD2[\x84\x94]|\xD1\x96|\xD0[\x90-\xAF]|\x0a|\x20|\x21|\x22|\x27|\x28|\x29|\x2B|\x2C|\x2D|\x2E|\x2F|\x3A|\x3F\x5C|\x5F)'  # Regular expression for Cyrillic characters + CRLF + Latin punctuation
# CYRILLIC_PATTERN = rb'(\x56\x52\x3F\x20|\xE2\x80\x94|'+ CYRILLIC_BYTES + rb'|\x0a|\x20|\x21|\x22|\x27|\x28|\x29|\x2B|\x2C|\x2D|\x2E|\x2F|\x3A|\x3F|\x5C|\x5F)'  # Regular expression for Cyrillic characters + CRLF + Latin punctuation
# CYRILLIC_PATTERN = rb'(' + SPECIFIC_CYRILLIC_BYTES_VR + rb'|' + CYRILLIC_BYTES[DEFAULT_ZONA_TRANSLATE_LANG_SRC] + rb'|' + LATIN_PUNCTUATION_BYTES + rb')'  # Regular expression for Cyrillic characters + CRLF + Latin punctuation
CYRILLIC_PATTERN = rb''  # See initialization in main() rigth after arguments parsing

# \x56\x52\x3F\x20 = 'VR? '
# \xE2\x84\x96 = '№' (finally not translated because translation in french is quite bad: no)
# \xE2\x80\x94 = '—' (long dash) (finally not translated because translation in french is not usefull: no)
# \xD0[\x81\x86-\xBF]|\xD1[\x80-\x8F]|\xD2[\x90-\x91]|\xD2[\x84\x94]|\xD1\x96|\xD0[\x90-\xAF] = Cyrillic
# \x0a|\x20|\x21|\x22|\x27|\x28|\x29|\x2B|\x2C|\x2D|\x2E|\x2F|\x3A|\x3F|\x5C|\x5F = Punctuation

# # Cyrillic bytes to select
# \xD0[\x81\x86-\xBF] : Correspond aux caractères UTF-8 cyrilliques dans la plage D0 81, D0 86, et de D0 90 à D0 BF.
# \xD1[\x80-\x8F] : Correspond aux caractères cyrilliques de D1 80 à D1 8F.
# \xD2[\x90-\x91] et \xD2[\x84\x94] : Correspond aux caractères spécifiques comme Ґ et Є.
# \xD1\x96 et \xD0[\x90-\xAF] : Inclut le caractère ukrainien і et d'autres caractères de base de la langue russe et ukrainienne.
# cyrillic_bytes = [
#     b'\xD0\x90', b'\xD0\x91', b'\xD0\x92', b'\xD0\x93', b'\xD0\x94',
#     b'\xD0\x95', b'\xD0\x81', b'\xD0\x96', b'\xD0\x97', b'\xD0\x98',
#     b'\xD0\x99', b'\xD0\x9A', b'\xD0\x9B', b'\xD0\x9C', b'\xD0\x9D',
#     b'\xD0\x9E', b'\xD0\x9F', b'\xD0\xA0', b'\xD0\xA1', b'\xD0\xA2',
#     b'\xD0\xA3', b'\xD0\xA4', b'\xD0\xA5', b'\xD0\xA6', b'\xD0\xA7',
#     b'\xD0\xA8', b'\xD0\xA9', b'\xD0\xAA', b'\xD0\xAB', b'\xD0\xAC',
#     b'\xD0\xAD', b'\xD0\xAE', b'\xD0\xAF', b'\xD0\xB0', b'\xD0\xB1',
#     b'\xD0\xB2', b'\xD0\xB3', b'\xD0\xB4', b'\xD0\xB5', b'\xD0\xB6',
#     b'\xD0\xB7', b'\xD0\xB8', b'\xD0\xB9', b'\xD0\xBA', b'\xD0\xBB',
#     b'\xD0\xBC', b'\xD0\xBD', b'\xD0\xBE', b'\xD0\xBF', b'\xD1\x80',
#     b'\xD1\x81', b'\xD1\x82', b'\xD1\x83', b'\xD1\x84', b'\xD1\x85',
#     b'\xD1\x86', b'\xD1\x87', b'\xD1\x88', b'\xD1\x89', b'\xD1\x8A',
#     b'\xD1\x8B', b'\xD1\x8C', b'\xD1\x8D', b'\xD1\x8E', b'\xD1\x8F',
#     # Special characters
#     b'\x0a',   # LF
#     b'\x20'    # Whitespace
#     b'\x21',   # !
#     b'\x22',   # "
#     b'\x27',   # '
#     b'\x28',   # (
#     b'\x29',   # )
#     b'\x2B',   # +
#     b'\x2C',   # ,
#     b'\x2D',   # -
#     b'\x2E',   # .
#     b'\x2F',   # /
#     b'\x3A',   # :
#     b'\x3F',   # ?
#     b'\x5C',   # \
#     b'\x5F',   # _
# ]

# To fix (level11)
# заброшенне cело||D0 97 D0 B0 D0 B1 D1 80 D1 BE D1 88 D0 B5 D0 BD D0 BD D0 BE D0 B5

# Latin	Char Unicode	Hex (UTF-8)	Binaire (UTF-8)
# A	    А	U+0410	D0 90	11010000 10100000
# B	    Б	U+0411	D0 91	11010000 10100001
# V	    В	U+0412	D0 92	11010000 10100010
# G	    Г	U+0413	D0 93	11010000 10100011
# D	    Д	U+0414	D0 94	11010000 10100100
# E	    Е	U+0415	D0 95	11010000 10100101
# Yo	Ё	U+0401	D0 81	11010000 10000001
# Zh	Ж	U+0416	D0 96	11010000 10100110
# Z 	З	U+0417	D0 97	11010000 10100111
# I 	И	U+0418	D0 98	11010000 10101000
# Y 	Й	U+0419	D0 99	11010000 10101001
# K 	К	U+041A	D0 9A	11010000 10101010
# L 	Л	U+041B	D0 9B	11010000 10101011
# M 	М	U+041C	D0 9C	11010000 10101100
# N 	Н	U+041D	D0 9D	11010000 10101101
# O 	О	U+041E	D0 9E	11010000 10101110
# P 	П	U+041F	D0 9F	11010000 10101111
# R 	Р	U+0420	D0 A0	11010000 10110000
# S 	С	U+0421	D0 A1	11010000 10110001
# T 	Т	U+0422	D0 A2	11010000 10110010
# U 	У	U+0423	D0 A3	11010000 10110011
# F 	Ф	U+0424	D0 A4	11010000 10110100
# Kh	Х	U+0425	D0 A5	11010000 10110101
# Ts	Ц	U+0426	D0 A6	11010000 10110110
# Ch	Ч	U+0427	D0 A7	11010000 10110111
# Sh	Ш	U+0428	D0 A8	11010000 10111000
# Shch	Щ	U+0429	D0 A9	11010000 10111001
# Hard Sign	Ъ	U+042A	D0 AA	11010000 10111010
# Y (with hook)	Ы	U+042B	D0 AB	11010000 10111011
# Soft Sign	Ь	U+042C	D0 AC	11010000 10111100
# E 	Э	U+042D	D0 AD	11010000 10111101
# Yu	Ю	U+042E	D0 AE	11010000 10111110
# Ya	Я	U+042F	D0 AF	11010000 10111111
# a	    а	U+0430	D0 B0	11010000 10110000
# b	    б   U+0431	D0 B1	11010000 10110001
# v	    в	U+0432	D0 B2	11010000 10110010
# g 	г	U+0433	D0 B3	11010000 10110011
# d 	д	U+0434	D0 B4	11010000 10110100
# e 	е	U+0435	D0 B5	11010000 10110101
# yo	ё	U+0451	D1 91	11010001 10010001
# zh	ж	U+0436	D0 B6	11010000 10110110
# z 	з	U+0437	D0 B7	11010000 10110111
# i 	и	U+0438	D0 B8	11010000 10111000
# y 	й	U+0439	D0 B9	11010000 10111001
# k 	к	U+043A	D0 BA	11010000 10111010
# l 	л	U+043B	D0 BB	11010000 10111011
# m 	м	U+043C	D0 BC	11010000 10111100
# n 	н	U+043D	D0 BD	11010000 10111101
# o 	о	U+043E	D0 BE	11010000 10111110
# p 	п	U+043F	D0 BF	11010000 10111111
# r 	р	U+0440	D1 80	11010001 10000000
# s 	с	U+0441	D1 81	11010001 10000001
# t 	т	U+0442	D1 82	11010001 10000010
# u 	у	U+0443	D1 83	11010001 10000011
# f 	ф	U+0444	D1 84	11010001 10000100
# kh	х	U+0445	D1 85	11010001 10000101
# ts	ц	U+0446	D1 86	11010001 10000110
# ch	ч	U+0447	D1 87	11010001 10000111
# sh	ш	U+0448	D1 88	11010001 10001000
# shch	щ	U+0449	D1 89	11010001 10001001
# hard sign	ъ	U+044A	D1 8A	11010001 10001010
# y (with hook)	ы	U+044B	D1 8B	11010001 10001011
# soft sign	ь	U+044C	D1 8C	11010001 10001100
# e 	э	U+044D	D1 8D	11010001 10001101
# yu	ю	U+044E	D1 8E	11010001 10001110
# ya	я	U+044F	D1 8F	11010001 10001111

String = namedtuple("String", ["s", "offset", "binary_length", "ascii_length"])

CUSTOM_TARGET_STOPWORDS = {
    "en": [ 'the', 'to', 'and', 'a', 'in', 'it', 'is', 'that', 'this', 'had', 'on', 'for', 'were', 'was' ],
    "fr": [ 'a', 'abord', 'alors', 'aucun', 'aucune', 'avec', 'avoir', 'car', 'ce', 'cela', 'ces', 'cette', 'contre', 'dans', 'de', 'des', 'du', 'en', 'et', 'il', 'ils', 'je', 'la', 'le', 'les', 'mais', 'me', 'mon', 'ne', 'ni', 'nous', 'on', 'ou', 'par', 'pour', 'que', 'qui', 'quoi', 'sa', 'si', 'son', 'sur', 'ta', 'te', 'toi', 'ton', 'un', 'une', 'vous', 'y', 'dans', 'pouvez', 'peut', 'serait', 'aura', 'doit', 'etre' ],
    "de": ['aber', 'abzug', 'alle', 'allem', 'allen', 'aller', 'alles', 'als', 'ander', 'andere', 'anderem', 'anderen', 'anderer', 'anderes', 'anderm', 'andern', 'anders', 'angekommen', 'auch', 'auf', 'bei', 'benutzt', 'ber', 'berfalls', 'berleben', 'berraschungen', 'bewegungen', 'bist', 'bleibt', 'damit', 'dann', 'derselbe', 'derselben', 'denselben', 'desselben', 'demselben', 'dieselbe', 'dieselben', 'dass', 'dasselbe', 'dazu', 'dein', 'deine', 'deinem', 'deinen', 'deiner', 'deines', 'den', 'denn', 'der', 'derer', 'des', 'dessen', 'dich', 'diesem', 'diesen', 'dieser', 'doch', 'dormitory', 'durch', 'ein', 'eine', 'einem', 'einen', 'einer', 'eines', 'einheit', 'einig', 'einige', 'einigem', 'einigen', 'einiger', 'einiges', 'einmal', 'erinnert', 'ihm', 'etwas', 'euer', 'eure', 'eurem', 'euren', 'eurer', 'eures', 'fur', 'gesch', 'gegen', 'gewehr', 'gewesen', 'gibt', 'habe', 'haben', 'hallo', 'hatte', 'hatten', 'hauptquartier', 'hilft', 'hin', 'hinter', 'ich', 'im', 'kamera', 'kugelflug', 'mich', 'mir', 'ihr', 'ihm', 'ihn', 'ihnen', 'indem', 'infizierte', 'ist', 'jede', 'jedem', 'jeden', 'jeder', 'jedes', 'jener', 'jenem', 'jenen', 'jener', 'jenes', 'jetzt', 'kalorien', 'kann', 'kannst', 'kein', 'keine', 'keinem', 'keinen', 'keiner', 'keines', 'konnen', 'konnte', 'machen', 'manchem', 'manchen', 'mancher', 'manches', 'mein', 'meine', 'meinem', 'meinen', 'meiner', 'meines', 'monolithen', 'muss', 'musste', 'nach', 'nicht', 'nichts', 'nun', 'nur', 'nutzen', 'oder', 'ohne', 'patrone', 'patronem', 'perfekt', 'perfekte', 'risches', 'sehr', 'sein', 'seine', 'seinem', 'seinen', 'seiner', 'seines', 'selbst', 'sich', 'sie', 'siehst', 'sind', 'solche', 'solchem', 'solchen', 'solcher', 'solches', 'sollte', 'sondern', 'sonst', 'sowohl', 'uber', 'und', 'uns', 'unser', 'unsere', 'unserem', 'unseren', 'unseres', 'unter', 'verbrennen', 'viel', 'vom', 'vor', 'vorbereiten', 'wahrend', 'waren', 'warst', 'weg', 'welche', 'welchem', 'welchen', 'welcher', 'welches', 'welt', 'wenn', 'werde', 'werden', 'wie', 'wieder', 'wir', 'wird', 'wirst', 'wollen', 'wollte', 'wohnheim', 'wurde', 'wurden', 'zug', 'zum', 'zur', 'zwar', 'zwischen'],
    "cs": [ 'a', 'ale', 'aniz', 'az', 'bude', 'by', 'byl', 'byla', 'bylo', 'byly', 'co', 'do', 'jak', 'jako', 'je', 'jedna', 'jeste', 'jeho', 'jejich', 'jsem', 'jsi', 'k', 'kdyz', 'ktera', 'ktere', 'ktery', 'ma', 'mam', 'mit', 'muze', 'my', 'na', 'nebo', 'nekdo', 'neni', 'o', 'od', 'ona', 'oni', 'po', 'pod', 'pokud', 'pro', 'proti', 'rezim', 'se', 'si', 'svuj', 'svoje', 'ta', 'tak', 'ten', 'to', 'tu', 'uz', 'vam', 'vas', 'vy', 'z', 'za', 'ze', 'musite', 'musi', 'bude' ],
    "it": [ 'a', 'ad', 'al', 'alla', 'alle', 'altro', 'ancora', 'anche', 'aspetta', 'avere', 'che', 'come', 'con', 'contro', 'cosa', 'da', 'dai', 'dal', 'de', 'di', 'dove', 'e', 'fai', 'fara', 'gia', 'ha', 'hanno', 'il', 'in', 'io', 'la', 'le', 'lo', 'loro', 'ma', 'me', 'mi', 'mio', 'modalita', 'ne', 'noi', 'nostro', 'o', 'per', 'piu', 'quale', 'quando', 'che', 'chi', 'sono', 'su', 'tra', 'tu', 'un', 'una', 'voi', 'sarebbe', 'deve', 'puo' ],
    "es": [ 'a', 'al', 'ante', 'bajo', 'como', 'con', 'contra', 'cuanto', 'de', 'del', 'desde', 'donde', 'durante', 'el', 'ella', 'ellos', 'en', 'entre', 'es', 'esta', 'estoy', 'ha', 'hace', 'hay', 'lo', 'los', 'me', 'mi', 'mismo', 'modo', 'muy', 'nada', 'nos', 'nuestro', 'o', 'para', 'pero', 'por', 'que', 'quien', 'si', 'sin', 'sobre', 'su', 'sus', 'te', 'tu', 'un', 'una', 'y' ],
    "ro": [ 'a', 'acesta', 'aceste', 'adica', 'altceva', 'altul', 'am', 'an', 'as', 'atunci', 'ba', 'bai', 'bi', 'de', 'decat', 'din', 'dintre', 'este', 'eu', 'fara', 'fie', 'fiecare', 'fiecare', 'in', 'impotriva', 'la', 'ma', 'me', 'mi', 'mii', 'mod', 'o', 'pe', 'poate', 'propria', 'propriile', 'sau', 'se', 'si', 'sunt', 'tine', 'tu', 'un', 'una', 'vor', 'va' ],
    "pl": [ 'a', 'ale', 'by', 'c', 'co', 'd', 'da', 'dla', 'do', 'i', 'jak', 'je', 'jeden', 'jedna', 'kiedy', 'ktory', 'moze', 'na', 'ni', 'o', 'od', 'ona', 'oni', 'po', 'pomiedzy', 'przeciwko', 'przed', 'przy', 'sa', 'si', 'tak', 'to', 'tryb', 'tu', 'w', 'wszystko', 'z', 'za' ]
}

RESTORE_SPECIFIC_WORDS = {
    "cs": [
        { "from": "tracker", "to": "Stalker", "case_sensitive": False },
        { "from": "psi", "to": "Psych", "case_sensitive": False }
    ],
    "da": [],
    "de": [
        { "from": "tracker", "to": "Stalker", "case_sensitive": False }
    ],
    "en": [
        { "from": "tracker", "to": "Stalker", "case_sensitive": False }
    ],
    "es": [
        { "from": "acosador", "to": "Stalker", "case_sensitive": False },
        { "from": "rastreador", "to": "Stalker", "case_sensitive": False }
    ],
    "fr": [
        { "from": "harceleur", "to": "Stalker", "case_sensitive": False },
        { "from": "traqueur", "to": "Stalker", "case_sensitive": False },
        { "from": "stalkers gratuits", "to": "Stalkers Libres", "case_sensitive": False },
        { "from": "ihor", "to": "IGOR", "case_sensitive": False },
        { "from": "voron", "to": "Corbeau", "case_sensitive": False },
        { "from": "shelter", "to": "Abri", "case_sensitive": False },  # Origin / Ukrainian + Russian / level11
        { "from": "refuge", "to": "Abri", "case_sensitive": False },  # Origin / Ukrainian + Russian / level11
        { "from": "asile", "to": "Abri", "case_sensitive": False },  # Origin / Russian / level11
        { "from": "but. menu", "to": "Retour", "case_sensitive": False },
        { "from": "plus loin", "to": "Suivant", "case_sensitive": False },
        { "from": "le bon controleur", "to": "Le controleur droit", "case_sensitive": False },
        { "from": "œ", "to": "oe", "case_sensitive": False },
        { "from": "cheveux gris", "to": "Gray", "case_sensitive": False },
        { "from": "comme 'val'", "to": "AS 'Val'", "case_sensitive": False },
        { "from": "comme \"val\"", "to": "AS 'Val'", "case_sensitive": False },
        { "from": "Entree", "to": "Quitter", "case_sensitive": True },  # Origin / Ukrainian
        { "from": "l'Exode", "to": "quitter", "case_sensitive": True },  # Origin / Ukrainian
        { "from": "Exode", "to": "Quitter", "case_sensitive": True },  # Origin / Ukrainian
        { "from": "Cantonnement", "to": "Ville militaire", "case_sensitive": True },  # Origin / Ukrainian / level11
        { "from": "Gage", "to": "Avant-poste", "case_sensitive": True },  # Origin / Ukrainian / level11
        { "from": "Village Topp", "to": "Marais du village", "case_sensitive": True },  # Origin / Ukrainian / level11
        { "from": "a mange", "to": "ite", "case_sensitive": True }  # Origin / Russian / level11 / 'Cело' with a latin 'C' = Village Russian / 'ело' = a mangé / 'Cело' = 'Ca mang' => Cite 
    ],
    "fi": [],
    "hu": [],
    "it": [
        { "from": "tracker", "to": "Stalker", "case_sensitive": False }
    ],
    "nl": [],
    "pl": [
        { "from": "tracker", "to": "Stalker", "case_sensitive": False }
    ],
    "pt": [],
    "ro": [
        { "from": "urmaritor", "to": "Stalker", "case_sensitive": False },
        { "from": "tracker", "to": "Stalker", "case_sensitive": False }
    ],
    "sv": [],
    "all": [
        { "from": "pripiat", "to": "Prypiat", "case_sensitive": False },  # Origin / Ukrainian + Russian / level11
        { "from": "  ", "to": " ", "case_sensitive": False },
        { "from": " # ", "to": "#", "case_sensitive": False },
        { "from": " :", "to": ": ", "case_sensitive": False },
        { "from": " ,", "to": ",", "case_sensitive": False },
        { "from": " .", "to": ".", "case_sensitive": False },
        { "from": " !", "to": "!", "case_sensitive": False },
        { "from": " ?", "to": "?", "case_sensitive": False },
        { "from": " ’’ ", "to": " ", "case_sensitive": False },
        { "from": "’’", "to": "'", "case_sensitive": False },
        { "from": " ’ ", "to": " ", "case_sensitive": False },
        { "from": " ' ", "to": " ", "case_sensitive": False },
        { "from": "’", "to": "'", "case_sensitive": False },
    ]
}

i_debug = False


def get_current_version(file_ggm):
    current_version_patch = None
    with open(file_ggm, 'rb') as f:
        f.seek(0)
        b = f.read()
        # Search for first '0.0NN' version pattern
        for version in ascii_strings_version(b):
            current_version_patch = version.s
    if current_version_patch is None:
        printc(f" No '0.0NN' version patch found in '{file_ggm}' binary file.\n", bcolors.FAIL)
        inputc(f" Press Enter to exit...\n", bcolors.ASK)
        sys.exit(-1)
    return current_version_patch


def ascii_strings_version(buf):
    reg = DEFAULT_ZONA_VERSION_REGEX
    ascii_re = re.compile(reg)
    for match in ascii_re.finditer(buf):
        ascii_string = match.group().decode("ascii")
        ascii_length = len(ascii_string)
        ascii_address = match.start()
        printc(f" {DEFAULT_ZONA_GAME_NAME}:{DEFAULT_ZONA_DIR_NAME}:{DEFAULT_ZONA_DATA_DIR_NAME}:{DEFAULT_ZONA_GLOBAL_GM}:0x{ascii_address:x} (v{ascii_string}) \n", bcolors.NOTIF)
        yield String(ascii_string, ascii_address, 0, ascii_length)
        # Only the first one
        break


def get_config(var):
    if os_path.exists(DEFAULT_ZONA_TRANSLATE_CFG_FILE):
        printc(f" • [Get '{var}' from '{DEFAULT_ZONA_TRANSLATE_CFG_FILE}'] ...\n", bcolors.INFO)
        with open(DEFAULT_ZONA_TRANSLATE_CFG_FILE, 'r') as f:
            for line in f:
                # Use the regex to find 'i_lang' and capture its value
                match = re.match(r'%s=(\w+)' % var, line)
                if match:
                    value = match.group(1)
                    printc(f" • [Get '{var}={value}' from '{DEFAULT_ZONA_TRANSLATE_CFG_FILE}'] OK\n", bcolors.OK)
                    return value
        printc(f" • [Get '{var}' from '{DEFAULT_ZONA_TRANSLATE_CFG_FILE}'] Not found\n", bcolors.WARN)
    return None


def set_config(var, value):

    printc(f" • [Set '{var}' with '{value}' in '{DEFAULT_ZONA_TRANSLATE_CFG_FILE}'] ...\n", bcolors.INFO)
    line_found = False

    if not os_path.exists(DEFAULT_ZONA_TRANSLATE_DIR_NAME):
        os_makedirs(DEFAULT_ZONA_TRANSLATE_DIR_NAME)

    if os_path.exists(DEFAULT_ZONA_TRANSLATE_CFG_FILE):
        # Reading and modifying lines
        with open(DEFAULT_ZONA_TRANSLATE_CFG_FILE, 'r') as file:
            lines = file.readlines()

        # Browse lines to find and modify i_directory
        with open(DEFAULT_ZONA_TRANSLATE_CFG_FILE, 'w') as file:
            for line in lines:
                # Modify the line
                if line.startswith(f"{var}="):
                    line = f"{var}={value}\n"
                    printc(f" • [Set '{var}={value}' in '{DEFAULT_ZONA_TRANSLATE_CFG_FILE}'] OK\n", bcolors.OK)
                    line_found = True
                file.write(line)

            if not line_found:
                line = f"{var}={value}\n"
                file.write(line)
                printc(f" • [Set '{var}={value}' in '{DEFAULT_ZONA_TRANSLATE_CFG_FILE}'] OK\n", bcolors.OK)
                line_found = True
    else:
        with open(DEFAULT_ZONA_TRANSLATE_CFG_FILE, 'w') as file:
            line = f"{var}={value}\n"
            file.write(line)
            printc(f" • [Set '{var}={value}' in '{DEFAULT_ZONA_TRANSLATE_CFG_FILE}'] OK\n", bcolors.OK)
            line_found = True

    return line_found


def get_secret_input(prompt="Enter your secret: "):
    print(prompt, end='', flush=True)
    input_chars = []    
    while True:
        char = msvcrt_getch()  # Capture keyboard input
        if char in {b'\r', b'\n'}:  # Enter key
            print()
            break
        elif char == b'\x08':  # Backspace key
            if input_chars:
                input_chars.pop()
                sys.stdout.write('\b \b')  # Erase the last `*`
                sys.stdout.flush()
        else:
            input_chars.append(char)
            sys.stdout.write('*')  # Display `*` for each character
            sys.stdout.flush()    
    return b''.join(input_chars).decode()  # Convert list of bytes to string


def validation_original_data_files(file):
    expected_flag_len = len(DEFAULT_ZONA_TRANSLATE_STR_IN_BINARY)
    expected_flag = DEFAULT_ZONA_TRANSLATE_STR_IN_BINARY.encode('utf-8')  # Convertir en bytes
    # Open the file in binary mode
    with open(file, 'rb') as f:
        # Go 'expected_flag_len' bytes before the end of the file
        f.seek(-(expected_flag_len), 2)  # 2 signifie "depuis la fin du fichier"
        # Read last 'expected_flag_len' bytes
        last_bytes = f.read(expected_flag_len)

        # TESTING PURPOSE ONLY
        # print(f"{file}: last_bytes='{last_bytes}'")

    # Check whether the last 'expected_flag_len' bytes correspond to the string
    if last_bytes == expected_flag:
        return False
    return True


def remove_specials(text):
    # return text.replace('"', '')
    # Replace special characters with one whitepace (can generate double whitespace)
    text = re.sub(r'[^a-zA-Z0-9\s\.\'",!?\\/\(\)-:]', ' ', text)
    # Remove double whitespaces
    text = text.replace('  ', ' ')
    return text


def replace_accents(text):
    # text = unicodedata.normalize('NFKD', text)
    # return "".join([c for c in text if not unicodedata.combining(c)])
    return unidecode(text)


def restore_translated_words(text, lang='uk'):
    # # FOR TESTING PURPOSES ONLY
    # text_save = text
    for restore_word in RESTORE_SPECIFIC_WORDS[lang]:
        # # CASE SENSITIVE
        # pattern = re.compile(re.escape(restore_word['from']), re.IGNORECASE)
        # text = pattern.sub(restore_word['to'], text)
        # CASE INSENSITIVE
        if not restore_word['case_sensitive']:
            text = re.sub(re.escape(restore_word['from']), restore_word['to'], text, flags=re.IGNORECASE)
        else:
            text = re.sub(re.escape(restore_word['from']), restore_word['to'], text)
    # # FOR TESTING PURPOSES ONLY
    # print(f"{bcolors.OK}{text_save}{bcolors.ENDC}:{bcolors.FAIL}{text}{bcolors.ENDC}")
    return text


def dialog_filter(dialog, lang='uk'):
    # # BEGIN TEST WITHOUT STOPWORDS
    # # Remove stop words
    # if CUSTOM_TARGET_STOPWORDS.get(lang):
    #     # Split text to a list of words
    #     tokens = word_tokenize(dialog)
    #     # Filter stopwords
    #         dialog_filtered_list = [t for t in tokens if t.lower() not in CUSTOM_TARGET_STOPWORDS[lang]]
    #     # Recreate dialog
    #     dialog = ' '.join(dialog_filtered_list)
    # # END TEST WITHOUT STOPWORDS

    # Restore specific words in translated lang
    dialog = restore_translated_words(dialog, lang=lang)
    # Restore specific words for all langs
    dialog = restore_translated_words(dialog, lang='all')
    return dialog


# Dynamic function for Google translator
def dialog_translate_google(translator, dialog='(OUPS)', lang_from=DEFAULT_ZONA_TRANSLATE_LANG_SRC, lang_to='fr'):
    return translator.translate(dialog, src=lang_from, dest=lang_to, raise_exception=True).text


# Dynamic function for Deepl translator
def dialog_translate_deepl(translator, dialog='(OUPS)', lang_from=DEFAULT_ZONA_TRANSLATE_LANG_SRC,  lang_to='fr'):
    return translator.translate_text(dialog, source_lang=lang_from, target_lang=lang_to).text


def dialog_translate(translator, file='(NO_F)', dialog='(OUPS)', lang_from=DEFAULT_ZONA_TRANSLATE_LANG_SRC, lang_to='fr', delay=1, retries=2):
    # Translate dialog string
    # /!\ This method isn't pretty, but it takes much less time than the 'for attempt in range(retries+1)' loop.
    if dialog is None or dialog == '':
        return '(OUPS)'
    try:
        # dialog_tr = translator.translate(dialog, src=DEFAULT_ZONA_TRANSLATE_LANG_SRC, dest=to).text
        dialog_tr = globals()[DEFAULT_TRANSLATE_FUNCTION](translator, dialog, lang_from, lang_to)
    except AuthorizationException_deepl as e:
        printc(f"Function '{currentframe().f_code.co_name}': Boo! A valid 'auth_key' is required with \"-p auth_key\" parameter. Exception {type(e).__name__}: {e}.", bcolors.FAIL)
        sys.exit(-1)
    except Exception as e:
        try:
            printc(f"Function '{currentframe().f_code.co_name}': Rats! Google Translator attempt 1/3 failed on a translation in '{file}'. new attempt in {delay}s", bcolors.WARN)
            time_sleep(delay)
            # dialog_tr = translator.translate(dialog, src=DEFAULT_ZONA_TRANSLATE_LANG_SRC, dest=to).text
            dialog_tr = globals()[DEFAULT_TRANSLATE_FUNCTION](translator, dialog, lang_to)
        except Exception as e:
            try:
                printc(f"Function '{currentframe().f_code.co_name}': Rats! Google Translator attempt 2/3 failed on a translation in '{file}'. new attempt in {delay}s", bcolors.WARN)
                time_sleep(delay)
                # dialog_tr = translator.translate(dialog, src=DEFAULT_ZONA_TRANSLATE_LANG_SRC, dest=to).text
                dialog_tr = globals()[DEFAULT_TRANSLATE_FUNCTION](translator, dialog, lang_to)
            except Exception as e:
                # Do not generate an exception, just add (OUCH) at the end of the string as a tag
                # raise RuntimeError(f"Function '{currentframe().f_code.co_name}': Rats! Google Translator failed after 3 attemps on a translation in '{file}'. Exception {type(e).__name__}: {e}. Just bad luck :/\n")
                printc(f"Function '{currentframe().f_code.co_name}': Rats! Google Translator failed after 3 attempts on a translation in '{file}'. Exception {type(e).__name__}: {e}. Just bad luck :/", bcolors.FAIL)
                dialog_tr = dialog + ' (OUPS)'

    # # # FOR TESTING PURPOSES ONLY
    # print(f"{file}:{DEFAULT_ZONA_TRANSLATE_LANG_SRC}:{bcolors.INFO}{dialog}{bcolors.ENDC}:{to}:{bcolors.OK}{dialog_tr}{bcolors.ENDC}")
    # inputc("Press enter to continue...\n")

    # /!\ This method is fire but consume too much time because of the 'for attempt in range(retries+1)' loop
    # for attempt in range(retries+1):
    #     try:
    #         dialog_tr = translator.translate(dialog, src=DEFAULT_ZONA_TRANSLATE_LANG_SRC, dest=to).text
    #     except Exception as e:
    #         if attempt < retries:
    #             time_sleep(delay)
    #         elif attempt == retries:
    #             attempt += 1
    #             # dialog_tr = f"{dialog} (Sorry)"
    #             # If all attempts fail, raise an exception
    #             raise RuntimeError(f"Function '{currentframe().f_code.co_name}': Rats! Google Translator failed after 3 attemps on a translation in '{file}'. Exception {type(e).__name__}: {e}. Just bad luck :/\n")

    # Add a whitespace as first character if original 'dialog' has a this first whitespace (deleted by translation)
    if dialog[0] == ' ':
        dialog_tr = ' ' + dialog_tr
    dialog = dialog_tr
    # Replace all accentuation characters
    dialog = replace_accents(dialog)
    # Remove all special characters
    dialog = remove_specials(dialog)
    # Restore specific words in translated lang
    dialog = restore_translated_words(dialog, lang=lang_to)
    # Restore specific words for all langs
    dialog = restore_translated_words(dialog, lang='all')
    return dialog


def get_address_from_binary(file_desc, file, search_hex, label):
    file_desc.seek(0)
    try:
        offset_int = file_desc.read().find(bytes.fromhex(search_hex))
    except Exception as e:
        raise RuntimeError(f"Function '{currentframe().f_code.co_name}': Hell! Error during search address for '{label}' in '{file}' binary file. Exception {type(e).__name__}: {e}.\n")
    return offset_int


def backup_files(version):
    global i_debug
    
    backup_dir = f"{DEFAULT_ZONA_TRANSLATE_DIR}/v{version}/{DEFAULT_ZONA_TRANSLATE_BACKUP_DIR_NAME}"

    if i_debug:
        printc(f" • [Create backup in '{backup_dir}/' directory] ...\n", bcolors.INFO)

    os_makedirs(backup_dir)
    # All 'levelNN' original files
    files_to_copy = [os_path.join(DEFAULT_ZONA_DATA_DIR, f) for f in os_listdir(DEFAULT_ZONA_DATA_DIR) if f.startswith('level') and not f.endswith('.resS')]
    # Unique 'resources.assets' original file
    files_to_copy.append(f"{DEFAULT_ZONA_DATA_DIR}/resources.assets")
    
    # Copy all original files in backup directory
    for file in files_to_copy:
        backup_file = os_path.join(backup_dir, os_path.basename(file))
        # Check file is a real original file
        if validation_original_data_files(file):
            shutil.copy2(file, backup_file)
        else:
            # # Remove backup directory to force recreation at next launch
            # os_rmdir(backup_dir)

            # Rename directory name with date and time appended (Don't remove because directory can contains files)
            current_time = datetime.now().strftime('%Y%m%d-%H%M%S')
            os_rename(backup_dir, f"{backup_dir}_{current_time}")
            raise RuntimeError(f"Function '{currentframe().f_code.co_name}': Humm! '{DEFAULT_ZONA_DATA_DIR}' are not original files\n Use the Steam 'Check integrity of game files' button located in 'Installed files' tab in the {DEFAULT_ZONA_GAME_NAME}'s game properties to restore original data files.\n")

    if i_debug:
        printc(f" • [Create backup in '{backup_dir}/' directory] OK\n", bcolors.OK)


def restore_files(version=None, src=None):
    global i_debug

    # Check 'version' parameter
    if version:
        if src is None:
            src = f"{DEFAULT_ZONA_TRANSLATE_DIR}/v{version}/{DEFAULT_ZONA_TRANSLATE_BACKUP_DIR_NAME}"
    else:
        raise RuntimeError(f"Function '{currentframe().f_code.co_name}': 'version' parameter is required.\n")

    if i_debug:
        printc(f" • [Restore files from '{src}/' directory to '{DEFAULT_ZONA_DATA_DIR}/'] ...\n", bcolors.INFO)

    if not os_path.exists(src):
        tips =''
        if src == DEFAULT_ZONA_TRANSLATE_BACKUP_DIR:
            tips = f" Tip: Use the Steam 'Check integrity of game files' button located in 'Installed files' tab in the {DEFAULT_ZONA_GAME_NAME}'s game properties."
        error_msg = f"Damn! Restore files from '{src}/' directory impossible because directory does not exist. {tips}"
        raise RuntimeError(f"Function '{currentframe().f_code.co_name}': {error_msg}.\n")

    # All backup files
    files_to_copy = [os_path.join(src, f) for f in os_listdir(src)]
    files_count = len(files_to_copy)
    if not files_count:
        raise RuntimeError(f"Function '{currentframe().f_code.co_name}': Damn! There is {files_count} file to restore from '{src}/' directory.\n")
    # Copy all backup files in data directory
    for file in files_to_copy:
        data_file = os_path.join(DEFAULT_ZONA_DATA_DIR, os_path.basename(file))
        shutil.copy2(file, data_file)

    if i_debug:
        printc(f" • [Restore {files_count} files from '{src}/' directory to '{DEFAULT_ZONA_DATA_DIR}/'] OK\n", bcolors.OK)


def check_all_in_langs(text):
    if 'all' in text:
        text = ALL_SUPPORTED_LANGS
    return text


def translate_ended_message(src_language):
    print(f" To play with this translation:")
    print(f"    1. Just launch '{DEFAULT_ZONA_GAME_NAME}' game from Steam as usual.")
    print(f"    2. Be sure to select '{ALL_SUPPORTED_LANGS_DB[src_language]}' language in '{DEFAULT_ZONA_GAME_NAME}' game settings.\n")
    printc(f"                                                                                                         ", bcolors.NOTIF)
    printc(f"    /!\\ Over the next few days:                                                                          ", bcolors.NOTIF)
    printc(f"        If '{DEFAULT_ZONA_GAME_NAME}' no longer launches correctly or if a new update has been made by AGaming+    ", bcolors.NOTIF)
    printc(f"        You will need to run this script again to update the translation.                                ", bcolors.NOTIF)
    printc(f"                                                                                                         ", bcolors.NOTIF)
    print()


def create_restore_shortcut():
    # Get current script name
    script_name = f"{os_path.splitext(os_path.basename(__file__))[0]}.exe"
    # Get current working directory
    current_dir = os_getcwd()
    # Define the executable path and shortcut properties
    exe_path = f"{current_dir}\\{script_name}"
    exe_args = '-r'
    shortcut_name = DEFAULT_ZONA_TRANSLATE_RESTORE_SHORTCUT
    shortcut_target = exe_path
    # Create a WScript.Shell object
    shell = w32_dispatch('WScript.Shell')
    # Create a shortcut object
    shortcut = shell.CreateShortCut(shortcut_name)
    # Set the shortcut properties
    shortcut.TargetPath = shortcut_target
    shortcut.WorkingDirectory = os_path.dirname(shortcut_target)
    shortcut.Arguments = exe_args
    # Save the shortcut
    shortcut.save()
    return shortcut_name


def printc(msg, c=None):
    if not c:
        print(msg)
    else:
        print(f"{c}{msg}{bcolors.ENDC}")


def inputc(prompt, c=None):
    if not c:
        res = input(prompt)
    else:
        res = input(f"{c}{prompt}{bcolors.ENDC}")
    return res


# Fonction pour extraire les sequences cyrilliques
def extract_cyrillic_sequences(buf, min_size=2, start_from=0):
    cyrillic_reg = rb'(%s{%d,})' % (CYRILLIC_PATTERN, min_size)
    cyrillic_pattern_min = rb'((?:' + CYRILLIC_BYTES[DEFAULT_ZONA_TRANSLATE_LANG_SRC] + rb'){2,})'  # Regex pour trouver au moins 2 caractères cyrilliques
    for match in re.finditer(cyrillic_reg, buf):  # Chercher toutes les occurrences
        cyrillic_binary = match.group(0)  # Retourner les bytes cyrilliques trouvés
        if re.search(cyrillic_pattern_min, cyrillic_binary):
            cyrillic_string = cyrillic_binary.decode('utf-8', errors='ignore')
            yield String(
                cyrillic_string,  # Cyrillic string found (string)
                start_from + match.start(),  # Cyrillic string found offset (int)
                len(cyrillic_binary),  # Cyrillic binary found length (int)
                len(cyrillic_string)  # Cyrillic string found length (int)
            )


def main():
    # Set CYRILLIC_PATTERN as global variable
    global CYRILLIC_PATTERN
    # Set default global variables
    global DEFAULT_ZONA_EXE_FILENAME
    global DEFAULT_ZONA_GAME_NAME
    global DEFAULT_ZONA_DIR_NAME
    global DEFAULT_ZONA_DIR_EXAMPLE
    global DEFAULT_ZONA_DATA_DIR_NAME
    global DEFAULT_ZONA_DATA_DIR
    global DEFAULT_ZONA_GLOBAL_GM
    global DEFAULT_ZONA_VERSION_REGEX
    global DEFAULT_ZONA_TRANSLATE_LANG_SRC
    global DEFAULT_TRANSLATE_FUNCTION
    global i_debug

    # Main code with global exception management
    try:
        # Allow to fail in 'exception/finally' directives with -1 when error occurs
        Failure = False

        # Check current working directory is valid
        DEFAULT_ZONA_EXE_FILENAME = None
        for game_exec in DEFAULT_ZONA_FILENAME_LIST:
            if os_path.exists(game_exec):
                if game_exec == 'ZONAORIGIN.exe':
                    DEFAULT_ZONA_EXE_FILENAME = game_exec
                    DEFAULT_ZONA_GAME_NAME = 'Z.O.N.A Origin'
                    DEFAULT_ZONA_DIR_NAME = 'ZONAORIGIN'
                    DEFAULT_ZONA_DIR_EXAMPLE = f"C:\\SteamLibrary\\steamapps\\common\\{DEFAULT_ZONA_DIR_NAME}"
                    DEFAULT_ZONA_DATA_DIR_NAME = 'ZONAORIGIN_Data'
                    DEFAULT_ZONA_DATA_DIR = f"./{DEFAULT_ZONA_DATA_DIR_NAME}"
                    DEFAULT_ZONA_GLOBAL_GM = 'globalgamemanagers'
                    DEFAULT_ZONA_GLOBAL_GM_DIR = f"{DEFAULT_ZONA_DATA_DIR}/{DEFAULT_ZONA_GLOBAL_GM}"
                    DEFAULT_ZONA_VERSION_REGEX = rb'(0\.0[0-9][0-9])'
                    DEFAULT_ZONA_TRANSLATE_LANG_SRC = 'uk'
                elif game_exec == 'ZONA.exe':
                    DEFAULT_ZONA_EXE_FILENAME = game_exec
                    DEFAULT_ZONA_GLOBAL_GM_DIR = f"{DEFAULT_ZONA_DATA_DIR}/{DEFAULT_ZONA_GLOBAL_GM}"

        if not DEFAULT_ZONA_EXE_FILENAME:
            raise RuntimeError(f"Function '{currentframe().f_code.co_name}': Heck! The script is not where it should be. Move this script in one of the same directory as the {'\' or \''.join(DEFAULT_ZONA_FILENAME_LIST)}' executable files (Example: usually in the '{DEFAULT_ZONA_DIR_EXAMPLE}' directory). Then run this moved script again ;)\n")

        # Get game current version
        current_version_patch = get_current_version(DEFAULT_ZONA_GLOBAL_GM_DIR)

        # Replace '@PLACEHOLDER_VERSION_DIR' with current game version
        DEFAULT_ZONA_TRANSLATE_BACKUP_DIR = f"{DEFAULT_ZONA_TRANSLATE_DIR}/v{current_version_patch}/{DEFAULT_ZONA_TRANSLATE_BACKUP_DIR_NAME}"

        # Get script arguments
        argparser = argparse.ArgumentParser()
        argparser.add_argument("-t", "--translator", type=str, default='google', choices=['google', 'deepl'], help="Translator to use to translate to. (default value: google)")
        argparser.add_argument("-ta", "--auth-key", type=str, default='', help="Your Translator API authentivation key. (default value: '')")
        argparser.add_argument("-ls", "--lang-src", type=str, default='empty', choices=ALL_SUPPORTED_LANGS_SRC, help="Language to translate from. (default value: 'empty').")
        argparser.add_argument("-l", "--langs", type=str, default='empty', choices=ALL_SUPPORTED_LANGS+['empty', 'all'], help="Languages to translate to. if more than one language then '--langs' parameter must be comma separated (eg. 'fr,cs')")
        argparser.add_argument("-f", "--files", type=str, default='empty', help="Comma separated str. Default is with all 'levelNN' and 'resources.assets' files. if '--file' is specified then '--files' parameter must be comma separated (eg. 'level7,level11')")
        argparser.add_argument("-s", "--min-size", type=int, default=2, help="Minimum size for string to translate is set to 2")
        argparser.add_argument("-v", "--verbose", action='store_true', help="Execute verbose mode (show translation results")
        argparser.add_argument("--sep", type=str, default=';', help="String separator for verbose mode. (default value: ';')")
        argparser.add_argument("-d", "--debug", action='store_true', help="Execute debug mode")
        argparser.add_argument("-df", "--debug-file", action='store_true', help="Print debug in 'auto_ZO_translate_ru.log' file")
        argparser.add_argument("-r", "--restore", action='store_true', help="Restore backup files (reset)")
        argparser.add_argument("-rv", "--restore-version", type=str, default=None, help="Specify the '0.0NN' patch version to restore. Default will be the current version. (reset)")
        argparser.add_argument("--force", action='store_true', help=f"Force translate even if translated files are already existing in '{DEFAULT_ZONA_TRANSLATE_DIR}/' directory")
        argparser.add_argument("--delay", type=int, default=1, help="Delay in secondes between each attempt after an error with Google Translator (default value is 1)")
        argparser.add_argument("--retries", type=int, default=2, help="Number of attempts after an error with Google Translator (default value: 2). Parameter disabled.")
        
        args = argparser.parse_args()

        i_translator = args.translator
        i_auth_key = args.auth_key
        i_langs = args.langs.lower().split(',')
        i_lang_src = args.lang_src.lower()
        i_force = args.force
        i_files = args.files.split(',')
        i_min_size = args.min_size
        i_verbose = args.verbose
        i_sep = args.sep
        i_debug = args.debug
        i_debug_file = args.debug_file
        i_restore = args.restore
        i_restore_version = args.restore_version
        i_delay = args.delay
        i_retries = args.retries

        if i_debug_file:
            i_debug = True

        if i_debug:
            print(f" DEFAULT_ZONA_GAME_NAME={bcolors.OK}'{DEFAULT_ZONA_GAME_NAME}'{bcolors.ENDC}")
            print(f" DEFAULT_ZONA_DIR_NAME={bcolors.OK}'{DEFAULT_ZONA_DIR_NAME}'{bcolors.ENDC}")
            print(f" DEFAULT_ZONA_DIR_EXAMPLE={bcolors.OK}'{DEFAULT_ZONA_DIR_EXAMPLE}'{bcolors.ENDC}")
            print(f" DEFAULT_ZONA_DATA_DIR_NAME={bcolors.OK}'{DEFAULT_ZONA_DATA_DIR_NAME}'{bcolors.ENDC}")
            print(f" DEFAULT_ZONA_DATA_DIR={bcolors.OK}'{DEFAULT_ZONA_DATA_DIR}'{bcolors.ENDC}")
            print(f" DEFAULT_ZONA_GLOBAL_GM={bcolors.OK}'{DEFAULT_ZONA_GLOBAL_GM}'{bcolors.ENDC}")
            print(f" DEFAULT_ZONA_VERSION_REGEX={bcolors.OK}'{DEFAULT_ZONA_VERSION_REGEX}'{bcolors.ENDC}")
            print(f" DEFAULT_ZONA_TRANSLATE_LANG_SRC={bcolors.OK}'{DEFAULT_ZONA_TRANSLATE_LANG_SRC}'{bcolors.ENDC}\n")

        # RESTORE: Create backup file in backup directory if not already existing
        if i_restore:
            print(f" /// RESTORATION:\n")
            if i_restore_version:
                restore_version = i_restore_version
            else:
                restore_version = current_version_patch
            restore_dir = f"{DEFAULT_ZONA_TRANSLATE_DIR}/v{restore_version}/{DEFAULT_ZONA_TRANSLATE_BACKUP_DIR_NAME}"
            if os_path.exists(restore_dir):
                restore = ''
                while restore not in ['y', 'n']:
                    restore = str(inputc(f" Confirm you want to restore all '{restore_version}' backup binary files (y/n): ", bcolors.ASK)).lower().strip()
                if restore == 'y':
                    printc(f" • [Restore original files] ...\n", bcolors.INFO)
                    restore_files(version=restore_version)
                    printc(f" • [Restore original files] OK\n", bcolors.OK)
            else:
                printc(f" • [Restore all binary files impossible because there is no backup for '{restore_version}' version] Failed\n", bcolors.FAIL)
                printc(f" Tip: Use the Steam 'Check integrity of game files' button located in 'Installed files' tab in the {DEFAULT_ZONA_GAME_NAME}'s game properties to restore original binary files.\n", bcolors.INFO)
                inputc(f" Press Enter to exit...\n", bcolors.ASK)
                sys.exit(-1)

        # TRANSLATE
        else:
            print(" /// PREREQUISITES:\n")
            printc(f"    • Your '{DEFAULT_ZONA_GAME_NAME}' game must be up to date.", bcolors.INFO)
            printc("    • Your PC must have an Internet connection for Google Translator or Deepl API requests.", bcolors.INFO)
            printc("    • You must have a valid API auth key if you use Deepl API requests with the \"-t 'deepl'\" and \"-ta 'xxx'\" parameters.\n", bcolors.INFO)
            # printc(f" If needed you can update now your '{DEFAULT_ZONA_GAME_NAME}' game before begin translation.", bcolors.ASK)
            # inputc(f" Then press Enter to translate your '{DEFAULT_ZONA_GAME_NAME}' game...\n", bcolors.ASK)

            # Create the restore shortcut in the current directory if not existing
            if not os_path.exists(DEFAULT_ZONA_TRANSLATE_RESTORE_SHORTCUT):
                printc(f" • [Create a restore shortcut in the current directory] ...\n", bcolors.INFO)
                shortcut = create_restore_shortcut()
                printc(f" • [Create '{shortcut}' restore shortcut in the current directory] OK\n", bcolors.OK)

            # Create default translate dir path (for SQLite DB file)
            if not os_path.exists(DEFAULT_ZONA_TRANSLATE_DIR):
                os_makedirs(DEFAULT_ZONA_TRANSLATE_DIR)

            # BEGIN GUI execution
            if i_translator in DEFAULT_ZONA_TRANSLATE_WITH_AUTHENT:
                if not i_auth_key or i_auth_key is None:
                    while not len(i_auth_key):
                        # i_auth_key = str(inputc(f"API authentication key for '{i_translator}': ", bcolors.ASK)).strip()
                        i_auth_key = get_secret_input(f"API authentication key for '{i_translator}': ").strip()
                        # # BEGIN FOR TESTING PURPOSES ONLY
                        print(f"i_auth_key: '{i_auth_key}'")
                        input("Press enter to continue...\n")
                        # sys.exit(0)
                        # # END FOR TESTING PURPOSES ONLY
            if i_lang_src not in ['empty']:
                set_config('i_lang_src', i_lang_src)
            if i_lang_src == 'empty':
                # Get source language from config file
                i_lang = get_config('i_lang_src')
                if not i_lang:
                    printc(f" • [Get 'i_lang_src' from '{DEFAULT_ZONA_TRANSLATE_CFG_FILE}'] Not found\n", bcolors.WARN)
                    i_lang = ''
                    printc(ALL_SUPPORTED_SOURCE_LANGS_DESCRIPTION, bcolors.INFO)
                    while i_lang not in ALL_SUPPORTED_SOURCE_LANGS:
                        i_lang = str(inputc(f" Language to translate from (specify the 2-letter language code): ", bcolors.ASK)).lower().strip()
                    print()
            # GUI execution requiert only one unique 'i_lang' in 'i_langs' destination list
            # Write new preferred lang in config file (only if langs is not ['all'] or ['empty'])
            if i_langs not in [['all'], ['empty']]:
                set_config('i_lang', i_langs[0])
            if i_langs == ['empty']:
                # Get translated language from config file
                i_lang = get_config('i_lang')
                if not i_lang:
                    printc(f" • [Get 'i_lang' from '{DEFAULT_ZONA_TRANSLATE_CFG_FILE}'] Not found\n", bcolors.WARN)
                    i_lang = ''
                    printc(ALL_SUPPORTED_LANGS_DESCRIPTION, bcolors.INFO)
                    while i_lang not in ALL_SUPPORTED_LANGS:
                        i_lang = str(inputc(f" Language to translate to (specify the 2-letter language code): ", bcolors.ASK)).lower().strip()
                    print()
                i_langs = [i_lang]
                set_config('i_lang', i_langs[0])
                i_langs = check_all_in_langs(i_langs)

            # Replace ['all'] with all supported langs
            i_langs = check_all_in_langs(i_langs)
            # END GUI execution

            # Regular expression for Cyrillic characters (Russian + Specific + Ukrainian pattern) and Latin punctuation
            # CYRILLIC_PATTERN = rb'(\xD0[\x90-\xBF]|\xD1[\x80-\x8F]|\x0a|\x20|\x21|\x22|\x27|\x28|\x29|\x2B|\x2C|\x2D|\x2E|\x2F|\x5C|\x5F)'
            # CYRILLIC_PATTERN = rb'(\xE2\x80\x94|\xD0[\x81\x86-\xBF]|\xD1[\x80-\x8F]|\xD2[\x90-\x91]|\xD2[\x84\x94]|\xD1\x96|\xD0[\x90-\xAF]|\x0a|\x20|\x21|\x22|\x27|\x28|\x29|\x2B|\x2C|\x2D|\x2E|\x2F|\x3A|\x3F\x5C|\x5F)'  # Regular expression for Cyrillic characters + CRLF + Latin punctuation
            # CYRILLIC_PATTERN = rb'(\x56\x52\x3F\x20|\xE2\x80\x94|'+ CYRILLIC_BYTES + rb'|\x0a|\x20|\x21|\x22|\x27|\x28|\x29|\x2B|\x2C|\x2D|\x2E|\x2F|\x3A|\x3F|\x5C|\x5F)'  # Regular expression for Cyrillic characters + CRLF + Latin punctuation
            # CYRILLIC_PATTERN = rb'(' + SPECIFIC_CYRILLIC_BYTES_VR + rb'|' + CYRILLIC_BYTES[DEFAULT_ZONA_TRANSLATE_LANG_SRC] + rb'|' + LATIN_PUNCTUATION_BYTES + rb')'  # Regular expression for Cyrillic characters + CRLF + Latin punctuation
            CYRILLIC_PATTERN = rb'(' + SPECIFIC_CYRILLIC_BYTES_VR + rb'|' + CYRILLIC_BYTES[i_lang_src] + rb'|' + LATIN_PUNCTUATION_BYTES + rb')'  # Regular expression for Cyrillic characters + CRLF + Latin punctuation

            # Save 'i_min_size' for 'resources.assets'
            i_min_size_saved = i_min_size

            # Default 'i_files'
            if i_files == ['empty']:
                i_files = [f for f in os_listdir(DEFAULT_ZONA_DATA_DIR) if f.startswith('level') and not f.endswith('.resS')]
                i_files.append('resources.assets')

            print()
            print(f" /// PARAMETERS:\n")
            
            printc(f"    • Translator ........................ : '{i_translator}'", bcolors.INFO)
            if i_auth_key:
                printc(f"    • Translator authentication key...... : '********'", bcolors.INFO)
            printc(f"    • Translate from .................... : '{i_lang_src}'", bcolors.INFO)
            printc(f"    • Translate to ...................... : {i_langs}", bcolors.INFO)
            printc(f"    • Minimum size string to translate .. : {i_min_size}", bcolors.INFO)
            printc(f"    • Verbose mode ...................... : {i_verbose}", bcolors.INFO)
            printc(f"    • Debug/dry mode .................... : {i_debug}", bcolors.INFO)
            printc(f"    • Force mode ........................ : {i_force}", bcolors.INFO)
            if i_debug:
                printc(f"    • Debug/dry in file ................. : {i_debug_file}", bcolors.INFO)
            printc(f"    • Binary files to translate ......... : {i_files}\n", bcolors.INFO)
            
            # Download nltk 'stopwords' and 'punkt_tab'
            # nltk_download('stopwords')
            # Download nltk 'punkt' and 'punkt_tab'
            # nltk_download('punkt')
            # nltk_download('punkt_tab')
            # stops = set(stopwords.words('german'))
            # stops = set(stopwords.words('french'))
            # stops = set(stopwords.words('czech'))
            # print(stops)
            # inputc(f" Press Enter to continue...", bcolors.ASK)
            # sys.exit(0)

            # Create or get existing DB for translation
            db = DBManager(db_name=f"{DEFAULT_ZONA_TRANSLATE_DB_DIR}/{DEFAULT_ZONA_TRANSLATE_DB_NAME[DEFAULT_ZONA_DIR_NAME.lower()]}")
            # Add source lang to DB
            src_lang_id = db.add_lang(i_lang_src, ALL_SUPPORTED_LANGS_DB[i_lang_src], i_verbose)
            
            print(f" /// TRANSLATION:\n")
            try:
                if i_translator == 'deepl':
                    # Initialize Deepl Translator
                    translator = deepl_Translator(i_auth_key)
                    print(str(translator))
                    DEFAULT_TRANSLATE_FUNCTION = "dialog_translate_deepl"
                # elif i_translator == 'new Futur Translator':
                #     # Initialize new Futur Translator here
                #     
                #     
                else:
                    # Initialize default Google Translator
                    translator = googletrans_Translator()
                    DEFAULT_TRANSLATE_FUNCTION = "dialog_translate_google"
            except:
                raise RuntimeError(f"Function '{currentframe().f_code.co_name}': Argh! '{i_translator} Translator error. Exception {type(e).__name__}: {e}.\n")

            # Create backup file in backup directory if not already existing
            backup_dir = f"{DEFAULT_ZONA_TRANSLATE_DIR}/v{current_version_patch}/{DEFAULT_ZONA_TRANSLATE_BACKUP_DIR_NAME}"
            printc(f" • [Backup in '{backup_dir}/' directory] ...\n", bcolors.INFO)
            backup_need = True
            if os_path.exists(backup_dir):
                # Is 'backup_dir' a directory ?
                if os_path.isdir(backup_dir):
                    # Is there files in 'backup_dir' directory ?
                    if os_listdir(backup_dir):
                        printc(f" • [Backup in '{backup_dir}/' directory] OK (already exists)\n", bcolors.OK)
                        backup_need = False
                    else:
                        # Remove empty 'backup_dir' directory
                        os_rmdir(backup_dir)
                else:
                    # Remove empty 'backup_dir' file
                    os_remove(backup_dir)
            if backup_need:
                backup_files(current_version_patch)
                printc(f" • [Backup in '{backup_dir}/' directory] OK\n", bcolors.OK)
            
            # TESTING PURPOSE ONLY
            # input('test')

            # Initialiaze variable for lang for progression
            i_langs_count = len(i_langs)
            i_langs_index = 0
            
            for i_lang in i_langs:

                # Increment lang index for progression
                i_langs_index = i_langs_index + 1

                # Add translated lang to DB
                target_lang_id = db.add_lang(i_lang, ALL_SUPPORTED_LANGS_DB[i_lang], i_verbose)
                
                # Check already existing and create relative translate dir for lang file destination
                TRANSLATE_DIR_PATH = f"{DEFAULT_ZONA_TRANSLATE_DIR}/v{current_version_patch}/{i_lang_src.lower()}_to_{i_lang.lower()}"
                # Initialiaze success file flag path
                TRANSLATE_SUCCEED_FILE = f"{TRANSLATE_DIR_PATH}/{DEFAULT_ZONA_TRANSLATE_SUCCEED_FILE}"
                # Translate dir for lang file destination does not exist
                if not os_path.exists(TRANSLATE_DIR_PATH):
                    os_makedirs(TRANSLATE_DIR_PATH)
                # Translate dir does exist
                else:
                    if i_debug:printc(f" • [Translated files for '{i_lang}' and '{current_version_patch}' version already exists in '{TRANSLATE_DIR_PATH}/' directory] OK\n", bcolors.OK)
                    # Check success file flag exists in translate lang directory
                    if os_path.exists(TRANSLATE_SUCCEED_FILE):
                        if i_debug: printc(f" • [Translated directory contains a valid '{TRANSLATE_SUCCEED_FILE}' succeed flag file] OK\n", bcolors.OK)
                        # Translate dir for lang file destination does exists ('--force' parameter is not requested)
                        if not i_force:
                            if i_debug: printc(f" • [Force translate IS NOT requested]\n", bcolors.ASK)
                            # Copy existing translate dir for lang file
                            printc(f" • [Restore translated files from '{TRANSLATE_DIR_PATH}/' to '{DEFAULT_ZONA_DATA_DIR}/'] ...\n", bcolors.INFO)
                            restore_files(version=current_version_patch, src=TRANSLATE_DIR_PATH)
                            printc(f" • [Restore translated files from '{TRANSLATE_DIR_PATH}/' to '{DEFAULT_ZONA_DATA_DIR}/'] OK\n", bcolors.OK)
                            # translate_ended_message(i_lang_src)
                            # inputc(f" Press Enter to exit...\n", bcolors.ASK)
                            # sys.exit(0)
                            continue
                        # Translate dir for lang file destination does exists ('--force' parameter is requested)
                        else:
                            if i_debug:
                                printc(f" • [Translated files for '{i_lang}' and '{current_version_patch}' version already exists in '{TRANSLATE_DIR_PATH}/' directory] OK\n", bcolors.OK)
                                printc(f" • [Translated directory does contain a valid '{TRANSLATE_SUCCEED_FILE}' succeed flag file] OK\n", bcolors.OK)
                                printc(f" • [Force translate IS requested] OK\n", bcolors.OK)
                                printc(f" • [Remove valid '{TRANSLATE_SUCCEED_FILE}' succeed flag file] ...\n", bcolors.INFO)
                            os_remove(TRANSLATE_SUCCEED_FILE)
                            if i_debug: printc(f" • [Remove valid '{TRANSLATE_SUCCEED_FILE}' succeed flag file] OK\n", bcolors.OK)
                    else:
                        if i_debug: 
                            printc(f" • [Translated directory does not contain a valid '{TRANSLATE_SUCCEED_FILE}' succeed flag file] OK\n", bcolors.OK)
                            printc(f" • [Force translate will be performed]\n", bcolors.ASK)

                # # Do not restore when the backup has just been performed (only for the first loop)
                # if not backup_files_done:
                #     # Restore original backup files in data dir before translate
                #     printc(f" • [Restore original backup files from '{DEFAULT_ZONA_TRANSLATE_BACKUP_DIR}/' to '{DEFAULT_ZONA_DATA_DIR}/'] ...\n", bcolors.INFO)
                #     restore_files(version=current_version_patch)
                #     printc(f" • [Restore original backup files from '{DEFAULT_ZONA_TRANSLATE_BACKUP_DIR}/' to '{DEFAULT_ZONA_DATA_DIR}/'] OK\n", bcolors.OK)
                #     # Allow restore BACKUP directory after each translate for each lang
                #     backup_files_done = False

                # Always restore original backup files in data dir before translate
                printc(f" • [Restore original backup files from '{DEFAULT_ZONA_TRANSLATE_BACKUP_DIR}/' to '{DEFAULT_ZONA_DATA_DIR}/'] ...\n", bcolors.INFO)
                restore_files(version=current_version_patch)
                printc(f" • [Restore original backup files from '{DEFAULT_ZONA_TRANSLATE_BACKUP_DIR}/' to '{DEFAULT_ZONA_DATA_DIR}/'] OK\n", bcolors.OK)

                # BEGIN Translate to i_lang
                printc(f" • [Translate {len(i_files)} files from '{i_lang_src}' to '{i_lang}' ({i_langs_index}/{i_langs_count} lang)] ...\n", bcolors.INFO)

                if i_debug:
                    if i_debug_file:
                        printc(f" • [Debug mode in file: log writed in './{DEFAULT_ZONA_TRANSLATE_DEBUG_FILE}'] ...\n", bcolors.INFO)
                    else:
                        printc(f" • [Debug mode in terminal] ...\n", bcolors.INFO)

                # Open debug file with overwrite existing content mode
                with open(DEFAULT_ZONA_TRANSLATE_DEBUG_FILE, 'w', encoding="utf-8") as debug_f:

                    for i_file in tqdm(i_files):
                    
                        i_file_translated = f"{TRANSLATE_DIR_PATH}/{i_file}"
                        i_file = f"{DEFAULT_ZONA_DATA_DIR}/{i_file}"
                    
                        # print(f" • [Translate from '{i_lang_src}' to '{i_lang}'] {i_file} ...\n")

                        # Translate only existing 'i_file'
                        if not os_path.exists(i_file):
                            printc(f" Warning: '{i_file}' is skipped because not found.", bcolors.WARN)
                            continue
                        
                        with open(i_file, 'rb') as f:
                            if i_file == 'resources.assets':
                                # 'i_min_size' for 'resources.assets' cannot be too big. Some quests (as 'Explore ' one ) are truncated with non-ascii characters.
                                if i_min_size > 6:
                                    i_min_size = 6
                                # Only 'resources.assets' file
                                start_from_hex_0 = "41 46 55 20 5F 4F 54 53 54 55 50 4E 49 4B"  # AFU _OTSTUPNIK
                                start_from_int_0 = get_address_from_binary(f, i_file, start_from_hex_0, 'AFU _OTSTUPNIK')
                                # end_from_hex_0 = "53 68 6F 6F 74 69 6E 67 20 73 66 78"  # Shooting sfx
                                # end_from_int_0 = get_address_from_binary(f, i_file, end_from_hex_0, 'Shooting sfx')
                                allowed_ranges = [
                                    {
                                        "begin_int": start_from_int_0,  # 131796768/0x07db0f20
                                        # "end_int": end_from_int_0  # 131811120/0x07db4730   # Not used anymore
                                        "end_int": -1
                                    },
                                    # {
                                    #     "begin_int":  start_from_int_1,  # 131424672/0x07d561a0
                                    #     "end_int": end_from_int_1  # 132384996/0x07e408e4
                                    # }
                                ]
                            else:
                                i_min_size = i_min_size_saved
                                # All 'levelNN' files
                                start_from_hex_0 = "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 80 3F"  # ....Ç?..Ç?..Ç?..Ç?
                                start_from_int_0 = get_address_from_binary(f, i_file, start_from_hex_0, '....Ç?..Ç?..Ç?..Ç?')
                                allowed_ranges = [
                                    {
                                        "begin_int": start_from_int_0,  # 0
                                        "end_int": -1  # To the EOF
                                    }
                                ]
                        
                        # If start address for searching in file is a valid address (not negative one)
                        if start_from_int_0 >= 0:

                            with open(i_file, 'rb') as f:
                                # Get all binary file's bytes into a byte array for future writes.
                                f.seek(0)
                                bytearray_to_translate = bytearray(f.read())
                                # Go to first byte to translate
                                f.seek(start_from_int_0)
                                bytes_to_translate = f.read()
                                
                                # cyrillic_sequences = check_cyrillic_sequences(bytes_to_translate, min_size=i_min_size, start_from=start_from_int_0)
                                # for s in tqdm(cyrillic_sequences):
                                for s in extract_cyrillic_sequences(bytes_to_translate, min_size=i_min_size, start_from=start_from_int_0):
                                    
                                    break_requested = False
                                    # Check if we are in allowed range
                                    for range in allowed_ranges:
                                        if range['begin_int'] < 0:
                                            break_requested = True
                                        # Break if string address not in allowed range
                                        if range['begin_int'] >= 0 and s.offset < range['begin_int']:
                                            break_requested = True
                                        if range['end_int'] >= 0 and s.offset > range['end_int']:
                                            break_requested = True
                                    if break_requested:
                                        break

                                    binary_max_length = s.binary_length

                                    # Get translate from DB
                                    # dialog_str = db.get_translate_target_from_src(s.s, src_lang_id, target_lang_id, i_verbose)
                                    dialog_str = db.get_translation_to_text_by_from_text(s.s, src_lang_id, target_lang_id, i_verbose)
                                    
                                    if dialog_str:
                                        dialog_len = len(dialog_str)
                                        dialog_type = 'DB'
                                    # Translate does not exist
                                    else:
                                        dialog_type = 'ONLINE'
                                        dialog_str = dialog_translate(translator=translator,
                                                                      file=i_file,
                                                                      dialog=s.s,
                                                                      lang_from=i_lang_src,
                                                                      lang_to=i_lang,
                                                                      delay=i_delay,
                                                                      retries=i_retries)

                                        # Format translate before adding in DB
                                        dialog_len = len(dialog_str)
                                        # Remove stopword if necessary
                                        if dialog_len > binary_max_length:
                                            dialog_str = dialog_filter(dialog=dialog_str, lang=i_lang)
                                        # Crop dialog if necessary
                                        dialog_str = dialog_str[:binary_max_length]
                                        # Fill dialog with whitespaces to match source length
                                        dialog_str = dialog_str.ljust(binary_max_length)

                                        # Add new translate in DB
                                        # db.add_translate(src_lang_id, s.s, target_lang_id, dialog_str, i_verbose)
                                        db.add_translation(src_lang_id, s.s, target_lang_id, dialog_str, i_verbose)
                                    
                                    # # DEBUG PRINT
                                    if i_debug:
                                        if i_debug_file:
                                            debug_str = " {:s}{:1s}CYR{:1s}0x{:x}{:1s}{:s}{:1s}{:d}{:1s}{:d}{:1s}{:s}{:1s}{:s}\n".format(i_file, i_sep, i_sep, s.offset, i_sep, dialog_type, i_sep, binary_max_length, i_sep, dialog_len, i_sep, s.s, i_sep, dialog_str)
                                            debug_f.write(debug_str)
                                    if i_verbose:
                                        debug_str = " {:s}{:1s}CYR{:1s}{:s}0x{:x}{:s}{:1s}{:s}{:s}{:s}{:1s}{:d}{:1s}{:d}{:1s}{:s}{:s}{:s}{:1s}{:s}{:s}{:s}".format(i_file, i_sep, i_sep, bcolors.FAIL, s.offset, bcolors.ENDC, i_sep, bcolors.WARN, dialog_type, bcolors.ENDC, i_sep, binary_max_length, i_sep, dialog_len, i_sep, bcolors.INFO, s.s, bcolors.ENDC, i_sep, bcolors.OK, dialog_str, bcolors.ENDC)
                                        print(debug_str)

                                    # Set new binary string with translated dialog
                                    binary_string = b''
                                    for ascii_char in dialog_str:
                                        binary_string += bytes([ord(ascii_char)])
                                    # Set translated dialog in bytes array
                                    bytearray_to_translate[s.offset:s.offset+binary_max_length] = binary_string

                            if i_debug:
                                printc(f" • [Debug mode without writing translation in binary file] OK\n", bcolors.OK)
                            else:
                                # Copy original file in relative translate dir
                                shutil.copyfile(i_file, i_file_translated)

                                # Translate file in relative translate dir
                                with open(i_file_translated, 'rb+') as f:
                                    # Write flag for translated file at the very end of the data file
                                    bytearray_to_translate.extend(DEFAULT_ZONA_TRANSLATE_STR_IN_BINARY.encode('utf-8'))
                                    # Write translated dialog in bytes array into translated file
                                    f.write(bytearray_to_translate)

                            # # printc(f" • [Translate from '{i_lang_src}' to '{i_lang}'] {i_file} OK\n", bcolors.OK)

                    if i_debug:
                        if i_debug_file:
                            printc(f" • [Debug mode in file: log writed in './{DEFAULT_ZONA_TRANSLATE_DEBUG_FILE}'] OK\n", bcolors.OK)
                        else:
                            printc(f" • [Debug mode in terminal] OK\n", bcolors.OK)
                        # inputc(f" Press Enter to exit...", bcolors.ASK)
                        # sys.exit(0)

                # Create success file flag in translate lang directory
                with open(TRANSLATE_SUCCEED_FILE, "w") as f:
                    pass
                # END Translate to i_lang

                # All is OK!
                printc(f"\n • [Translate {len(i_files)} files from '{i_lang_src}' to '{i_lang}' ({i_langs_index}/{i_langs_count} lang)] OK\n", bcolors.OK)

                if i_debug:
                    printc(f" • [Debug mode without overwriting '{DEFAULT_ZONA_DATA_DIR}/' game binary file] OK\n", bcolors.OK)
                else:
                    # Copy translated files to default data dir
                    restore_files(version=current_version_patch, src=TRANSLATE_DIR_PATH)

            # Close SQLite DB
            db.close()
            # Show ended message
            translate_ended_message(i_lang_src)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os_path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        printc(f" Error: {e}\n {exc_type}\n {fname}\n {exc_tb.tb_lineno}", bcolors.FAIL)
        Failure = True

    finally:
        inputc(f" Press Enter to exit...", bcolors.ASK)
        if Failure:
            sys.exit(-1)

if __name__ == '__main__':
    main()
