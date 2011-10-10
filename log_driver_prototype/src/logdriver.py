'''
Created on Sep 3, 2011

@author: jds
'''

from Tkinter import *


def pause_data():
    print "Pausing... well not really yet"

def continue_data():
    print "Pausing... well not really yet"

if __name__ == '__main__':
    app = Tk()
    app.title("loggen_prototype")

    Label( app, text = "Source Data File:").pack()
    
    # Tk.Text Field for address
    Label(app, text="Source Data Output:").pack()
    output_file_textarea = Entry(app).pack()
    
        # Tk.Text Field for address
    Label(app, text="Data:").pack()
    data = Text(app).pack()
    
    Button(app, text = "Pause", command = pause_data).pack()
    Button(app, text = "Continue", command = pause_data).pack()
    app.mainloop()
    