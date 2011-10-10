'''
Created on Sep 4, 2011

@author: jds

expand on mixer, and making oo widgits
are doing the example ( basically from chapter 10 of "head first programming" - python )

Here we are going to use sound_panel.py to get our local-functions
'''

from Tkinter import *
from sound_panel import *
import pygame.mixer
import os

app = Tk()
app.title("Head First Mix ( ch10) ")


mixer = pygame.mixer
mixer.init()

sounds_dir = os.path.curdir + "/../music_tracks/"
sound_red_n = sounds_dir + "/50459_M_RED_Nephlimizer.wav"
create_gui(app, mixer, sound_red_n)

sound_red_beep_line = sounds_dir + "/39147_M_RED_beep_line.wav"
create_gui(app, mixer, sound_red_beep_line)


def shutdown():
    """ shutdown call back, effectivally the issue is that if a user "does something" 
    that our event's dont handle... then Tk gets to decide what to do about it... and 
    Tk might not be smart enough to know what "things" in your app might need-to-be-done """
    track.stop()
    app.destroy()
    print "JDS: called-shutdown callback"

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
