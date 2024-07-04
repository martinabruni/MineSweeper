import math
import tkinter as tk
import math
import Utils.generic as g
from PIL import Image, ImageTk

def setWinCondition():
    g.winCondition = math.ceil(g.boardSizeGlobal ** 2 * (100 - g.bombsPercentageGlobal) / 100)


def setCoreGameUI():
    if g.isFullScreen == False:
        setRootPosition(g.rootGlobal)
    g.frameGlobal = tk.Frame(bg="black", bd=10, relief="groove")
    g.frameGlobal.place(relx=0.5, rely=0.5, anchor='center')


def createButton(frame, text, command, fg="white", bg="grey"):
    return tk.Button(frame, text=text,
                     width=g.buttonWidth,
                     height=g.buttonHeight,
                     bg=bg, fg=fg,
                     command=command)

def pixelButton(frame,image,command,rely):
    # Caricamento dell'immagine pixelata
    pixel_image = Image.open(image)
    pixel_image = pixel_image.resize((130, 60), Image.LANCZOS) 
    photo = ImageTk.PhotoImage(pixel_image)
    
    # Creazione del bottone con immagine pixelata
    button = tk.Button(
        frame,
        image=photo,
        command=command,
        borderwidth=0,
        highlightthickness=0,
        relief=tk.FLAT,        
        activebackground="#000000",  
        activeforeground="#000000"
    )
    button.image = photo 
   
    button.place(relx=0.5, rely=rely, anchor='center')  
    
def changeImage(image,button):
    new_image = Image.open(image)
    new_image = new_image.resize((100, 60), Image.LANCZOS)  # Ridimensiona l'immagine
    new_photo = ImageTk.PhotoImage(new_image)
    button.config(image=new_photo)
    button.image = new_photo  # Mantieni il riferimento all'immagine  
    
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


def createEscapeRoot(title):
    g.escapeRoot = tk.Tk()
    g.escapeRoot.withdraw()

    dialog = tk.Toplevel(g.escapeRoot)
    dialog.title("Scegli un'opzione")

    label = tk.Label(dialog, text=title)
    label.pack(pady=10)

    button_continue = tk.Button(dialog, text="Restart", command=g.gameController.restartGame)
    button_continue.pack(side=tk.LEFT, padx=10, pady=10)

    button_exit = tk.Button(dialog, text="Menu", command=g.gameController.createMenu)
    button_exit.pack(side=tk.RIGHT, padx=10, pady=10)

    button_close = tk.Button(dialog, text="Quit", command=g.gameController.quitGame)
    button_close.pack(side=tk.LEFT, padx=10, pady=10)

    dialog.mainloop()


if __name__ == "__name__":
    root = tk.Tk()
    setRootPosition(root)
    root.mainloop()
