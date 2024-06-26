import tkinter as tk
import tkinter.font as tkFont
import cv2

from PIL import Image, ImageTk
from Utils import generic, lib


class CustomFrame:

    def __init__(self, sizeTitle, textTitle, imagePath):
        self.__sizeTitle = sizeTitle
        self.__textTitle = textTitle
        self.__image = imagePath

    def initializeMenu(self):
        self.__setRoot()
        self.__setFrame()
        self.__setTitle()
        self.__setImage()

    def __setRoot(self):
        generic.rootGlobal.title(self.__textTitle)
        lib.setRootFullScreen(generic.rootGlobal)
        generic.rootGlobal.configure(bg="black")
        
       

    def __setFrame(self):
        generic.frameGlobal = tk.Frame(generic.rootGlobal, bg="black", bd=5, relief="groove")
        generic.frameGlobal.pack(fill="both", expand=True, padx=10, pady=10) 
        
        sfondo_path = generic.imageMenuB  
        sfondo_image = Image.open(sfondo_path)
        sfondo_photo = ImageTk.PhotoImage(sfondo_image)
 
         # Crea una Label per contenere l'immagine di sfondo
        sfondo_label = tk.Label(generic.frameGlobal, image=sfondo_photo)
        sfondo_label.image = sfondo_photo  # Mantiene un riferimento all'immagine
        sfondo_label.place(relwidth=1, relheight=1)  # Copre tutta la finestra

    def __setTitle(self):
        customFont = tkFont.Font(family="Terminal", size=self.__sizeTitle)
        label = tk.Label(generic.frameGlobal, text=self.__textTitle, font=customFont, fg="white", bg="black")
        label.place(relx=0.5, rely=0.4, anchor='center')

    def __setImage(self):
        image = cv2.imread(self.__image)
        image = cv2.resize(image, (150, 150))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.__image = ImageTk.PhotoImage(image=Image.fromarray(image))
        imageLabel = tk.Label(generic.frameGlobal, image=self.__image, bg="black")
        imageLabel.place(relx=0.5, rely=0.2, anchor='center')
