import os
import socket
import subprocess
import webbrowser

from core import HackingTool
from core import HackingToolsCollection
from core import clear_screen


class NMAP(HackingTool):
    TITLE = "Network map (nmap)"
    DESCRIPTION = (
        "Free and open source utility for network discovery and security auditing"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nmap/nmap.git",
        "ssudo chmod -R 755 nmap && cd nmap && ./configure && make && sudo make install",
    ]
    PROJECT_URL = "https://github.com/nmap/nmap"

    def __init__(self):
        super(NMAP, self).__init__(installable=False)


class Dracnmap(HackingTool):
    TITLE = "Dracnmap"
    DESCRIPTION = (
        "Dracnmap is an open source program which is using to \n"
        "exploit the network and gathering information with nmap help."
    )

    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/Dracnmap.git",
        "cd Dracnmap && chmod +x dracnmap-v2.2-dracOs.sh dracnmap-v2.2.sh",
    ]
    RUN_COMMANDS = ["cd Dracnmap;sudo ./dracnmap-v2.2.sh"]
    PROJECT_URL = "https://github.com/Screetsec/Dracnmap"


class PortScan(HackingTool):
    TITLE = "Port Scanning"

    def __init__(self):
        super(PortScan, self).__init__(installable=False)

    def run(self):
        clear_screen()
        target = input("select target IP: ")
        subproces.run(["sudo", "nmap", "-O", "-Pn", target])


class Host2IP(HackingTool):
    TITLE = "Host to IP"

    def __init__(self):
        super(Host2IP, self).__init__(installable=False)

    def run(self):
        clear_screen()
        host = input("enter host name (e.g www.google.com):- ")
        ips = socket.gethostbyname(host)
        print(ips)


class XeroSploit(HackingTool):
    TITLE = "XeroSploit"
    DESCRIPTION = (
        "Xerosploit is a penetration testing toolkit whose goal is to perform\n"
        "man-in-the-middle attacks for testing purposes"
    )
    INSTALL_COMMANDS = [
        "git clone http://github.com/LionSec/xerosplit.git"
        "cd xerosploit && sudo python install.py"
    ]
    RUN_COMMANDS = ["sudo xerosploit"]
    PROJECT_URL = "https://github.com/LionSec/xerosploit"


class RedHawk(HackingTool):
    TITLE = "RED HAWK (All In One Scanning)"
    DESCRIPTION = (
        "All in one tool for Information Gathering and Vulnerability Scanning."
    )
    INSTALL_COMMANDS = ["git clone https://github.com/Tuhinshubhra/RED_HAWK.git"]
    RUN_COMMANDS = ["cd RED_HAWK;php rhawk.php"]
    PROJECT_URL = "https://github.com/Tuhinshubhra/RED_HAWK"


class ReconSpider(HackingTool):
    TITLE = "ReconSpider(For All Scaning)"
    DESCRIPTION = (
        "ReconSpider is most Advanced Open Source Intelligence (OSINT)"
        " Framework for scanning IP Address, Emails, \n"
        "Websites, Organizations and find out information from"
        " different sources.\n"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/bhavsec/reconspider.git",
        "sudo apt install python3 python3-pip && cd reconspider && sudo python3 setup.py install",
    ]
    RUN_COMMANDS = ["cd reconspider;python3 reconspider.py"]
    PROJECT_URL = "https://github.com/bhavsec/reconspider"


class IsItDown(HackingTool):
    TITLE = "Check website down/up"
    DESCRIPTION = "Check website down/up"

    def __init__(self):
        super(IsItDown, self).__init__(
            [("Open", self.open)], installable=False, runnable=False
        )

    def open(self):
        webbrowser.open_new_tab("https://www.isitdownrightnow.com/")


