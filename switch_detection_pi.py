import pywemo
import time
import os
import subprocess
import magichue


light = magichue.Light('192.168.1.12')  # change address
address = "192.168.1.177"
port = pywemo.ouimeaux_device.probe_wemo(address)
url = 'http://%s:%i/setup.xml' % (address, port)
on = True
device = pywemo.discovery.device_from_description(url, None)  

while True:
    try:
        device = pywemo.discovery.device_from_description(url, None)
        if device.get_state() == 1:
            if not on:
                os.system("/opt/vc/bin/tvservice -p")
                time.sleep(1)
                os.system("xset s reset")
                os.system("sudo uhubctl -p 2 -a 1")
                on = True
                if not light.on:
                    light.on = True
        else:
            if on:
                on = False
                os.system("/opt/vc/bin/tvservice -o")
                os.system("sudo uhubctl -p 2 -a 0 -r 10")
                if light.on:
                    light.on = False
        print(device.get_state())
    except:
        pass
