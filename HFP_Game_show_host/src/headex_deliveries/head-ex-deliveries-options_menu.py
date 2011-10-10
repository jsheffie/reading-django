'''
Created on Aug 28, 2011

@author: jds
'''

from Tkinter import *
from tkMessageBox import *

def save_data():
    try:
        fd = open("deliveries.txt", "a")
        fd.write("Depot:\n")
        fd.write("%s\n" %(depot.get()))
        fd.write("Description:\n")
        fd.write("%s\n" % (description.get()))
        fd.write("Address:\n")
        fd.write("%s" % (address.get("1.0", END)))
        fd.close()
        
        # Clean up the fields
        depot.set(None)
        description.delete(0,END )
        address.delete("1.0", END)
    except Exception as ex:
        showerror("Error:", "Can't open file for writing [%s]" % ex)
    
def read_options(file):
    depots = []
    fh = open(file)
    for line in fh:
            depots.append(line.rstrip())

    return depots
        
if __name__ == '__main__':
    app = Tk()
    app.title("Head-Ex Deliveries")
    Label(app, text = "Depot:").pack() # dont forget to pack those widgets

    # Making the Menu: ( reading in the menu/depot from a file)
    # Tk.Radio Field for Depot, note it is using a model depot ( as its controller variable)
    # its MVC baby... and Model=StringVar = V = tkwidget radiobutton, and C = variable 
    depot = StringVar()
    depot.set(None)
    options = []
    try:
        options = read_options("depos.txt")
    except Exception as ex:
        showerror("Error!", "Can't read the file the file \n %s" % ex)
    OptionMenu(app, depot, *options).pack()
    
    
    # Tk.Entry Field For description
    Label(app, text="Description:").pack()
    description = Entry(app)
    description.pack()
    
    # Tk.Text Field for address
    Label(app, text="Address:").pack()
    address = Text(app)
    address.pack()
    
    Button(app, text = "Save", command = save_data).pack()
    app.mainloop()