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

class PayloadCreatorTools(HackingToolsCollection):
    TITLE = "Payload Creator Tools"
    TOOLS = [
        TheFatRat(),
    ]