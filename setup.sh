 #! /bin/bash
sudo apt update
sudo apt upgrade
sudo apt install subfinder -y
sudo apt install amass -y
sudo apt install gobuster -y
sudo apt install golang -y
sudo apt install assetfinder -y
sudo apt install hakrawler -y
sudo apt install arjun -y
sudo apt install gospider -y
sudo apt install dirb -y
sudo apt install ffuf -y
sudo apt install dirsearch -y
sudo apt install httprobe -y
sudo apt install seclists -y

go install github.com/lc/gau/v2/cmd/gau@latest
sudo mv ~/go/bin/gau /usr/local/bin/

go install github.com/projectdiscovery/notify/cmd/notify@latest
sudo mv ~/go/bin/notify /usr/local/bin/

go install github.com/projectdiscovery/httpx/cmd/httpx@latest
sudo mv ~/go/bin/httpx /usr/local/bin/

cd ~
wget https://github.com/lc/gau/blob/master/.gau.toml

go install github.com/projectdiscovery/katana/cmd/katana@latest
sudo mv ~/go/bin/katana /usr/local/bin/

go install github.com/tomnomnom/waybackurls@latest
sudo mv ~/go/bin/waybackurls /usr/local/bin/