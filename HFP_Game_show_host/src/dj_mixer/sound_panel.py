'''
Created on Sep 4, 2011

@author: jds

From Page 360 if head First Programming Python
Chapter 10, we are turning our mixer into "function-in-a-function"
i.e. local function based code... this is so that we can have multiple
mixers each with there own call-stack... er umm... widgets and event handelers
'''
from Tkinter import *
#import pygame

def create_gui(app, mixer, sound_file):
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
    volume_scale = Scale(app, variable = volume, from_ = 0.0, to = 1.0, resolution = 0.1,
                          command = change_volume, label = "Volume", orient = HORIZONTAL)
    volume_scale.pack(side=RIGHT)



class MyClass(object):
    '''
    classdocs
    '''


    def __init__(selfparams):
        '''
        Constructor
        '''
        