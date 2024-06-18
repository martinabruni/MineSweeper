import tkinter as tk

import Utils.globals as g


def setCoreGameUI():
    if g.isFullScreen == False:
        setRootPosition(g.rootGlobal)
    g.frameGlobal = tk.Frame(bg="black", bd=10, relief="groove")
    g.frameGlobal.place(relx=0.5, rely=0.5, anchor='center')


def createButton(frame, text, command):
    return tk.Button(frame, text=text,
                     width=g.buttonWidth,
                     height=g.buttonHeight,
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
    g.isFullScreen = False


def setRootFullScreen(root: tk.Tk):
    root.attributes("-fullscreen", True)
    root.bind("<Escape>", lambda e: endFullScreen(root))
    g.isFullScreen = True

def createEscapeRoot():
    g.escapeRoot = tk.Tk()
    g.escapeRoot.withdraw()

    dialog = tk.Toplevel(g.escapeRoot)
    dialog.title("Scegli un'opzione")

    label = tk.Label(dialog, text="Cosa vuoi fare?")
    label.pack(pady=10)

    button_continue = tk.Button(dialog, text="Restart", command=g.gameController.restartGame)
    button_continue.pack(side=tk.LEFT, padx=10, pady=10)

    button_exit = tk.Button(dialog, text="Menu", command=g.gameController.backToMenu)
    button_exit.pack(side=tk.RIGHT, padx=10, pady=10)

    button_close = tk.Button(dialog, text="Quit", command=g.gameController.quit)
    button_close.pack(side=tk.LEFT, padx=10, pady=10)

    dialog.mainloop()

if __name__ == "__name__":
    root = tk.Tk()
    setRootPosition(root)
    root.mainloop()
