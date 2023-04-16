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


root.config(menu=MenuBar)
root.mainloop()