import tkinter as tk
import tkinter.font as tkFont

import cv2
import pygame
from PIL import Image, ImageTk
from Utils.CustomFrame import CustomFrame
from Utils import lib
from Utils import generic


class Settings(CustomFrame):
    def __init__(self, sizeTitle, textTitle, imagePath):
        CustomFrame.__init__(self, sizeTitle, textTitle, imagePath)
        self.__buttonEasy = None
        self.__buttonMedium = None
        self.__buttonHard = None
        self.__saveButton = None

    def initializeMenu(self):
        CustomFrame.initializeMenu(self)
        self.__buttonEasy = lib.createButton(generic.frameGlobal, "Easy", self.__setEasyLevel, bg="green")
        self.__buttonMedium = lib.createButton(generic.frameGlobal, "Medium", self.__setMediumLevel, bg="orange")
        self.__buttonHard = lib.createButton(generic.frameGlobal, "Hard", self.__setHardLevel, bg="red")
        self.__buttonEasy.place(relx=0.5, rely=0.6, anchor='center')
        self.__buttonMedium.place(relx=0.5, rely=0.7, anchor='center')
        self.__buttonHard.place(relx=0.5, rely=0.8, anchor='center')

    def __setHardLevel(self):
        generic.boardSizeGlobal = 15
        generic.bombsPercentageGlobal = 16
        generic.gameController.createMenu()

    def __setMediumLevel(self):
        generic.boardSizeGlobal = 10
        generic.bombsPercentageGlobal = 16
        generic.gameController.createMenu()

    def __setEasyLevel(self):
        generic.boardSizeGlobal = 7
        generic.bombsPercentageGlobal = 20
        generic.gameController.createMenu()
