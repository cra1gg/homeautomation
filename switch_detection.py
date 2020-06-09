import pywemo
import time
import os
import subprocess

while True:
    address = "192.168.1.177"
    port = pywemo.ouimeaux_device.probe_wemo(address)
    url = 'http://%s:%i/setup.xml' % (address, port)
    device = pywemo.discovery.device_from_description(url, None)
    if device.get_state() == 1:
        print("Turning monitor on")
        cmdCommand = "nircmd.exe monitor on"   #specify your cmd command
        process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)
   
    else:
        print("Turning monitor off")
        cmdCommand = "nircmd.exe monitor off"   #specify your cmd command
        process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)
    print(device.get_state())
    