import time
import subprocess
import os
import sys
import webbrowser
from modes import *




typingPrint("Hello Friend\n\n")
typingPrint('''[1] one domain
[2] list of subdomains
[3] notify config
[4] subfinder config\n''')
pick = input(">> ")


def one(domain,notify):
    clear()
    typingPrint("now we using subfinder\n")
    print(subprocess.run("subfinder -d "+ domain +" -o subs.txt",shell=True))
    clear()
    typingPrint("now we using amass\n")
    print(subprocess.run("amass enum -passive -d "+domain+" -o amss_subs.txt",shell=True))
    clear()
    typingPrint("now we using assetfinder\n")
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
    clear()
    typingPrint("now we using dirb\n")
    print(subprocess.run("dirb http://"+domain+" -o dirb.txt",shell=True))
    clear()
    typingPrint("now we using dirsearch")
    print(subprocess.run("dirsearch -e php,html,js,jsp,bak,zip,tgz,txt -u "+domain+" -t 10 -o dirsearch.txt",shell=True))
    clear()
    typingPrint("now we using gobuster")
    print(subprocess.run("gobuster dir -u "+domain+" --no-error -r -o gobuster.txt",shell=True))
    clear()
    typingPrint("now we using ffuf")
    print(subprocess.run("ffuf -u https://"+domain+"/FUZZ -w /usr/share/Seclists/Discovery/Web-content/raft-medium-files.txt -mc 200,302,301 -t 1000"))
    clear()
    typingPrint("now we finished part 2, let's keep working")
    typingPrint("starting part 3 'Parameter fuzzing and gathering'")
    clear()
    typingPrint("now we using arjun")
    print(subprocess.run("arjun -i file -oT arjun.txt"))
    clear()
    typingPrint("now we using gospider")
    print(subprocess.run("gospider -S file -a -w -o gospider.txt"))
    clear()
    typingPrint("we finished part 3 :)")
    typingPrint("i am glad you still here")
    typingPrint("let's keep going and finish last part")
    clear()


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
elif pick == "3" or pick == 3:
    print(subprocess.run("cd ~ && sudo nano .config/notify/provider-config.yaml",shell=True))
elif pick == "4" or pick == 4:
    print(subprocess.run("cd ~ && sudo nano .config/subfinder/provider-config.yaml",shell=True))
else:
    print("\nwrong answer")