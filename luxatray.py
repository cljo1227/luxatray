import os
import hid
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator


def main():
    indicator = appindicator.Indicator.new("luxatray", "starred-symbolic",
                                           appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu())
    gtk.main()


def menu():
    menu = gtk.Menu()

    cmd_off = gtk.MenuItem('Off')
    cmd_off.connect('activate', lightOff)
    menu.append(cmd_off)
    
    cmd_red = gtk.MenuItem('Red')
    cmd_red.connect('activate', red)
    menu.append(cmd_red)
    
    cmd_green = gtk.MenuItem('Green')
    cmd_green.connect('activate', green)
    menu.append(cmd_green)
    
    cmd_blue = gtk.MenuItem('Blue')
    cmd_blue.connect('activate', blue)
    menu.append(cmd_blue)
    
    cmd_exit = gtk.MenuItem('Exit')
    cmd_exit.connect('activate', quit)
    menu.append(cmd_exit)

    menu.show_all()
    return menu


def lightOff(_):
	off = [0, 0, 0]
	writeToLux(off)
    
def red(_):
	red = [255, 0, 0]
	writeToLux(red)
    
def green(_):
	green = [0, 128, 0]
	writeToLux(green)

def blue(_):
	blue = [0, 0, 255]
	writeToLux(blue)

def quit(_):
    gtk.main_quit()
    
def writeToLux(color):
	device = hid.device()
	device.open(0x04D8, 0xF372)
	device.write([2] + [0x41] + color + [10])
	device.close()

if __name__ == "__main__":
    main()
