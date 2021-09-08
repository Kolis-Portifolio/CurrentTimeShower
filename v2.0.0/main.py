#!/usr/bin/env python3

# Author: Victor Kolis
# Version: 1.0.0
# Purpose: Show user's current local time (clock)

import sys
import time
from tkinter import *
from tkinter.font import Font

# Window setup
root = Tk()
root.title("Current Time Shower")
root.geometry("300x140")
root.config(bg="#000")

font = Font(family="Courier", size=27, weight="bold")

current_time = StringVar()
label = Label(root, textvariable=current_time, font=font)
label.config(bg="#000", fg="#fff")
label.pack(pady=30)


def killall():
    global running
    running = False
    sys.exit()


running = True
while running:
    current_time.set(time.ctime().split()[3])
    root.protocol("WM_DELETE_WINDOW", killall)
    root.update()
