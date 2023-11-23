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
    print(subprocess.run("mkdir outputs",shell=True))
    if notify == "y":
        typingPrint("\nthat's nice :)")
        time.sleep(1)
        clear()
        subprocess.run("echo 'now we using subfinder' | notify -silent",shell=True)
        print(subprocess.run("subfinder -d "+ domain +" -o outputs/finder_subs.txt | notify -bulk -silent",shell=True))
        clear()
        subprocess.run("echo 'now we using assetfinder' | notify -silent",shell=True)
        print(subprocess.run("assetfinder -subs-only "+domain+" > outputs/asset_subs.txt",shell=True))
        print(subprocess.run("notify -bulk -silent -data outputs/asset_subs.txt",shell=True))
        clear()
        typingPrint("opening browser, watch the results\n")
        webbrowser.open_new_tab('https://securitytrails.com/domain/'+domain+'/dns')
        webbrowser.open_new_tab('https://securitytrails.com/list/apex_domain/'+domain)
        typingPrint("now we finished subdomains finding. :)\n")
        typingPrint("let's start sort them in one file\n")
        print(subprocess.run("cat outputs/finder_subs.txt outputs/asset_subs.txt | sort -u >> outputs/uniq_subs.txt",shell=True))
        print(subprocess.run("cat outputs/uniq_subs.txt | httpx -mc 200,301,302,403 -o outputs/httpx.txt",shell=True))
        subprocess.run("echo 'results of httpx' | notify -bulk -silent",shell=True)
        subprocess.run("notify -bulk -silent -data outputs/httpx.txt",shell=True)
        clear()
        typingPrint("now we checked on open subs by httpx check the file called outputs/httpx.txt\n")
        typingPrint("so we will go to part to now 'Directory and file Enumeration'")
        time.sleep(2)
        clear()
        file_path = 'outputs/uniq_subs.txt'
        file_path_probe = 'outputs/httpx.txt'
        subprocess.run("echo 'now we using dirsearch' | notify -silent",shell=True)
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                subprocess.run("echo 'scanning subdomain: "+line+"' | notify -silent",shell=True)
                print(subprocess.run("dirsearch -e php,html,js,jsp,bak,zip,tgz,txt -u "+line+" -t 25 -x 404 -q | notify -bulk -silent",shell=True), end='')
        clear()
        subprocess.run("echo 'now we using gobuster' | notify -silent",shell=True)
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                subprocess.run("echo 'scanning subdomain: "+line+"' | notify -silent",shell=True)
                print(subprocess.run("gobuster dir -u "+line+" -w /usr/share/seclists/Discovery/Web-Content/common.txt --no-error -r -t 20 -o outputs/gobuster.txt",shell=True), end='')
        subprocess.run("notify -bulk -silent -data outputs/gobuster.txt",shell=True)
        clear()
        subprocess.run("echo 'now we using ffuf' | notify -silent",shell=True)
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                subprocess.run("echo 'scanning subdomain: "+line+"' | notify -silent",shell=True)
                print(subprocess.run("ffuf -u "+line+"/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt -mc 200,302,301 -c -t 20 -o outputs/ffuf.txt",shell=True), end='')
                clear()
        subprocess.run("notify -bulk -silent -data outputs/ffuf.txt",shell=True)
        clear()
        typingPrint("now we finished part 2, let's keep working\n")
        typingPrint("starting part 3 'Parameter fuzzing and gathering'")
        time.sleep(2)
        print(subprocess.run("cat outputs/dirsearch.txt outputs/gobuster.txt outputs/ffuf.txt >> outputs/dir.txt",shell=True))
        subprocess.run("echo 'we now finished the part 2 and heading to part 3 :) ' | notify -silent",shell=True)
        clear()
        typingPrint("now we using arjun")
        subprocess.run("echo 'now we using arjun' | notify -silent",shell=True)
        print(subprocess.run("arjun -i outputs/httpx.txt -oT outputs/arjun.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/arjun.txt",shell=True)
        clear()
        typingPrint("now we using gospider")
        subprocess.run("echo 'now we using gospider' | notify -silent",shell=True)
        print(subprocess.run("gospider -S outputs/httpx.txt -a -w -o outputs/gospider",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/gospider/*",shell=True)
        clear()
        typingPrint("we finished part 3 :)\n")
        typingPrint("i am glad you still here\n")
        typingPrint("let's keep going and finish last part")
        time.sleep(2)
        subprocess.run("echo 'we now finished the part 3 and heading to last part' | notify -silent",shell=True)
        clear()
        subprocess.run("echo 'now we using waybackurls' | notify -silent",shell=True)
        print(subprocess.run("cat outputs/httpx.txt | waybackurls >> outputs/waybackurls.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/waybackurls.txt",shell=True)
        clear()
        subprocess.run("echo 'now we using gau' | notify -silent",shell=True)
        print(subprocess.run("cat outputs/httpx.txt | gau >> outputs/gau.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/gau.txt",shell=True)
        clear()
        subprocess.run("echo 'now we using katana' | notify -silent",shell=True)
        print(subprocess.run("katana -list outputs/httpx.txt -v -jc -o outputs/katana.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/katana.txt",shell=True)
        clear()
        subprocess.run("echo 'now we using hakrawler' | notify -silent",shell=True)
        print(subprocess.run("cat outputs/httpx.txt | hakrawler >> outputs/hakrawler.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/hakrawler.txt",shell=True)
        clear()
        typingPrint("want to read total report?  (yes/no)")
        ans = input(">> ")
        if ans == "yes" or ans == "y" or ans == "Y" or ans == "Yes":
            report("y")
        elif ans == "no" or ans == "n" or ans == "N" or ans == "No":
            report("n")
        else:
            typingPrint("error in input.\n")
        typingPrint("now we are done :)\n")
        typingPrint("see you later my friend!\n")
        typingPrint("please if you liked my tool don't forget to star it and follow me in github it will support, thanks :)")
    elif notify == "n":
        clear()
        typingPrint("now we using subfinder\n")
        print(subprocess.run("subfinder -d "+ domain +" -o outputs/finder_subs.txt",shell=True))
        clear()
        typingPrint("now we using assetfinder\n")
        print(subprocess.run("assetfinder -subs-only "+domain+" > outputs/asset_subs.txt",shell=True))
        clear()
        typingPrint("opening browser, watch the results\n")
        webbrowser.open_new_tab('https://securitytrails.com/domain/'+domain+'/dns')
        webbrowser.open_new_tab('https://securitytrails.com/list/apex_domain/'+domain)
        typingPrint("now we finished subdomains finding. :)\n")
        typingPrint("let's start sort them in one file\n")
        print(subprocess.run("cat outputs/finder_subs.txt outputs/asset_subs.txt | sort -u >> outputs/uniq_subs.txt",shell=True))
        print(subprocess.run("cat outputs/uniq_subs.txt | httpx -mc 200,301,302,403 -o outputs/httpx",shell=True))
        clear()
        typingPrint("now we checked on open subs by httpx check the file called httpx\n")
        typingPrint("so we will go to part to now 'Directory and file Enumeration'")
        time.sleep(2)
        subprocess.run("touch outputs/dirsearch.txt",shell=True)
        subprocess.run("chmod +w outputs/dirsearch.txt",shell=True)
        clear()
        file_path = 'outputs/uniq_subs.txt'
        file_path_probe = 'outputs/httpx.txt'
        typingPrint("now we using dirsearch")
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                print(subprocess.run("dirsearch -e php,html,js,jsp,bak,zip,tgz,txt -u "+line+" -t 25 -x 404 -q | cat >> outputs/dirsearch.txt",shell=True))
        clear()
        typingPrint("now we using gobuster")
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                print(subprocess.run("gobuster dir -u "+line+" --no-error -r -o outputs/gobuster.txt",shell=True))
        clear()
        typingPrint("now we using ffuf")
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                print(subprocess.run("ffuf -u "+line+"/FUZZ -w /usr/share/Seclists/Discovery/Web-content/raft-medium-files.txt -mc 200,302,301 -c -t 20 -o outputs/ffuf.txt",shell=True))
        clear()
        subprocess.run("notify -bulk -silent -data outputs/ffuf.txt",shell=True)
        clear()
        typingPrint("now we finished part 2, let's keep working")
        typingPrint("starting part 3 'Parameter fuzzing and gathering'")
        time.sleep(2)
        clear()
        typingPrint("now we using arjun")
        print(subprocess.run("arjun -i outputs/httpx.txt -oT outputs/arjun.txt",shell=True))
        clear()
        typingPrint("now we using gospider")
        print(subprocess.run("gospider -S outputs/httpx.txt -a -w -o outputs/gospider.txt",shell=True))
        clear()
        typingPrint("we finished part 3 :)")
        typingPrint("i am glad you still here")
        typingPrint("let's keep going and finish last part")
        time.sleep(2)
        clear()
        typingPrint("now we using waybackuls")
        print(subprocess.run("cat outputs/httpx.txt | waybackurls >> outputs/waybackurls.txt",shell=True))
        clear()
        typingPrint("now we using gau")
        print(subprocess.run("cat outputs/httpx.txt | gau >> outputs/gau.txt",shell=True))
        clear()
        typingPrint("now we using katana")
        print(subprocess.run("katana -list outputs/httpx.txt -v -jc -o outputs/katana",shell=True))
        clear()
        typingPrint("now we using hakrawler")
        print(subprocess.run("cat outputs/httpx.txt | hakrawler >> outputs/hakrawler",shell=True))
        clear()
        typingPrint("want to read total report?  (yes/no)")
        ans = input(">> ")
        if ans == "yes" or ans == "y" or ans == "Y" or ans == "Yes":
            report("y")
        elif ans == "no" or ans == "n" or ans == "N" or ans == "No":
            report("n")
        else:
            typingPrint("error in input.\n")
        typingPrint("now we are done :)\n")
        typingPrint("see you later my friend!\n")
        typingPrint("please if you liked my tool don't forget to star it and follow me in github it will support, thanks :)")



def two(list,notify):
    print(subprocess.run("mkdir outputs",shell=True))
    clear()
    if notify == "y":
        print(subprocess.run("cat "+list+" | httprobe >> outputs/subdomains.txt",shell=True))
        clear()
        typingPrint("we will start now 'Directory and file Enumeration'")
        time.sleep(2)
        clear()
        file_path_probe = 'outputs/subdomains.txt'
        subprocess.run("echo 'now we using dirsearch' | notify -silent",shell=True)
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                subprocess.run("echo 'scanning subdomain: "+line+"' | notify -silent",shell=True)
                print(subprocess.run("dirsearch -e php,html,js,jsp,bak,zip,tgz,txt -u "+line+" -t 25 -x 404 -q | notify -bulk -silent",shell=True))
        clear()
        subprocess.run("echo 'now we using gobuster' | notify -silent",shell=True)
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                subprocess.run("echo 'scanning subdomain: "+line+"' | notify -silent",shell=True)
                print(subprocess.run("gobuster dir -u "+line+" --no-error -r -o outputs/gobuster.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/gobuster.txt",shell=True)
        clear()
        subprocess.run("echo 'now we using ffuf' | notify -silent",shell=True)
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                subprocess.run("echo 'scanning subdomain: "+line+"' | notify -silent",shell=True)
                print(subprocess.run("ffuf -u "+line+"/FUZZ -w /usr/share/Seclists/Discovery/Web-content/raft-medium-files.txt -mc 200,302,301 -c -t 20 -o outputs/ffuf.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/ffuf.txt",shell=True)
        clear()
        typingPrint("now we finished part 2, let's keep working\n")
        typingPrint("starting part 2 'Parameter fuzzing and gathering'\n")
        time.sleep(2)
        clear()
        subprocess.run("echo 'we now finished the part 1 and heading to part 2 :) ' | notify -silent",shell=True)
        clear()
        subprocess.run("echo 'now we using arjun' | notify -silent",shell=True)
        print(subprocess.run("arjun -i outputs/subdomains.txt -oT outputs/arjun.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/arjun.txt",shell=True)
        clear()
        typingPrint("now we using gospider")
        subprocess.run("echo 'now we using gospider' | notify -silent",shell=True)
        print(subprocess.run("gospider -S outputs/subdomains.txt -a -w -o outputs/gospider.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/gospider.txt",shell=True)
        clear()
        typingPrint("we finished part 2 :)\n")
        typingPrint("i am glad you still here\n")
        typingPrint("let's keep going and finish last part\n")
        time.sleep(2)
        clear()
        subprocess.run("echo 'we now finished the part 3 and heading to last part' | notify -silent",shell=True)
        clear()
        subprocess.run("echo 'now we using waybackurls' | notify -silent",shell=True)
        print(subprocess.run("cat outputs/subdomains.txt | waybackurls >> outputs/waybackurls.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/waybackurls.txt",shell=True)
        clear()
        subprocess.run("echo 'now we using gau' | notify -silent",shell=True)
        print(subprocess.run("cat outputs/subdomains.txt | gau >> outputs/gau.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/gau.txt",shell=True)
        clear()
        subprocess.run("echo 'now we using katana' | notify -silent",shell=True)
        print(subprocess.run("katana -list outputs/subdomains.txt -v -jc -o outputs/katana.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/katana.txt",shell=True)
        clear()
        subprocess.run("echo 'now we using hakrawler' | notify -silent",shell=True)
        print(subprocess.run("cat outputs/subdomains.txt | hakrawler >> outputs/hakrawler.txt",shell=True))
        subprocess.run("notify -bulk -silent -data outputs/hakrawler.txt",shell=True)
        clear()
        typingPrint("want to read total report?  (yes/no)")
        ans = input(">> ")
        if ans == "yes" or ans == "y" or ans == "Y" or ans == "Yes":
            report("y")
        elif ans == "no" or ans == "n" or ans == "N" or ans == "No":
            report("n")
        else:
            typingPrint("error in input.\n")
        typingPrint("now we are done :)\n")
        typingPrint("see you later my friend!\n")
        typingPrint("please if you liked my tool don't forget to star it and follow me in github it will support, thanks :)")
    elif notify == "n":
        print(subprocess.run("cat "+list+" | httprobe >> outputs/subdomains.txt",shell=True))
        clear()
        typingPrint("we will start now 'Directory and file Enumeration'")
        time.sleep(2)
        subprocess.run("touch outputs/dirsearch.txt",shell=True)
        subprocess.run("chmod +w outputs/dirsearch.txt",shell=True)
        clear()
        file_path_probe = 'outputs/subdomains.txt'
        typingPrint("now we using dirsearch")
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                print(subprocess.run("dirsearch -e php,html,js,jsp,bak,zip,tgz,txt -u "+line+" -t 25 -x 404 -q | cat >> outputs/dirsearch.txt",shell=True))
        clear()
        typingPrint("now we using gobuster")
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                print(subprocess.run("gobuster dir -u "+line+" --no-error -r -o outputs/gobuster.txt",shell=True))
        clear()
        typingPrint("now we using ffuf")
        with open(file_path_probe,'r') as file:
            for line in file:
                line = line.replace("\n", "")
                print(subprocess.run("ffuf -u "+line+"/FUZZ -w /usr/share/Seclists/Discovery/Web-content/raft-medium-files.txt -mc 200,302,301 -c -t 20 -o outputs/ffuf.txt",shell=True))
        clear()
        typingPrint("now we finished part 1, let's keep working\n")
        typingPrint("starting part 2 'Parameter fuzzing and gathering'\n")
        time.sleep(2)
        clear()
        subprocess.run("echo 'we now finished the part 1 and heading to part 2 :) ' | notify -silent",shell=True)
        clear()
        typingPrint("now we using arjun")
        print(subprocess.run("arjun -i outputs/subdomains.txt -oT outputs/arjun.txt",shell=True))
        clear()
        typingPrint("now we using gospider")
        print(subprocess.run("gospider -S outputs/subdomains.txt -a -w -o outputs/gospider.txt",shell=True))
        clear()
        typingPrint("we finished part 2 :)\n")
        typingPrint("i am glad you still here\n")
        typingPrint("let's keep going and finish last part")
        time.sleep(2)
        clear()
        typingPrint("now we using waybackuls")
        print(subprocess.run("cat outputs/subdomains.txt | waybackurls >> outputs/waybackurls.txt",shell=True))
        clear()
        typingPrint("now we using gau")
        print(subprocess.run("cat outputs/subdomains.txt | gau >> outputs/gau.txt",shell=True))
        clear()
        typingPrint("now we using katana")
        print(subprocess.run("katana -list outputs/subdomains.txt -v -jc -o outputs/katana",shell=True))
        clear()
        typingPrint("now we using hakrawler")
        print(subprocess.run("cat outputs/subdomains.txt | hakrawler >> outputs/hakrawler",shell=True))
        clear()
        typingPrint("want to read total report?  (yes/no)")
        ans = input(">> ")
        if ans == "yes" or ans == "y" or ans == "Y" or ans == "Yes":
            report("y")
        elif ans == "no" or ans == "n" or ans == "N" or ans == "No":
            report("n")
        else:
            typingPrint("error in input.\n")
            typingPrint("now we are done :)\n")
            typingPrint("see you later my friend!\n")
            typingPrint("please if you liked my tool don't forget to star it and follow me in github it will support, thanks :)")
    else:
        typingPrint("error please try again")


if pick == "1" or pick == 1:
    domainpick = input("enter your domain: ")
    if domainpick == "":
        typingPrint("please input domain")
        sys.exit
    else:
        notify = input("are you want to use notify?    (yes/no)\n>> ")
        if notify == "yes" or notify == "y" or notify == "Yes" or notify == "Y":
            one(domainpick,"y")
        elif notify == "no" or notify == "n" or notify == "No" or notify == "N":
            one(domainpick,"n")
        else:
            print("wrong answer try again with yes or no only !")
            sys.exit
elif pick == "2" or pick == 2:
    listpick = input("enter list of subdomains : ")
    if listpick == "":
        typingPrint("please input list of subdomains")
        sys.exit
    else:
        if os.path.exists(listpick):
            notify = input("are you want to use notify?    (yes/no)\n>> ")
            if notify == "yes" or notify == "y" or notify == "Yes" or notify == "Y":
                two(listpick,"y")
            elif notify == "no" or notify == "n" or notify == "No" or notify == "N":
                two(listpick,"n")
            else:
                print("wrong answer try again with yes or no only !")
                sys.exit
        else:
            typingPrint("the file does not exist. :(")
elif pick == "3" or pick == 3:
    print(subprocess.run("cd ~ && sudo nano .config/notify/provider-config.yaml",shell=True))
elif pick == "4" or pick == 4:
    print(subprocess.run("cd ~ && sudo nano .config/subfinder/provider-config.yaml",shell=True))
else:
    print("\nwrong answer")
    sys.exit
