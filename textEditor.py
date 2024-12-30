from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


filename = None

def newFile():
    global filename
    filename = "Untitled"    
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode = "w", defaultextension='.txt')
    t = text.get(0.0, END)
    
    try:
        f.write(t.rstrip())
    
    except:
        showerror(title="Oops!", message= "Unable to save...")
        
def openFile():
    f = askopenfile(mode = 'r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    
def undo():
    try:
        text.edit_undo()
    except TclError:
        showerror("Nothing to undo!")

def redo():
    try:
        text.edit_redo()
    except TclError:
        pass
    
root = Tk()
root.title("My text editor")

root.minsize(width=500, height=400)
root.maxsize(width=700, height=700)

text = Text(root, width=500, height=500, undo=True)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As..", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(root)
editmenu.add_command(label="Undo", command= undo)
editmenu.add_command(label="Redo", command= redo)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)
root.mainloop()
