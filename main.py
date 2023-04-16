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

MenuBar.add_cascade(label="Edit", menu=EditMenu)
FileMenu.add_command(label="Cut", command=Cut)
FileMenu.add_command(label="Copy", command=Copy)
FileMenu.add_command(label="Paste", command=Paste)

MenuBar.add_cascade(label="Help", menu=HelpMenu)
HelpMenu=Menu(MenuBar, tearoff=0)

root.config(menu=MenuBar)
root.mainloop()