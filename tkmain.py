from tkinter import *
from tkinter import ttk
import playsound

from os import listdir
from os.path import isfile, join


def playsoundWidget():
    files = [f for f in listdir("sounds") if isfile(join("sounds/", f))]
    playsound.playsound("sounds/"+files[0])

root = Tk()
root.title("Spook 1.0")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Play", command=playsoundWidget).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
root.mainloop()
