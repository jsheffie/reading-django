'''
Created on Sep 4, 2011

@author: jds

here we [ thats nice I am now referring to myself in the 3rd person ]
are doing the example ( basically from chapter 9 of "head first programming" - python )
'''

from Tkinter import *
import pygame.mixer
import os

app = Tk()
app.title("Head First Mix ( ch9) ")

sounds_dir = os.path.curdir + "/../music_tracks/"
sound_file = sounds_dir + "/50459_M_RED_Nephlimizer.wav"

mixer = pygame.mixer
mixer.init()

def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    else:
        track.stop()

def change_volume(v):
    track.set_volume(volume.get())
    
track = mixer.Sound(sound_file)

track_playing = IntVar()
track_button = Checkbutton(app, variable = track_playing, 
                           command = track_toggle, text = sound_file )
track_button.pack(side = LEFT)

volume = DoubleVar()
volume.set(track.get_volume())
volume_scale = Scale(variable = volume, from_ = 0.0, to = 1.0, resolution = 0.1,
                      command = change_volume, label = "Volume", orient = HORIZONTAL)
volume_scale.pack(side=RIGHT)

def shutdown():
    """ shutdown call back, effectivally the issue is that if a user "does something" 
    that our event's dont handle... then Tk gets to decide what to do about it... and 
    Tk might not be smart enough to know what "things" in your app might need-to-be-done """
    track.stop()
    app.destroy()
    print "JDS: called-shutdown callback"

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
