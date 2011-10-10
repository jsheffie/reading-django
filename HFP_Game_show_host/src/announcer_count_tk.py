'''
Created on Sep 3, 2011

@author: jds
'''
from Tkinter import *
import pygame.mixer
import os

sounds = pygame.mixer
sounds.init()
sounds_dir = os.path.curdir + "/sounds/"

correct_s = sounds.Sound(sounds_dir + "correct.wav")    
wrong_s   = sounds.Sound(sounds_dir + "wrong.wav") 

num_good=False
num_wrong=False
tot_num=False

number_correct = 0
number_wrong = 0
number_asked=0

def wait_finish(channel):
    while channel.get_busy(): # is sound still playing..??
        pass

def play_correct_sound():
    global number_correct, num_good, number_asked
    number_correct = number_correct + 1
    number_asked = number_asked + 1
    num_good.set(number_correct)
    tot_num.set(number_asked)
    correct_s.play()

def play_wrong_sound():
    global number_wrong, num_wrong, number_asked
    number_wrong = number_wrong + 1
    number_asked = number_asked + 1
    num_wrong.set(number_wrong)
    tot_num.set(number_asked)
    wrong_s.play()

CORRECT='1'
WRONG='2'
QUIT='0'

if __name__ == '__main__':
    app = Tk()
    app.title("TVN Game Show")
    app.geometry('300x110+200+100') #widthxheight+x+y

    lbl = Label(app, text="When you are ready, click on the buttons!", height = 3)
    lbl.pack()

    # GUI: Varialbles
    num_good = IntVar()
    num_good.set(0)
    lbl_ng = Label(app, textvariable = num_good)
    lbl_ng.pack(side='left')
    
    num_wrong = IntVar()
    num_wrong.set(0)
    lbl_ng = Label(app, textvariable = num_wrong)
    lbl_ng.pack(side='right')

    tot_num = IntVar()
    tot_num.set(0)
    lbl_ng = Label(app, textvariable = tot_num)
    lbl_ng.pack(side='bottom')

    # GUI Buttons    
    button_one = Button(app, text="Correct!", width=10, command=play_correct_sound)
    button_one.pack(side='left', padx=10, pady=10)
    
    button_two = Button(app, text="Wrong!", width=10, command=play_wrong_sound)
    button_two.pack(side='right', padx=10, pady=10)
    
    app.mainloop()
    
    print "You asked %d questions" % ( number_asked )
    print "%d were correctly answered" % ( number_correct )
    print "%d were incorrectly answered" % ( number_wrong)