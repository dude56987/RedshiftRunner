#! /usr/bin/python
import gtk
import os
import time
def closeRunner():
	# set display to netural color
	os.system('killall redshiftRunner_daemon')
	os.system('killall redshiftRunner')
	# 6500 is netural
	os.system('redshift -O 6500')
def openRunner():
	#close runner if open, this keeps stacking from occuring on logout and back in
	closeRunner()
	os.system('redshiftRunner_daemon &')
def getBrightness():
	maxNum=6500.0
	minNum=2500.0
	increment=((maxNum-minNum)/(12*60))
	currentTime=time.localtime()
	if currentTime[3]>12:
		# if over 12 convert back to 12 hour format
		hour=currentTime[3]-12
	else:
		# if less than 12 reverse the order
		hour=12-currentTime[3]
	# multuply brightness by total minutes, this changes brightness every minute
	brightness=int((maxNum-(((hour*60)+currentTime[4])*increment)))
	return brightness
class SystrayIconApp:
	def __init__(self):
		# status is the user picked option, values are "auto","dark","light"
		self.status = 'auto'
		self.tray = gtk.StatusIcon()
		self.tray.connect('popup-menu', self.on_right_click)
		self.tray.set_tooltip(('Redshift Runner Tray Controls'))
		# enable redshift on init
		self.enable('activate')
	def on_right_click(self, icon, event_button, event_time):
		self.make_menu(event_button, event_time)
	def make_menu(self, event_button, event_time):
		# create menu
		menu = gtk.Menu()
		# label of brightness
		if self.status == 'auto':
			brightnessLabel = gtk.MenuItem("Brightness: "+str(getBrightness())+'K')
		elif self.status == 'dark':
			brightnessLabel = gtk.MenuItem("Brightness: 2500K")
		elif self.status == 'light':
			brightnessLabel = gtk.MenuItem("Brightness: 6500K")
		brightnessLabel.show()
		menu.append(brightnessLabel)
		# seprator
		sep=gtk.SeparatorMenuItem()
		sep.show()
		menu.append(sep)
		# add enable item
		enable = gtk.MenuItem("Automatic")
		enable.show()
		menu.append(enable)
		enable.connect('activate',self.enable)
		# add disable item
		disable = gtk.MenuItem("Full Brightness")
		disable.show()
		menu.append(disable)
		disable.connect('activate',self.disable)
		# add full darkness item
		fullDarkness = gtk.MenuItem("Full Darkness")
		fullDarkness .show()
		menu.append(fullDarkness)
		fullDarkness.connect('activate',self.fullDark)
		# add quit item
		quit = gtk.MenuItem("Quit")
		quit.show()
		menu.append(quit)
		quit.connect('activate', gtk.main_quit)
		# show popup menu
		menu.popup(None, None, gtk.status_icon_position_menu,event_button, event_time, self.tray)
	def fullDark(self,widget):
		self.status = 'dark'
		self.tray.set_from_file('/usr/share/redshiftRunner/redshift.svg')
		closeRunner()
		os.system('redshift -O 2500')
	def disable(self,widget):
		self.status = 'light'
		self.tray.set_from_file('/usr/share/redshiftRunner/redshift_off.svg')
		closeRunner()
	def enable(self,widget):
		self.status = 'auto'
		self.tray.set_from_file('/usr/share/redshiftRunner/redshift.svg')
		openRunner()
if __name__ == "__main__":
	# create trayIcon
	SystrayIconApp()
	gtk.main()
	# kill redshift runner on tray exit
	closeRunner()
