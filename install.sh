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
echo -e "${WHITE} [>] Press enter to install hacking tool, ctrl-c to abort. ${NC}";
read INPUT
echo ""

if ["$PREFIX" = "/data/data/com.termux/files/usr"]; then
    INSTALL_DIR="$PREFIX/usr/share/AIOCLF"
    BIN_DIR="$PREFIX/usr/bin"
    pkg install -y git python3
else
    INSTALL_DIR="usr/share/doc/AIOCLF"
    BIN_DIR="usr/bin"
fi

echo "[✔] Checking directories..."
if [ -d "$INSTALL_DIR" ]; then
    echo "[!] A directory AIOCLF already exists.. do you want to replace it ? [y/n]?";
    read replacedir
    if [ "$replacedir" = "y"]; then
        rm -R "$INSTALL_DIR"
    else
        exit
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone https://github.com/slowy07/AIOCLF
echo "#!/bin/bash
python3 $INSTALL_DIR/hackingtool.py" '${1+"$@"}' > AIOCLF;
chmod +x AIOCLF;
sudo cp AIOCLF /usr/bin;
rm AIOCLF;

if [ -d "$INSTALL_DIR" ]; then
    echo "";
    echo "[✔] Successfuly Installed !!! [✔]";
else
    echo "[x] installation failed";
    exit
fi