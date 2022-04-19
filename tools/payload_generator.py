# coding=utf-8

from core import HackingTool
from core import HackingToolsCollection


class TheFatRat(HackingTool):
    TITLE = "The FatRat"
    DESCRIPTION = (
        "TheFatRat Provides An Easy way to create Backdoors and \n"
        "Payload which can bypass most anti-virus"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/TheFatRat.git",
        "cd TheFatRat && sudo chmod +x setup.sh",
    ]
    RUN_COMMANDS = ["cd TheFatRat && sudo bash setup.sh"]
    PROJECT_URL = "https://github.com/Screetsec/TheFatRat"

    def __init__(self):
        super(TheFatRat, self).__init__(
            [("Updaate", self.update), ("Troubleshoot", self.troubleshoot)]
        )

    def update(self):
        os.system("cd TheFatRat && bash update && chmod +x setup.sh && bash setup.sh")

    def troubleshoot(self):
        os.system("cdTheFatRat && sudo chmod +x chk_tools && ./chk_tools")


class Brutal(HackingTool):
    TITLE = "Brutal"
    DESCRIPTION = (
        "Brutal is a toolkit to quickly create various payload,"
        "powershell attack,\nvirus attack and launch listener for "
        "a Human Interface Device"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/Brutal.git",
        "cd Brutal && sudo chmod +x Brutal.sh",
    ]
    RUN_COMMANDS = ["cd Brutal && sudo bash Brutal.sh"]
    PROJECT_URL = "https://github.com/Screetsec/Brutal"

    def show_info(self):
        super(Brutal, self).show_info()
        print(
            """
        [!] requirements
         [x] arduino software (v1.6.7)
         [x] TeensyDuino
         [x] Linux udev rules
         [x] copy and past the paensylib into folder inside your arduino\libraries

        [!] Kindly Visit below link for Installation for Arduino 
            [x]  https://github.com/Screetsec/Brutal/wiki/Install-Requirements
        """
        )


class Stitch(HackingTools):
    TITLE = "Stitch"
    DESCRIPTION = (
        "Stitch is Cross Platform Python Remote Administrator Tool\n\t"
        "[!] Refer Below Link For Wins & MAc Os"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nathanlopez/Stitch.git",
        "cd Stitch && sudo pip install -r lnx_requirements.txt",
    ]
    RUN_COMMANDS = ["cd Stitch && sudo python main.py"]
    PROJECT_URL = "https://nathanlopez.github.io/Stitch"


class MSFVenom(HackinTool):
    TITLE = "MSFvenom Payload Creator"
    DESCRIPTION = (
        "MSFvenom Payload Creator (MSFPC) is a wrapper to generate \n"
        "multiple types of payloads, based on users choice.\n"
        "The idea is to be as simple as possible (only requiring "
        "one input) \nto produce their payload."
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/g0tmi1k/msfpc.git",
        "cd msfpc;sudo chmod +x msfpc.sh",
    ]
    RUN_COMMANDS = ["cd msfpc;sudo bash msfpc.sh -h -v"]
    PROJECT_URL = "https://github.com/g0tmi1k/msfpc"


class Venom(HackingTool):
    TITLE = "Venom Shellcode Generator"
    DESCRIPTION = (
        "venom 1.0.11 (malicious_server) was build to take "
        "advantage of \n apache2 webserver to deliver payloads "
        "(LAN) using a fake webpage writen in html"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/r00t-3xp10it/venom.git",
        "sudo chmod -R 775 venom*/ && cd venom*/ && cd aux && sudo bash setup.sh",
        "sudo ./venom.sh -u",
    ]
    RUN_COMMANDS = ["cd venom && sudo ./venom.sh"]
    PROJECT_URL = "https://github.com/r00t-3xp10it/venom"


class PayloadCreatorTools(HackingToolsCollection):
    TITLE = "Payload Creator Tools"
    TOOLS = [
        TheFatRat(),
        Brutal(),
        Stitch(),
        MSFVenom(),
        Venom(),
    ]
