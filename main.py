#!/usr/bin/env python3

# Author: Victor Kolis
# Version: 1.0.0
# Purpose: Show user's current local time (clock)

import os
import time
import pygame
from tkinter import *
from tkinter.font import Font


# Installing the requirements
print("Installing the requirements. Please wait!")
os.system("pip install -r requirements.txt")

# Constants
# Hex Colors
BLACK = "#000"
WHITE = "#fff"


# Functions
def update():
    textvariable.set(time.ctime().split()[3])
    root.after(1000, update)
    pygame.mixer.music.play(loops=0)


# Window setup
root = Tk()
root.title("Current Time Shower")
root.config(bg=BLACK)
root.geometry("400x500")
root.resizable(False, False)

# Audio setup
pygame.mixer.init()
pygame.mixer.music.load("src/clock_tick.ogg")

# Label setup
font = Font(family="Courier", size=40, weight="bold")
textvariable = StringVar()
textvariable.set(time.ctime().split()[3])
time_label = Label(root, textvariable=textvariable, font=font, cursor="fleur", bg=BLACK, fg=WHITE).pack(pady=210)

# Software loop
root.after(1000, update)
root.mainloop()
