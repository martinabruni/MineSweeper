import tkinter as tk
import tkinter.font as tkFont

import cv2
import pygame
from PIL import Image, ImageTk
from Utils.CustomFrame import CustomFrame
from Utils import lib
from Utils import generic


class Menu(CustomFrame):
    def __init__(self, sizeTitle, textTitle, imagePath):
        CustomFrame.__init__(self, sizeTitle, textTitle, imagePath)
        self.__buttonStart = None
        self.__buttonSettings = None
        self.__buttonQuit = None

    def initializeMenu(self):
        CustomFrame.initializeMenu(self)
        self.__buttonStart=lib.pixelButton(generic.frameGlobal,generic.pixelStart,self.__openGame,0.58)
        self.__buttonSettings = lib.pixelButton(generic.frameGlobal,generic.pixelSettings, self.__openSettings,0.70)
        self.__buttonQuit = lib.pixelButton(generic.frameGlobal,generic.pixelQuit, self.__quit,0.81)
   

    def __openSettings(self):
        self.__buttonSettings=lib.changeImage(generic.clickSetting,self.__buttonSettings)
        generic.frameGlobal.destroy()
        generic.gameController.createMenuSettings()      
   

    def __openGame(self):
        self.__buttonStart=lib.changeImage(generic.clickStart,self.__buttonStart)
        generic.frameGlobal.destroy()
        generic.gameController.createGame()      
        
    def __quit(self):
        self.__buttonQuit=lib.changeImage(generic.clickQuit,self.__buttonQuit)
        generic.rootGlobal.destroy()

          

    # MOSECA
    def __startMusic(self):
        pygame.mixer.init()  # Inizializza il mixer audio di pygame
        pygame.mixer.music.load(generic.music)  # Carica il file musicale
        pygame.mixer.music.set_volume(generic.volumeLevel)
        pygame.mixer.music.play(-1)  # Riproduci la music in loop (-1 significa loop infinito)
