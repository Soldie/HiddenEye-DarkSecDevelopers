#Primitive config works
import configparser

def createConfig(path = "Settings.ini"):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "Language", "en")

    with open(path, 'w') as configFile:
        config.write(configFile)

def readConfig(path = "Settings.ini"):
    config = configparser.ConfigParser()
    config.read(path)
    return config
