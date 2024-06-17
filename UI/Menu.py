import tkinter as tk
import tkinter.font as tkFont

import cv2
import pygame
from PIL import Image, ImageTk

from Utils import globals
from Utils import lib


class Menu:

    def __init__(self, root, frame):
        self.__frame = frame
        self.__root = root
        self.__buttonStar = None
        self.__buttonSettings = None
        self.__image = None
        self.__setRoot()
        self.__setFrame()
        self.__fillFrame()
        self.__startMusic()

    @property
    def root(self):
        return self.__root

    @property
    def frame(self):
        return self.__frame

    @property
    def image(self):
        return self.__image

    def __setRoot(self):
        self.__root.title("Campo Minato")
        lib.setRootFullScreen(self.__root)
        self.__root.configure(bg="black")

    def __setFrame(self):
        self.__frame = tk.Frame(self.__root, bg="black", bd=10, relief="groove")
        self.__frame.pack(fill="both", expand=True, padx=10, pady=10)

    def __openSettings(self):
        self.__buttonSettings.config(bg="white", fg="gray")
        self.__frame.destroy()
        globals.Settings.run_module(self.__root)

    def __openGame(self):
        self.__buttonStart.config(bg="white", fg="gray")
        self.__frame.destroy()
        globals.GameController(self.__root).createBoard()

    # IMMAGINE
    def __setImage(self):
        image = cv2.imread(globals.imagePath)
        image = cv2.resize(image, (150, 150))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.__image = ImageTk.PhotoImage(image=Image.fromarray(image))
        return self.__image

    def __fillFrame(self):
        image = self.__setImage()
        imageLabel = tk.Label(self.__frame, image=image, bg="black")
        imageLabel.place(relx=0.5, rely=0.2, anchor='center')

        # TITOLO
        customFont = tkFont.Font(family="Terminal", size=75)
        label = tk.Label(self.__frame, text=" CAMPO MINATO", font=customFont, fg="white", bg="black")
        label.place(relx=0.5, rely=0.4, anchor='center')

        # BUTTON
        self.__buttonStart = lib.createButton(self.__frame, "Start", self.__openGame)
        self.__buttonStart.place(relx=0.5, rely=0.6, anchor='center')
        self.__buttonSettings = lib.createButton(self.__frame, "Settings", self.__openSettings)
        self.__buttonSettings.place(relx=0.5, rely=0.7, anchor='center')

    # MOSECA
    def __startMusic(self):
        pygame.mixer.init()  # Inizializza il mixer audio di pygame
        pygame.mixer.music.load(globals.music)  # Carica il file musicale
        pygame.mixer.music.set_volume(globals.volumeLevel)
        pygame.mixer.music.play(-1)  # Riproduci la music in loop (-1 significa loop infinito)
