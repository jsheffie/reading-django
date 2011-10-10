'''
Created on Aug 28, 2011

@author: jds
'''

from Tkinter import *

def save_data():
    fd = open("deliveries.txt", "a")
    fd.write("Depot:\n")
    fd.write("%s\n" %(depot.get()))
    fd.write("Description:\n")
    fd.write("%s\n" % (description.get()))
    fd.write("Address:\n")
    fd.write("%s" % (address.get("1.0", END)))
    fd.close()
    # Clean up the fields
    depot.delete(0,END)
    description.delete(0,END )
    address.delete("1.0", END)
    
if __name__ == '__main__':
    app = Tk()
    app.title("Head-Ex Deliveries")
    # Tk.Entry Field for Depot:
    Label(app, text = "Depot:").pack() # dont forget to pack those widgets
    depot = Entry(app)
    depot.pack()
    
    # Tk.Entry Field For description
    Label(app, text="Description:").pack()
    description = Entry(app).pack()
      
    # Tk.Text Field for address
    Label(app, text="Address:").pack()
    address = Text(app)
    address.pack()
    
    Button(app, text = "Save", command = save_data).pack()
    app.mainloop()