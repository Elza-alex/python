from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfilename
import subprocess
import os
root=Tk()
root.title("Python IDLE")
root.geometry("1280x720+150+80")
root.configure(bg="#323846")
root.resizable(False,False)

#code input
code_input = Text(root,font="consolas 18")
code_input.place(x=180,y=0,width=680,height=720)

#code output
code_output = Text(root,font="consolas 15",bg="#323846",fg="lightgreen")
code_output.place(x=860,y=0,width=420,height=72)

root.mainloop()