from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
root =Tk()

def New():
    global file
    root.title("Untitle - Notepad")
    file = None
    TextArea.delete(1.0, END)

def Open():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes = [("Text Documents","*.txt*")])
    if file=="":
        file=None

def Save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension = ".txt",filetypes = [("Text Documents","*.txt*")])
        if file == "":
            file = None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file+ " - Notepad"))
            print("File Saved")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()


def Exit():
    root.destroy()

def Cut():
    TextArea.event_generate(("<<Cut>>"))

def Copy():
    TextArea.event_generate(("<<Copy>>"))

def Paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by YourName")

root.title("Notepad")
root.geometry("644x788")
TextArea = Text(root,font="Arial 13")
file =None
TextArea.pack(expand=True, fil=BOTH)

MenuBar = Menu(root)
FileMenu = Menu(MenuBar, tearoff =0)
MenuBar.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="New", command=New)

FileMenu.add_command(label="Open", command=Open)
FileMenu.add_command(label="Save", command=Save)

FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=Exit)

EditMenu = Menu(MenuBar, tearoff =0)
MenuBar.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label="Cut", command=Cut)
EditMenu.add_command(label="Copy", command=Copy)
EditMenu.add_command(label="Paste", command=Paste)

HelpMenu = Menu(MenuBar, tearoff =0)
MenuBar.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="About Notepad", command = about)

root.config(menu=MenuBar)
root.mainloop()