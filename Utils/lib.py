import tkinter as tk

import Utils.globals as globals

def setCoreGameUI():
    globals.rootGlobal.geometry("")
    globals.frameGlobal.config(bg="black", bd=10, relief="groove")
    globals.frameGlobal.place(relx=0.5, rely=0.5, anchor='center')
    return globals.Board(globals.boardSizeGlobal, globals.bombsPercentage, globals.frameGlobal)

def createButton(frame, text, command):
    return tk.Button(frame, text=text,
                     width=globals.buttonWidth,
                     height=globals.buttonHeight,
                     bg="gray", fg="white",
                     command=command)


def setRootPosition(root: tk.Tk, width=1200, height=700):
    screenW = root.winfo_screenwidth()
    screenH = root.winfo_screenheight()
    x = (screenW - width) // 2
    y = (screenH - height) // 7
    root.geometry(f"{width}x{height}+{x}+{y}")


def endFullScreen(root: tk.Tk):
    root.attributes("-fullscreen", False)
    setRootPosition(root)


def setRootFullScreen(root: tk.Tk):
    root.attributes("-fullscreen", True)
    root.bind("<Escape>", lambda e: endFullScreen(root))


if __name__ == "__name__":
    root = tk.Tk()
    setRootPosition(root)
    root.mainloop()
