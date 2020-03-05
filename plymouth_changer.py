#!/usr/bin/python3
import os
from shutil import copytree
from subprocess import PIPE, run


def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


os.system("figlet plymouth changer")
root = out("whoami")
print("you are", root)
print("run the script where the folder is present!")
try:
    if(str(root).strip() == "root"):
        folder = input("enter name of the folder:")
        print("copying the folder into /usr/share/plymouth/themes/"+str(folder))
        copytree(folder, "/usr/share/plymouth/themes/"+str(folder))
        print("file copied!")
        plymouth_name = input("enter name of the .plymouth name:")
        print("select the plymouth number")
        os.system(
            "sudo update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth /usr/share/plymouth/themes/"+str(folder)+"/"+str(plymouth_name)+".plymouth 100")
        print("changing configuration of default.plmouth.....")
        os.system("sudo update-alternatives --config default.plymouth")
        print("updating boot image......")
        os.system("sudo update-initramfs -u")
        print("plymouth changed successfully!")
        exit(0)
    else:
        print("run script as root!\n")
        print("sudo python3 plymouth_changer.py")
        exit(0)
except:
    print("something went wrong!\n")
    print("possible errors:\n1)folder already exists\n2)are you root?\n3)correct folder or not?\n4)correct .plymouth file or not?")

# 1. copy file to usr/share/plymouth/themes
# 2. run in terminal:
# sudo update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth /usr/share/plymouth/themes/zorin-flat/zorin-flat.plymouth 100
# sudo update-alternatives --config default.plymouth
# sudo update-initramfs -u
