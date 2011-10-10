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
    depot.set(None)
    description.delete(0,END )
    address.delete("1.0", END)
    
if __name__ == '__main__':
    app = Tk()
    app.title("Head-Ex Deliveries")
    Label(app, text = "Depot:").pack() # dont forget to pack those widgets
    # Tk.Radio Field for Depot, note it is using a model depot ( as its controller variable)
    # its MVC baby... and Model=StringVar = V = tkwidget radiobutton, and C = variable 
    depot = StringVar()
    depot.set(None)
    Radiobutton(app, variable=depot, text="Cambridge, MA", value="Cambridge, MA").pack()
    Radiobutton(app, variable=depot, text="Cambridge, UK", value="Cambridge, UK").pack()
    Radiobutton(app, variable=depot, text="Seattle, WA", value="Seattle, WA").pack()
    
 
    #depot = Entry(app)
    #depot.pack()
    
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