'''
Created on Sep 3, 2011

@author: jds
'''

import pygame.mixer
import os
def wait_finished(channel):
    """ is the sound still playing, then we better wait on it """
    while channel.get_busy():
        pass
    
if __name__ == '__main__':

    sounds = pygame.mixer
    sounds.init()
    
    #sounds_dir = "/host/jds/jdevel2/headfirstlabs/hfprog/hfprog_resources/Chapter 7/hfpr"
    snd_dir = os.path.curdir + "/sounds/"

    s = sounds.Sound(snd_dir + "heartbeat.wav")
    wait_finished(s.play())

    s = sounds.Sound(snd_dir + "buzz.wav")
    wait_finished(s.play())

    s = sounds.Sound(snd_dir + "ohno.wav")
    wait_finished(s.play())

    s = sounds.Sound(snd_dir + "carhorn.wav")
    wait_finished(s.play())
