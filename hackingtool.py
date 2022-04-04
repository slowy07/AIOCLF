##!usr/bin/env python3

import os
import sys
import argparse
import threading
import webbrowser
import requests
import time
import http.client
import urllib.request
import json
import telnetlib
import glob
import getpass
import socket
import base64
from getpass import getpass
import subprocess
from sys import argv
import random
import queue
import subprocess
import re
import getpass
from os import path
from platform import system
from urllib.parse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep


Logo = """\033[33m
                              _ 
                            _-' "'-,     
                         _-' | d$$b |  
                      _-'    | $$$$ |    
                   _-'       | Y$$P |  
                _-'|         |      |
             _-'  _*         |      |
          _-' |_-"      __--''\    /
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
\033[97m"""


def menu():
    print(
        Logo
        + """\033[0m
    \033[91m[x] this tool must run as a root...[!] \033[97m
    [00]AnonSurf
    [99]Exit
    """
    )

    choice = input("choice =>>")
    if choice == "0" or choice == "00":
        clearScr()
        anonsurf()
    elif choice == "99":
        clearScr(), sys.exit()
        exit()
    elif choice == "":
        menu()


def anonsurf():
    os.system(
        'echo  "It automatically overwrites the RAM when\nthe system is shutting down AnD AlSo cHange Ip" |boxes -d boy | lolcat'
    )
    anc = input("[1]install [2]Run [3]Stop [99]Main Menu >> ")
    if anc == "1":
        os.system("sudo git clone https://github.com/Und3rf10w/kali-anonsurf.git")
        os.system(
            "cd kali-anonsurf && sudo ./install.sh && cd .. && sudo rm -r kali-anonsurf"
        )
        anonsurf()
    elif anc == "2":
        os.system("sudo anonsurf start")
    elif anc == "3":
        os.system("sudo anonsurf stop")
    elif anc == "99":
        anonsurf()
    else:
        menu()


menu()
