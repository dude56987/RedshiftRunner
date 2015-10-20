#! /usr/bin/python
from os import system
from time import sleep
import time
import sys
# this runs redshift in oneshot mode based on hours insted of location
maxNum=6500.0
minNum=2500.0
# find total dist, divide by 12 hours multuplied by minutes
increment=((maxNum-minNum)/(12*60))
if '--debug' in sys.argv:
	currentTime=[0,0,0,0,0,0,0]
while True:
	if '--debug' in sys.argv:
		if currentTime[3]>24:
			currentTime[3]=0
		else:
			currentTime[3]+=1
	else:
		currentTime=time.localtime()
	# hour:minute:second
	print(str(currentTime[3])+':'+str(currentTime[4])+':'+str(currentTime[5]))
	# reverse the orders in order to make it a bell curve of brightness
	if currentTime[3]>12:
		# if over 12 convert back to 12 hour format
		hour=currentTime[3]-12
	else:
		# if less than 12 reverse the order
		hour=12-currentTime[3]
	# multuply brightness by total minutes, this changes brightness every minute
	brightness=int((maxNum-(((hour*60)+currentTime[4])*increment)))
	print('redshift -O '+str(brightness))
	system('redshift -O '+str(brightness))
	# pause the system 
	if '--debug' in sys.argv:
		# pause for 1 second in debug
		sleep(1)	
	else:
		# pause for one minute during regular execution
		sleep(60)	
