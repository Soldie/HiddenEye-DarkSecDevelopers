#SocialFish checks functions

from urllib.request import urlopen
from os import path, system
from subprocess import check_output
from platform import system as systemos, architecture
from wget import download

RED, GREEN, DEFAULT = '\033[91m', '\033[1;32m', '\033[0m'

def checkConnection(host='http://duckduckgo.com'): #Connection check
    try:
        urlopen(host)
        print("{0}Successful connection!{1}".format(GREEN, DEFAULT))
        return True
    except:
        return False
    if checkConnection() == False:
        print ('''
  ....._____.......     ____ ____ ____ _ ____ _       ____ _ ____ _  _
      /     \/|         [__  |  | |    | |__| |       |___ | [__  |__|
      \o__  /\|         ___] |__| |___ | |  | |___    |    | ___] |  |
          \|
                    {0}[{1}!{0}]{1} Network error. Verify your connection.\n
'''.format(RED, DEFAULT))
    exit(0)

def checkNgrok(): #Ngrok check
    if path.isfile('Server/ngrok') == False:  #Is Ngrok downloaded?
        print('[*] Downloading Ngrok...')
        if 'Android' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm -Rf ' + filename)
        system('clear')
