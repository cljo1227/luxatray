#!/usr/bin/env python3
import os
import datetime
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
    cmd_off.connect("activate", off)
    menu.append(cmd_off)

    cmd_red = gtk.MenuItem('Available')
    cmd_red.connect("activate", available)
    menu.append(cmd_red)

    cmd_green = gtk.MenuItem('Busy')
    cmd_green.connect("activate", busy)
    menu.append(cmd_green)

    cmd_blue = gtk.MenuItem('KA')
    cmd_blue.connect("activate", ka)
    menu.append(cmd_blue)

    cmd_helg = gtk.MenuItem('Helg')
    cmd_helg.connect("activate", helg)
    menu.append(cmd_helg)

    cmd_quit = gtk.MenuItem("Exit")
    cmd_quit.connect("activate", quit)
    menu.append(cmd_quit)

    menu.show_all()
    return menu

def off(_):
    os.system("luxe off")

def available(_):
    os.system("luxe available")

def busy(_):
    os.system("luxe busy")

def ka(_):
    os.system("luxe ka")

def helg(_):
    os.system("luxe helg")


def quit(_):
    gtk.main_quit()

if __name__ == "__main__":
    main()
