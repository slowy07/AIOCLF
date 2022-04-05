#!/bin/bash
clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'

echo -e "${CYAN} "
echo "AIOCLF GUN";
echo -e "${BLUE} this tool mut run as root [!] ${NC}";
echo -e ${CYAN} "select option: "
echo ""
echo -e "${WHITE}    [1] kali linux / parrot-os"
echo -e "${WHITE}    [0] exit"
echo -n -e "choice ->> "
read choice

INSTALL_DIR="usr/share/doc/AIOCLF"
BIN_DIR="/usr/bin"
if [ $choice == 1 ]; then 
    echo "[-] checking internet connection ..."
    wget -q --tries=10 --timeout=20 --spider http://google.com
    if [[ $? -eq 0 ]]; then
        echo -e ${BLUE} "[?] loading ..."
        sudo apt-get update && sudo apt-get upgrade
        sudo apt-get install python-pip
        echo "[-] checking directories ..."
        if [ -d "$INSTALL_DIR"]; then
            echo "[!] directory was found, do you want to replace it ? [y/n] "
            read input
            if [ "$input" == "y"]; then
                rm -R "$INSTALL_DIR"
            else
                exit
            fi
        fi
            echo "[!] installing ..."
            echo ""
            git clone https://github.com/slowy07/AIOCLF.git "$INSTALL_DIR";
            echo "#!/bin/bash 
            python3 $INSTALL_DIR/hackingtool.py" '${1+"$@"}' > AIOCLF;
            sudo chmod +x AIOCLF;
            sudo cp AIOCLF /usr/bin/;
            rm AIOCLF;
            echo "";
            echo "[!] installaction requirement ..."
            sudo pip3 install lolcat
            sudo apt-get install -y figlet
            sudo pip3 install boxes
            sudo apt-get install boxes
            sudo apt-get install flask
            sudo pip3 insstall requests
    else
        echo -e $RED "please check your internet connection"
    fi

if [-d "$INSTALL_DIR" ]; then
    echo "";
    echo "[✔] Successfuly Installed !!! ";
    echo "";
    echo "now just type in terminal AIOCLF to run the tool";    
else
    echo "[x] installation failed ";
    exit
fi

elif [ $choice -eq 0 ];
then
    echo -e $RED "[:v] thank you"
    exit
else
    echo -e $RED "[!] invalid choice"
    exit
fi
