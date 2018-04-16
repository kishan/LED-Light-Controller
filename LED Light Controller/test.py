#!/usr/bin/env python

"""
Example to cycle a bulb between colors in a list, with a smooth fade
between.  Assumes the bulb is already on.

The python file with the Flux LED wrapper classes should live in
the same folder as this script
"""

import os
import sys
import time
from itertools import cycle

this_folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(this_folder)
from flux_led import WifiLedBulb, BulbScanner, LedTimer

scanner = BulbScanner()
scanner.scan(timeout=4)

# Specific ID/MAC of the bulb to set 
bulb_info = scanner.getBulbInfoByID('6001948A4F89')
print "bulb_info: " + str(bulb_info)	

bulb = WifiLedBulb(bulb_info['ipaddr'])

color_time = 2 # seconds on each color

red = (255,0,0)
orange = (255,125,0)
yellow = (255, 255, 0) 
springgreen = (125,255,0) 
green = (0,255,0) 
turquoise = (0,255,125)
cyan = (0, 255, 255) 
ocean = (0,125,255)		
blue = (0,0,255) 
violet = (125, 0, 255) 
magenta = (255, 0, 255) 
raspberry = (255, 0, 125) 
colorwheel = [red, orange, yellow, springgreen, green, turquoise,
			 cyan, ocean, blue, violet, magenta, raspberry]			

colorwheel = [red, green, blue]			

for x in range(100):
	i = x % len(colorwheel)
	color = colorwheel[i]
	print color
	bulb.setRgb(*color, persist=False)
	time.sleep(1) #sleep for one second






