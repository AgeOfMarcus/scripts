#!/usr/bin/python3

from os import system as run

vmname = input("Enter VM name: ")

run("VBoxManage modifyvm \"%s\" --cpuidset 00000001 000306a9 00020800 80000201 178bfbff" % vmname)
run("VBoxManage setextradata \"%s\" \"VBoxInternal/Devices/efi/0/Config/DmiSystemProduct\" \"iMac11,3\"" % vmname)
run("VBoxManage setextradata \"%s\" \"VBoxInternal/Devices/efi/0/Config/DmiSystemVersion\" \"1.0\"" % vmname)
run("VBoxManage setextradata \"%s\" \"VBoxInternal/Devices/efi/0/Config/DmiBoardProduct\" \"Iloveapple\"" % vmname)
run("VBoxManage setextradata \"%s\" \"VBoxInternal/Devices/smc/0/Config/DeviceKey\" \"ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc\"" % vmname)
run("VBoxManage setextradata \"%s\" \"VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC\" 1" % vmname)
run("VBoxManage setextradata \"%s\" VBoxInternal2/EfiGopMode 4" % vmname)

# All (most) from:
# https://suzywu2014.github.io/ubuntu/2017/02/23/macos-sierra-virtualbox-vm-on-ubuntu
