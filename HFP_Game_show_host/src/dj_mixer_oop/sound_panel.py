'''
Created on Sep 4, 2011

@author: jds
'''
from Tkinter import *
import pygame.mixer
import os

class SoundPanel(Frame):
    '''
    From the progression in HFP Class Sound Panel is really just the create_gui() 
    function from ../dj_mixer. Implemented as a Subclass of the Frame class.
    '''
    

    def __init__(self, app, mixer, sound_file):
        '''
        Constructor
        '''
        Frame.__init__(self, app)
        self.track = mixer.Sound(sound_file)

        # is track_button < checkbox > 
        # just a local -- class based -- button
        self.track_playing = IntVar() # variable for value of CheckButton
        track_button = Checkbutton(self, variable = self.track_playing, 
                                        command = self.track_toggle, text = os.path.basename(sound_file) )
        track_button.pack(side = LEFT)

        # this is the slider
        self.volume = DoubleVar()
        self.volume.set(self.track.get_volume())
        volume_scale = Scale(self, variable = self.volume, from_ = 0.0, to = 1.0, resolution = 0.1,
                             command = self.change_volume, label = "Volume", orient = HORIZONTAL)
        volume_scale.pack(side=RIGHT, padx=10)        
    
    def track_toggle(self):
        if self.track_playing.get() == 1:
            self.track.play(loops = -1)
        else:
            self.track.stop()
    
    def change_volume(self, v):
        self.track.set_volume(self.volume.get())

    def stop_track(self):
        self.track.stop()

        
    