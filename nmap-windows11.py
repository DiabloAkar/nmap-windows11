import subprocess
from pip._vendor.colorama import Fore
import threading
import time
import os
import socket, requests
# Bu kodları değiştiren ahkalsızdır.
# Zamanında bir Atsız varmış var olsun!

subprocess.call('start https://discord.gg/zEaPMEh2aj', shell=True)
subprocess.call('start https://github.com/DiabloAkar', shell=True)
subprocess.call('start https://nmap.org/dist/nmap-7.92-setup.exe', shell=True)

def ResetTool():
    while 1:
        multi()
        os.system("pause")

def multi(): 
    os.system('cls && title Diablo Multi Tool')
    print(f'''

    {Fore.RED}                      ████████▄   ▄█     ▄████████ ▀█████████▄   ▄█        ▄██████▄
    {Fore.RED}                      ███   ▀███ ███    ███    ███   ███    ███ ███       ███    ███
    {Fore.RED}                      ███    ███ ███▌   ███    ███   ███    ███ ███       ███    ███
    {Fore.RED}                      ███    ███ ███▌   ███    ███  ▄███▄▄▄██▀  ███       ███    ███
    {Fore.CYAN}                      ███    ███ ███▌ ▀███████████ ▀▀███▀▀▀██▄  ███       ███    ███
    {Fore.CYAN}                      ███    ███ ███    ███    ███   ███    ██▄ ███       ███    ███
    {Fore.CYAN}                      ███   ▄███ ███    ███    ███   ███    ███ ███▌    ▄ ███    ███
    {Fore.CYAN}                      ████████▀  █▀     ███    █▀  ▄█████████▀  █████▄▄██  ▀██████▀
                                                  
{Fore.LIGHTRED_EX}      Install the downloaded setup file. Close this program after the installation is finished. You can use it again
                             {Fore.WHITE}[+]═════════════════════[+]═══════════════════[+]
	                      {Fore.WHITE}║ {Fore.LIGHTBLUE_EX}[0] - Help            {Fore.WHITE}║{Fore.LIGHTBLUE_EX} [3] - L4ncelot      {Fore.WHITE}║
		              {Fore.WHITE}║ {Fore.LIGHTBLUE_EX}[1] - Diablo          {Fore.WHITE}║{Fore.LIGHTBLUE_EX} [4] - Kronos        {Fore.WHITE}║
		              {Fore.WHITE}║ {Fore.LIGHTBLUE_EX}[2] - Eddley          {Fore.WHITE}║{Fore.LIGHTBLUE_EX} [5] - Yusuf         {Fore.WHITE}║
		             {Fore.WHITE}[+]═════════════════════[+]═══════════════════[+]
                             {Fore.LIGHTRED_EX}           Please press 0 before starting''')


    soru = input(Fore.RED+" ┌─/"+Fore.LIGHTBLUE_EX+"Write Number"+Fore.RED+"""/
    └──╼ """+Fore.LIGHTBLUE_EX+"=> ")

    if soru == '0':
        print(Fore.GREEN+'1 = Finding live hosts in your network. / Ağınızdaki canlı ana bilgisayarları bulma.')
        print(Fore.GREEN+'2 = Listing open ports on a target host. / Bir hedef ana bilgisayardaki açık bağlantı noktalarını listeleme.')
        print(Fore.GREEN+'3 = Fingerprinting OS and services running on a target host. / Hedef ana bilgisayarda çalışan parmak izi işletim sistemi ve hizmetler.')
        print(Fore.GREEN+'4 = To enable OS detection. / İşletim sistemi algılamasını etkinleştirmek için.')
        print(Fore.GREEN+'5 = Using NSE scripts against a target host. / NSE komut dosyalarını bir hedef ana bilgisayara karşı kullanma.')
        print(Fore.RED+'To stop = CTRL + C')

    
    elif soru == "1":
        soru1 = input(Fore.WHITE+'Your Target= ')
        os.system('nmap -sn '+soru1)
    
    elif soru == "2":
        soru2 = input(Fore.WHITE+'Your Target= ')
        os.system('nmap '+soru2)

    elif soru == "3":
        soru3 = input(Fore.WHITE+'Your Target= ')
        os.system('nmap -sV '+soru3)
    elif soru == "4":
        soru4 = input(Fore.WHITE+'Your Target= ')
        os.system('nmap -O '+soru4)
    elif soru == "5":
        soru5 = input(Fore.WHITE+'Your Target= ')
        os.system('nmap -sC '+soru5)
    else:
        multi()


ResetTool()



##Signed By Diablo Akar

##Signed By AkarGuard
