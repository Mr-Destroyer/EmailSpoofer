#Developed By Mohammad Zim
# Email Spoofing Tool
# Amazing Tool for begginers
# Spoof Email !


import os
import sys
import time
from colorama import Fore

def banner():
    print("""
 ______                 _ _  _____                    __
|  ____|   coded by  (_) |  / ____|   Mohammad Zim    / _|
| |__   _ __ ___   __ _ _| | | (___  _ __   ___   ___ | |_ ___ _ __
|  __| | '_ ` _ \ / _` | | |  \___ \| '_ \ / _ \ / _ \|  _/ _ \ '__|
| |____| | | | | | (_| | | |  ____) | |_) | (_) | (_) | ||  __/ |
|______|_| |_| |_|\__,_|_|_| |_____/| .__/ \___/ \___/|_| \___|_|
                                    | |
                                    |_|
    """)

def slow(y):
    for x in y + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.1)

def menu():
    os.system("clear")
    banner()
    time.sleep(2)
    slow(Fore.GREEN + "Coded By Mohammad Zim \n This Tool is made for Email Spoofing and Specially for educational purposes \n Don't Use it For Illegal attention")
    time.sleep(3)
    username = input("Enter username of SMTP server: ")
    password = input("Enter password of SMTP server: ")
    server = input("Enter SMTP server: ")
    port = input("Enter server port: ")
    spoofer = input("Enter The email that you wanna spoof: ")
    victim = input("Enter Victim email: ")
    os.system("clear")
    time.sleep(2)
    subject = input("Enter Subject: ")
    message = input("Enter Message: ")
    os.system(f"sendemail -xu {username} -xp {password} -s {server}:{port} -f {'spoofer'} -t {'target'} -u {'subject'} -m {'message'} ")
    slow("Email Sent Successfully>>>")
menu()
