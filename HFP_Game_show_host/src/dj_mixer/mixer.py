'''
Created on Sep 3, 2011

@author: jds
'''

from Tkinter import *
import pygame.mixer, os

app = Tk()
app.title=("Head First Mix")
app.geometry('250x100+200+100')

sounds_dir = os.path.curdir + "/../music_tracks/"

sound_file = sounds_dir + "/50459_M_RED_Nephlimizer.wav"

print sound_file
print type(sound_file)
if os.path.isfile(sound_file):
    print "We found the sound file %s" % (sound_file)
else:
    raise "Error: could not find file [%s]" % (sound_file)
    
sounds = pygame.mixer
sounds.init()
track = sounds.Sound(sound_file) 


def track_start():
    track.play(loops = -1)
    
def track_stop():
    track.stop()

start_button = Button(app, command = track_start, text = "Start").pack(side=LEFT)
start_button = Button(app, command = track_stop, text = "stop").pack(side=RIGHT)

app.mainloop()

#if __name__ == '__main__':
#    pass