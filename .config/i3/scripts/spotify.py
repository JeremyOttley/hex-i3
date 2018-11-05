#!/usr/bin/python3

# based on https://github.com/firatakandere/i3blocks-spotify
# to show the spotify song and artist put the following lines in your i3blocks config file:
#[spotify]
#label=
#command=/path/to/this/script
#color=#81b71a
#interval=5

import dbus
import subprocess

DEF_VOLUME = 85  # change this if it's to loud or low
NULL = open(subprocess.os.devnull, 'r')

try:
    bus = dbus.SessionBus()
    spotify_bus = bus.get_object("org.mpris.MediaPlayer2.spotify",
                                 "/org/mpris/MediaPlayer2")
    spotify_properties = dbus.Interface(spotify_bus,
                                        "org.freedesktop.DBus.Properties")
    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player",
                                      "Metadata")
    artist = str(metadata['xesam:artist'][0])
    title = str(metadata['xesam:title'])
    if 'Spotify' in title:
        subprocess.call(["amixer", "-D", "pulse", "sset", "Master", "0%"],
                        stdout=NULL, stderr=NULL)
        NULL.close()
        print('Spotify Add')
        exit
#    subprocess.call(["amixer", "-D", "pulse", "sset", "Master",
#                    str(DEF_VOLUME) + "%"], stdout=NULL, stderr=NULL)
    NULL.close()
    print(artist, '-', title)
    exit
except dbus.exceptions.DBusException:
    exit
