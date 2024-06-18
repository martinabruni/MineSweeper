import tkinter as tk
import tkinter.font as tkFont

import cv2
import pygame
from PIL import Image, ImageTk

from Utils import generic
from Utils import lib


class Menu:

    def __init__(self, root, frame):
        self.__frame = frame
        self.__root = root
        self.__buttonStar = None
        self.__buttonSettings = None
        self.__image = None

    @property
    def root(self):
        return self.__root

    @property
    def frame(self):
        return self.__frame

    @property
    def image(self):
        return self.__image

    def initializeMenu(self):
        self.__setRoot()
        self.__setFrame()
        self.__fillFrame()
        self.__startMusic()

    def __setRoot(self):
        self.__root.title("Campo Minato")
        lib.setRootFullScreen(self.__root)
        self.__root.configure(bg="black")

   
    def __openSettings(self):
        self.__buttonSettings.config(bg="white", fg="gray")
        self.__frame.destroy()
        generic.Settings.run_module(self.__root)

    def __openGame(self):
        self.__buttonStart.config(bg="white", fg="gray")
        self.__frame.destroy()
        generic.gameController.createBoard()

    # IMMAGINE
    

        # TITOLO
       

        # BUTTON
        self.__buttonStart = lib.createButton(self.__frame, "Start", self.__openGame)
        self.__buttonStart.place(relx=0.5, rely=0.6, anchor='center')
        self.__buttonSettings = lib.createButton(self.__frame, "Settings", self.__openSettings)
        self.__buttonSettings.place(relx=0.5, rely=0.7, anchor='center')

    # MOSECA
    def __startMusic(self):
        pygame.mixer.init()  # Inizializza il mixer audio di pygame
        pygame.mixer.music.load(generic.music)  # Carica il file musicale
        pygame.mixer.music.set_volume(generic.volumeLevel)
        pygame.mixer.music.play(-1)  # Riproduci la music in loop (-1 significa loop infinito)
