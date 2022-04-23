# !usr/bin/env python3

import os
import webbrowser
from platform import system
from time import sleep

from core import HackingToolsCollection
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_generator import PayloadCreatorTools
from tools.phising_attack import PhisingAttackTools


logo = """\033[33m
                              _
                            _-' "'-,
                         _-' | d$$b |
                      _-'    | $$$$ |
                   _-'       | Y$$P |
                _-'|         |      |
             _-'  _*         |      |
          _-' |_-"      __--''\\    /
       _-'         __--'     __*--'
     -'       __-''    __--*__-"`
    |    _--''   __--*"__-'`
    |_--"  .--=`"__-||"
    |      |  |\\   ||
    | .dUU |  | \\ //
    | UUUU | _|___//
    | UUUU |  |
    | UUUU |  |
    | UUUU |  |
    | UUUU |  |
    | UUUU |  |
    | UUP' |  |
    |   ___^-"`
     ""'
     AIOCLF
\033[97m"""


all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    DDOSTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    PhisingAttackTools(),
    ExploitFrameworkTools(),
    OtherTools(),
]


class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        print(logo + "\033[0m \033[97m")


if __name__ == "__main__":
    try:
        if system() == "Linux":
            fpath = "home/AIOCLFpath.txt"
            if not os.path.exists(fpath):
                os.system("clear")
                print(
                    f"""
                    AIOCLF

                    [@] set path (all your tools will be installed in that directory)
                    [1] manual
                    [2] default
                """
                )
                choice = input("choice ->> ")

                if choice == "1":
                    inpath = input("enter path (with directory name ) >> ")
                    with open(fpath, "w") as f:
                        f.write(inpath)
                    print(f"succesfully set path to {inpath}")
                elif choice == "2":
                    autopath = "/home/AIOCLF/"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print(f"your default path is {autopath}")
                    sleep(3)
                else:
                    print("try again ..")
                    exit(0)

            with open(fpath) as f:
                archive = f.readline()
                if not os.path.exists(archive):
                    os.mkdir(archive)
                os.chdir(archive)
                all_tools = AllTools()
                all_tools.show_options()

        elif system() == "Windows":
            print(
                "\033[91m please run this tool on a debian system for best result "
                "\\e[00m"
            )
            sleep(2)
            webbrowser.open_new_tab("https://www.debian.org/")
        else:
            print("please check your system")

    except KeyboardInterrupt:
        print("\nExitting...")
        sleep(2)
