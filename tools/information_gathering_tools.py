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


class InformationGatheringTools(HackingToolsCollections):
    TITLE = "Information gathering tools"
    TOOLS = [NMAP(), Dracnmap()]
