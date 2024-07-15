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
        self.__buttonEasy = lib.pixelButton(generic.frameGlobal,generic.pixelEasy,self.__setEasyLevel,0.58)
        self.__buttonMedium = lib.pixelButton(generic.frameGlobal,generic.pixelMedium,self.__setMediumLevel,0.70)
        self.__buttonHard = lib.pixelButton(generic.frameGlobal,generic.pixelHard,self.__setHardLevel,0.81)
        

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
