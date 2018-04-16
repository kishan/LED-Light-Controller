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

color_time = 5 # seconds on each color


def crossFade(bulb, color1, color2):

	r1,g1,b1 = color1
	r2,g2,b2 = color2
	
	steps = 100
	for i in range(1,steps+1):
		r = r1 - int(i * float(r1 - r2)/steps)
		g = g1 - int(i * float(g1 - g2)/steps)
		b = b1 - int(i * float(b1 - b2)/steps)
		# (use non-persistent mode to help preserve flash)
		new = (r,g,b)
		print "crossFade: " + str(new)
		bulb.setRgb(r,g,b, persist=False)
		time.sleep(0.1)

	



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



# for x in xrange(200):
# 	i = x % 3
# 	color = colorwheel[i]
	
# 	print str(color)
# 	bulb.setRgb(*color)
# 	time.sleep(0.1)

# use cycle() to treat the list in a circular fashion
colorpool = cycle(colorwheel)

# get the first color before the loop
color = next(colorpool)
while True:
	bulb.refreshState()

	# set to color and wait
	# (use non-persistent mode to help preserve flash)
	print color
	# bulb.setRgb(*color)
	# time.sleep(color_time)

	#fade from color to next color			
	next_color = next(colorpool)
	crossFade(bulb, color, next_color)
	
	# ready for next loop
	color = next_color



