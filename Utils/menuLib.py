import tkinter as tk
import Utils.globals as globals

def createButton(frame, text, command):
    return tk.Button(frame, text=text,
                     width=globals.buttonWidth,
                     height=globals.buttonHeight,
                     bg="gray", fg="white",
                     command=command)