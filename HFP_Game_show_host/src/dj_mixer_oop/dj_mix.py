'''
Created on Sep 4, 2011

@author: jds
'''

# Layout is annoying 
# only display the filename... in the lable...
# add a dir bar where we display the location of the wave files and give the user th
# the option to change them.
# help

from Tkinter import *
import pygame.mixer
from  sound_panel import SoundPanel
import os


if __name__ == '__main__':
    app = Tk()
    app.title("Head First Mix ( ch10 Final OOP) ")
        
    mixer = pygame.mixer
    mixer.init()
    
        
    sounds_dir = os.path.curdir + "/../music_tracks/"
    dirList = os.listdir(sounds_dir)    
    for fname in dirList:
        if fname.endswith(".wav"):  
            panel = SoundPanel(app, mixer, sounds_dir + "/" + fname)
            panel.pack()
    
    def shutdown():
        """ shutdown call back, effectivally the issue is that if a user "does something" 
        that our event's dont handle... then Tk gets to decide what to do about it... and 
        Tk might not be smart enough to know what "things" in your app might need-to-be-done """
        panel.stop_track()
        app.destroy()
        print "JDS: called-shutdown callback"
    
    app.protocol("WM_DELETE_WINDOW", shutdown)
    app.mainloop()
