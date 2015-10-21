#! /usr/bin/python
import gtk
import os
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
class SystrayIconApp:
	def __init__(self):
		self.tray = gtk.StatusIcon()
		self.tray.set_from_file('/usr/share/pixmaps/redshift.svg')
		self.tray.connect('popup-menu', self.on_right_click)
		self.tray.set_tooltip(('Redshift Runner Tray Controls'))
	def on_right_click(self, icon, event_button, event_time):
		self.make_menu(event_button, event_time)
	def make_menu(self, event_button, event_time):
		# create menu
		menu = gtk.Menu()
		# add enable item
		enable = gtk.MenuItem("Enable")
		enable.show()
		menu.append(enable)
		enable.connect('activate',self.enable)
		# add disable item
		disable = gtk.MenuItem("Disable")
		disable.show()
		menu.append(disable)
		disable.connect('activate',self.disable)
		# add quit item
		quit = gtk.MenuItem("Quit")
		quit.show()
		menu.append(quit)
		quit.connect('activate', gtk.main_quit)
		# show popup menu
		menu.popup(None, None, gtk.status_icon_position_menu,event_button, event_time, self.tray)
	def disable(self,widget):
		closeRunner()
	def enable(self,widget):
		openRunner()
if __name__ == "__main__":
	# launch the daemon on launch of trayIcon
	openRunner()
	# create trayIcon
	SystrayIconApp()
	gtk.main()
	# kill redshift runner on tray exit
	closeRunner()
