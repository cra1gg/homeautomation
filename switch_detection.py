import pywemo
import time
import os
import subprocess
from pyvesync import VeSync

manager = VeSync("cfdt123@gmail.com", "Marlenne123")
manager.login()
manager.update()

my_switch = manager.outlets[0]

address = "192.168.1.177"
port = pywemo.ouimeaux_device.probe_wemo(address)
url = 'http://%s:%i/setup.xml' % (address, port)

on = True
device = pywemo.discovery.device_from_description(url, None)
if device.get_state() == 1:
    my_switch.turn_on()
    cmdCommand = "nircmd.exe monitor on"   #specify your cmd command
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
    on = True
    cmdCommand = "adb\\adb.exe shell service call power 12"   #specify your cmd command
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output.decode("utf-8") )
    if output == "Result: Parcel(00000000 00000000   '........')\r\n":
                cmdCommand = "adb\\adb.exe shell input keyevent 26"   #specify your cmd command
                process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
    
else:
    on = False
    my_switch.turn_off()
    print("Turning monitor off")
    cmdCommand = "nircmd.exe monitor off"   #specify your cmd command
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    cmdCommand = "adb\\adb.exe shell service call power 12"   #specify your cmd command
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output.decode("utf-8") )
    if output == "Result: Parcel(00000000 00000001   '........')\r\n":
                cmdCommand = "adb\\adb.exe shell input keyevent 26"   #specify your cmd command
                process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()

while True:
    device = pywemo.discovery.device_from_description(url, None)
    if device.get_state() == 1:
        if not on:
            on = True
            my_switch.turn_on()
            print("Turning monitor on")
            cmdCommand = "nircmd.exe monitor on"   #specify your cmd command
            process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            cmdCommand = "adb\\adb.exe shell service call power 12"   #specify your cmd command
            process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            print(output.decode("utf-8"))
            if output == "Result: Parcel(00000000 00000001   '........')\r\n":
                cmdCommand = "adb\\adb.exe shell input keyevent 26"   #specify your cmd command
                process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()

   
    else:
        if on:
            on = False
            my_switch.turn_off()
            print("Turning monitor off")
            cmdCommand = "nircmd.exe monitor off"   #specify your cmd command
            process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            cmdCommand = "adb\\adb.exe shell service call power 12"   #specify your cmd command
            process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            print(output.decode("utf-8"))
            if output == "Result: Parcel(00000000 00000000   '........')\r\n":
                cmdCommand = "adb\\adb.exe shell input keyevent 26"   #specify your cmd command
                process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()
    print(device.get_state())
    