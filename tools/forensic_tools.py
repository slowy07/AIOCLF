# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection


class Autopsy(HackingTool):
    TITLE = "Autopsy"
    DESCRIPTION = "Autopsy is a tool for forensic analysis of digital images."
    RUN_COMMANDS = "sudo autopsy"

    def __init__(self):
        super(Autopsy, self).__init__(installable=False)


class Wireshark(HackingTool):
    TITLE = "Wireshark"
    DESCRIPTION = (
        "Wireshark is a network capture and analyzer \n"
        "tool to see what’s happening in your network.\n "
        "And also investigate Network related incident"
    )
    RUN_COMMANDS = ["sudo wireshark"]

    def __init__(self):
        super(Wireshark, self).__init__(installable=False)


class BulkExtractor(HackingTool):
    TITLE = "Bulk extractor"
    DESCRIPTION = "Extract useful information without parsing the file system"
    PROJECT_URL = "https://github.com/simsong/bulk_extractor"

    def __init__(self):
        super(BulkExtractor, self).__init__(
            [
                ("GUI Mode (Downlod required)", self.gui_mode),
                ("CLI Mode", self.cli_mode),
            ],
            installable=False,
            runnable=False,
        )

    def gui_mode(self):
        os.system("sudo git clone https://github.com/simsong/bulk_extractor.git")
        os.system("ls src/ && cd .. && cd java_gui && ./BEViewer")
        print(
            "If you getting error after clone go to /java_gui/src/ And Compile .Jar file && run ./BEViewer"
        )
        print(
            "Please Visit For More Details About Installation >> https://github.com/simsong/bulk_extractor"
        )

    def cli_mode(self):
        os.system("sudo apt-get install bulk_extractor")
        print("bulk extractor and options")
        os.system("bulk_extractor -h")
        os.system(
            'echo "bulk_extractor [options] imagefile | boxes -d headline | lolcat'
        )


class Guymager(HackingTool):
    TITLE = "Disk clone and iso image aquire"
    DESCRIPTION = "Gumager is a free forensic imager for media acquisition"
    INSTALL_COMMANDS = ["sudo apt-get install gumager"]
    RUN_COMMANDS = ["sudo gumager"]
    PROJECT_URL = "https://guymager.sourceforge.io/"


class Toolsley(HackingTool):
    TITLE = "Toolsley"
    DESCRIPTION = (
        "toolsley got more than ten useful tool for investigation.\n"
        "[+]File signature verifier\n"
        "[+]File identifier.\n"
        "[+]Hash & validate.\n"
        "[+]Binary inspector.\n"
        "[+]Encode text.\n"
        "[+]Data URI generator.\n"
        "[+]Password generator"
    )
    PROJECT_URL = "https://www.toolsley.com/"

    def __init__(self):
        super(Toolsley, self).__init__(installable=False, runnable=False)


class ForensicTools(HackingToolsCollection):
    TITLE = "Forensic tools"
    TOOLS = [Autopsy(), Wireshark(), BulkExtractor(), Guymager(), Toolsley()]
