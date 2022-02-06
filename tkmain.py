from tkinter import *
from tkinter import ttk
import subprocess
from random import randrange

from os import listdir
from os.path import isfile, join

import time
import datetime

def playsoundWidget():
    time.sleep(5)
    
    files = [f for f in listdir("/home/pi/Music") if isfile(join("/home/pi/Music/", f))]
    selected = randrange(len(files))
    print("Playing " + files[selected])
    filePath = "/home/pi/Music/"+files[selected]
    
    subprocess.run(["sudo", "aplay", filePath])
while True:
    if datetime.datetime.now().minute == 15:
        playsoundWidget()
        time.sleep(60)

"""
root = Tk()

root.after(10, playsoundWidget)
root.title("Spook 1.0")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="Play", command=playsoundWidget).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
root.mainloop()

"""
