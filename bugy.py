import time
import subprocess
import os
import sys
import webbrowser
from modes import *




typingPrint("Hello Friend\n\n")
typingPrint('''[1] one domain
[2] list of subdomains\n''')
pick = input(">> ")


def one(domain,notify):
    print(subprocess.run("subfinder -d "+ domain +" -o subs.txt",shell=True))
    clear()
    print(subprocess.run("amass enum -passive -d "+domain+" -o amss_subs.txt",shell=True))
    clear()
    print(subprocess.run("assetfinder -subs-only "+domain+" > asset_subs.txt",shell=True))
    clear()
    typingPrint("opening browser, watch the results")
    webbrowser.open_new_tab('https://securitytrails.com/domain/'+domain+'/dns')
    typingPrint("now we finished subdomains finding. :)")
    typingPrint("let's start sort them in one file")
    print(subprocess.run("cat finder_subs.txt amass_subs.txt asset_subs.txt | sort -u >> uniq_subs.txt"))
    print(subprocess.run("cat uniq_subs.txt | httpx -o httpx"))
    clear()
    typingPrint("now we checked on open subs by httpx check the file called httpx")
    typingPrint("so we will go to part to now 'Directory and file Enumeration'")
    print(subprocess.run("dirb "+domain,shell=True))
    clear()
    print(subprocess.run("dirsearch -u "+domain,shell=True))
    clear()
    print(subprocess.run("ffuf -u https://"+domain+"/FUZZ -w /usr/share/Seclists/Discovery/Web-content/raft-medium-files.txt -mc 200,302,301 -t 1000"))
    


def two(list,notify):
    print(subprocess.run("subfinder -l "+ list +" -o subs.txt",shell=True))
    clear()



if pick == "1" or pick == 1:
    domainpick = input("enter your domain: ")
    notify = input("are you want to use notify?    (yes/no)\n>> ")
    if notify == "yes" or notify == "y" or notify == "Yes" or notify == "Y":
        one(domainpick,"yes")
    elif notify == "no" or notify == "n" or notify == "No" or notify == "N":
        one(domainpick,"no")
    else:
        print("wrong answer try again with yes or no only !")
        sys.exit
elif pick == "2" or pick == 2:
    listpick = input("enter list of subdomains : ")
    notify = input("are you want to use notify?    (yes/no)\n>> ")
    if notify == "yes" or notify == "y" or notify == "Yes" or notify == "Y":
        two(listpick,"yes")
    elif notify == "no" or notify == "n" or notify == "No" or notify == "N":
        two(listpick,"no")
    else:
        print("wrong answer try again with yes or no only !")
        sys.exit
else:
    print("\nwrong answer")