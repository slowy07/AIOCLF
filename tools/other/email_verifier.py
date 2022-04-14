# coding=utf-8
from core import HackingTool
from core import HackingToolsCollection


class KnockMail(HackingTool):
    TITLE = "KnockMail"
    DESCRIPTION = "tool verifies if email exists"
    INSTALL_COMMANDS = [
        "git clone https://github.com/heywood/KnockMail.git",
        "cd KnockMail;pip3 install -r requirements.txt",
    ]
    RUN_COMMANDS = ["cd KnockMail;python3 knockmail.py"]
    PROJECT_URL = "https://github.com/heywood/KnockMail"


class EmailVerifyTools(HackingToolsCollection):
    TITLE = "email verify tools"
    TOOLS = [KnockMail()]
