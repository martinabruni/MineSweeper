import tkinter as tk
import tkinter.font as tkFont

import cv2
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
        self.__buttonSettings = lib.createButton(generic.frameGlobal, "Settings", self.__openSettings)
        self.__buttonStart = lib.createButton(generic.frameGlobal, "Start", self.__openGame)
        self.__buttonSettings.place(relx=0.5, rely=0.7, anchor='center')
        self.__buttonStart.place(relx=0.5, rely=0.6, anchor='center')
        self.__buttonQuit = lib.createButton(generic.frameGlobal, "Quit", generic.gameController.quitGame)
        self.__buttonQuit.place(relx=0.5, rely=0.8, anchor='center')

    def __openSettings(self):
        self.__buttonSettings.config(bg="white", fg="gray")
        generic.frameGlobal.destroy()
        generic.gameController.createMenuSettings()

    def __openGame(self):
        self.__buttonStart.config(bg="white", fg="gray")
        generic.frameGlobal.destroy()
        generic.gameController.createBoard()
