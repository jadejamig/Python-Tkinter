#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio as gio
from gi.repository import Gtk as gtk
import os

def get_icon_filename(filename,size):
    #final_filename = "default_icon.png"
    final_filename = ""
    if os.path.isfile(filename):
        # Get the icon name
        file = gio.File.new_for_path(filename)
        file_info = file.query_info('standard::icon',0)
        file_icon = file_info.get_icon().get_names()[0]
        # Get the icon file path
        icon_theme = gtk.IconTheme.get_default()
        icon_filename = icon_theme.lookup_icon(file_icon, size, 0)
        if icon_filename != None:
            final_filename = icon_filename.get_filename()

    return final_filename


print(get_icon_filename("/home/newtron/Desktop/counter.desktop",48))