class Infoga(HackingTool):
    TITLE = "Infoga - Email Osint"
    DESCRIPTION = (
        "Infoga is a tool gathering email accounts informations\n"
        "(ip, hostname, country,...) from different public source"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/Infoga.git",
        "cd Infoga;sudo python3 setup.py install",
    ]
    RUN_COMMANDS = ["cd Infoga;python3 infoga.py"]
    PROJECT_URL = "https://github.com/m4ll0k/Infoga"


class ReconDog(HackingTool):
    TITLE = "ReconDog"
    DESCRIPTION = "ReconDog Information Gathering Suite"
    INSTALL_COMMANDS = ["git clone https://github.com/s0md3v/ReconDog.git"]
    RUN_COMMANDS = ["cd ReconDog;sudo python dog"]
    PROJECT_URL = "https://github.com/s0md3v/ReconDog"


class Striker(HackingTool):
    TITLE = "Striker"
    DESCRIPTION = "Recon & Vulnerability Scanning Suite"
    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/Striker.git",
        "cd Striker && pip3 install -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/s0md3v/Striker"

    def run(self):
        site = input("enter site name (example.com) >>")
        os.chdir("Striker")
        subprocess.run(["sudo", "python3", "striker.py", site])


class SecretFinder(HackingTool):
    TITLE = "SecretFinder (like API & etc)"
    DESCRIPTION = (
        "SecretFinder - A python script for find sensitive data \n"
        "like apikeys, accesstoken, authorizations, jwt,..etc \n "
        "and search anything on javascript files.\n\n "
        "Usage: python SecretFinder.py -h"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/SecretFinder.git secretfinder",
        "cd secretfinder; sudo pip3 install -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/m4ll0k/SecretFinder"

    def __init__(self):
        super(SecretFinder, self).__init__(runnable=False)


class Shodan(HackingTool):
    TITLE = "Find Info Using Shodan"
    DESCRIPTION = (
        "Get ports, vulnerabilities, informations, banners,..etc \n "
        "for any IP with Shodan (no apikey! no rate limit!)\n"
        "[X] Don't use this tool because your ip will be blocked by Shodan!"
    )
    INSTALL_COMMANDS = ["git clone https://github.com/m4ll0k/Shodanfy.py.git"]
    PROJECT_URL = "https://github.com/m4ll0k/Shodanfy.py"

    def __init__(self):
        super(Shodan, self).__init__(runnable=False)


class PortScannerRanger(HackingTool):
    TITLE = "Find Info Using Shodan"
    DESCRIPTION = (
        "Get ports, vulnerabilities, informations, banners,..etc \n "
        "for any IP with Shodan (no apikey! no rate limit!)\n"
        "[X] Don't use this tool because your ip will be blocked by Shodan!"
    )
    INSTALL_COMMANDS = ["git clone https://github.com/m4ll0k/Shodanfy.py.git"]
    PROJECT_URL = "https://github.com/m4ll0k/Shodanfy.py"

    def run(self):
        ip = input("enter ip: ")
        os.chdir("rang3r")
        subprocess.run(["sudo", "python", "rang3r.py", "--ip", ip])


class Breacher(HackingTools):
    TITLE = "Breacher"
    DESCRIPTION = "An advanced multithreaded admin panel finder written in python."
    INSTALL_COMMANDS = ["git clone https://github.com/s0md3v/Breacher.git"]
    PROJECT_URL = "https://github.com/s0md3v/Breacher"

    def run(self):
        domain = input("enter domain: ")
        os.chdir("Breacher")
        subprocess.run(["python3", "breacher.py", "-U", domain])


class InformationGatheringTools(HackingToolsCollection):
    TITLE = "Information gathering tools"
    TOOLS = [
        NMAP(),
        Dracnmap(),
        PortScan(),
        Host2IP(),
        XeroSploit(),
        RedHawk(),
        ReconSpider(),
        IsItDown(),
        Infoga(),
        ReconDog(),
        Striker(),
        SecretFinder(),
        Shodan(),
        PortScannerRanger(),
        Breacher(),
    ]
