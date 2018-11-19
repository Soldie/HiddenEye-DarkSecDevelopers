#Python3
#WILL BE SOON
#WIP

import gettext
from Defs.Configurations import readConfig

def langRussian():
    ru = gettext.translation('hiddeneye',localedir='./locale', languages=['ru'])
    ru.install()

def langUkrainian():
    uk = gettext.translation('hiddeneye',localedir='./locale', languages=['uk'])
    uk.install()

def langEnglish():
    en = gettext.translation('hiddeneye',localedir='./locale', languages=['en'])
    en.install()


def checkAndSetLanguage():
    language = readConfig().get("Settings", "Language")

    if language == "en":
        langEnglish()
    elif language == "ru":
        langRussian()
    elif language == "uk":
        langUkrainian()
    else:
        langEnglish()
