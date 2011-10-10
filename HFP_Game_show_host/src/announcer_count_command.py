'''
Re-Created on Sep 3, 2011
Created on Aug 27, 2011

@author: jds
'''
import pygame.mixer
import os

def wait_finish(channel):
    while channel.get_busy(): # is sound still playing..??
        pass

CORRECT='1'
WRONG  ='2'
QUIT   ='0'

if __name__ == '__main__':
    sounds = pygame.mixer
    sounds.init()
    #sounds_dir = "/host/jds/jdevel2/headfirstlabs/hfprog/hfprog_resources/Chapter 7/hfprog_sounds/"
    sounds_dir = os.path.curdir + "/sounds/"

    correct_s = sounds.Sound(sounds_dir + "correct.wav")    
    wrong_s   = sounds.Sound(sounds_dir + "wrong.wav")    
    
    prompt = "Press %c for Correct, %c for Wrong, %c to Quit" %( CORRECT, WRONG, QUIT)

    number_asked = 0
    number_correct = 0
    number_wrong = 0 
    
    choice = raw_input(prompt) # input for python 3 and raw_input for python2..?
    
    while choice != QUIT:
        number_asked = number_asked + 1

        if choice == CORRECT:
            print "c"
            number_correct = number_correct + 1
            wait_finish(correct_s.play())
        
        if choice == WRONG:
            print "w"
            number_wrong = number_wrong + 1    
            wait_finish(wrong_s.play())
        choice = raw_input(prompt)

    print "You asked %d questions" % ( number_asked )
    print "%d were correctly answered" % ( number_correct )
    print "%d were incorrectly answered" % ( number_wrong)