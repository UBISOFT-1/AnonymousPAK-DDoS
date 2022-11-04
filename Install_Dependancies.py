import os
class co:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(co.OKGREEN + '[+] Installing Dependancies for AnonymousPAK DDoS Attack' + co.ENDC)
print(co.OKBLUE + '[+] Download GoLang from Golang.org/dl/'+ co.ENDC)
try:
    os.system('python3 -m pip install wheel')
    os.system('python -m pip install wheel')
    os.system('pip3 install wheel')
    os.system('py -m pip install wheel')
    os.system('python3 -m pip install pyfiglet')
    os.system('pip3 install pyfiglet')
    os.system('py -m pip install pyfiglet')
    os.system('python -m pip install pyfiglet')
    os.system('python3 -m pip install pyttsx3')
    os.system('pip3 install pyttsx3')
    os.system('py -m pip install pyttsx3')
    os.system('python -m pip install pyttsx3')
    os.system('python3 -m pip install colorama')
    os.system('pip3 install colorama')
    os.system('py -m pip install colorama')
    os.system('python -m pip install colorama')
    os.system('sudo apt-get install figlet')
    print(
        '''[+] If this comes and you are on any OS just Ignore only if there is a py command not found as below;
          sh: py: command not found''')
except:
    print(co.BOLD + 'Just Install Pyfiglet, Pyttsx3 and GoLang and Colorama' + co.ENDC)
