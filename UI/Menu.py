import tkinter as tk
import tkinter.font as tkFont

import cv2
import pygame
from PIL import Image, ImageTk
from Utils.Frame import Frame
from Utils import lib
from Utils import generic


class Menu(Frame):
    def __init__(self, sizeTitle, textTitle, imagePath):
        Frame.__init__(self, sizeTitle, textTitle, imagePath)
        self.__buttonStart = None
        self.__buttonSettings = None
    @property
    def image(self):
        return self.__image

    def initializeMenu(self):
        self.__setRoot()
        Frame.initializeMenu(self)
        self.__buttonSettings = lib.createButton(generic.frameGlobal, "Settings", self.__openSettings)
        self.__buttonStart = lib.createButton(generic.frameGlobal, "Start", self.__openGame)
        self.__buttonSettings.place(relx=0.5, rely=0.7, anchor='center')
        self.__buttonStart.place(relx=0.5, rely=0.6, anchor='center')
        self.__startMusic()

    def __setRoot(self):
        generic.rootGlobal.title("Campo Minato")
        lib.setRootFullScreen(generic.rootGlobal)
        generic.rootGlobal.configure(bg="black")

    def __openSettings(self):
        self.__buttonSettings.config(bg="white", fg="gray")
        generic.frameGlobal.destroy()
        generic.Settings.run_module(generic.rootGlobal)

    def __openGame(self):
        self.__buttonStart.config(bg="white", fg="gray")
        generic.frameGlobal.destroy()
        generic.gameController.createBoard()

        # IMMAGINE

        # TITOLO

        # BUTTON
        # self.__buttonStart = lib.createButton(self.__frame, "Start", self.__openGame)
        # self.__buttonStart.place(relx=0.5, rely=0.6, anchor='center')
        # self.__buttonSettings = lib.createButton(self.__frame, "Settings", self.__openSettings)
        # self.__buttonSettings.place(relx=0.5, rely=0.7, anchor='center')

    # MOSECA
    def __startMusic(self):
        pygame.mixer.init()  # Inizializza il mixer audio di pygame
        pygame.mixer.music.load(generic.music)  # Carica il file musicale
        pygame.mixer.music.set_volume(generic.volumeLevel)
        pygame.mixer.music.play(-1)  # Riproduci la music in loop (-1 significa loop infinito)
