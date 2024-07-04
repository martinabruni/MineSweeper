import tkinter as tk
from GameController import GameController
import math
from Entities.Timer import TimerApp
from UI.Menu import Menu
from Entities.Board import Board
from UI.Settings import Settings

# UI variables
redFlag = "\U0001F6A9"
bomb = "\U0001F4A3"
buttonWidth = 10
buttonHeight = 2
imagePath = "Assets/icona.png"
imageMenuB="Assets/sfondoMenu.png"
imageSettings = "Assets/settingsImage.png"

pixelStart= "Assets/StartButton.png"
pixelSettings= "Assets/ButtonSettings.png"
pixelQuit="Assets/ButtonQuit.png"
pixelEasy="Assets/ButtonEasy.png"
pixelMedium="Assets/ButtonMedium.png"
pixelHard="Assets/ButtonHard.png"

clickStart="Assets/StartButtonG.png"
clickSetting="Assets/ButtonSettingG.png"
clickQuit="Assets/ButtonQuitG.png"
clickEasy="Assets/ButtonEasyG.png"
clickMedium="Assets/ButtonMediumG.png"
clickHard="Assets/ButtonHardG.png"

gifBomba = "gifb.gif"
gifBandiera = "giff.gif"
music = "Assets/retrovideogame.mp3"
volumeLevel = 0.1
isFullScreen = False
sizeTitle = 75
gameTitle = "CAMPO MINATO"
settingsTitle = "SETTINGS"

# Game logic variables
boardSizeGlobal = 5
bombsPercentageGlobal = 20
revealedCellsGlobal = 0
winCondition = 0

# UI objects
escapeRoot = None
rootGlobal = tk.Tk()
frameGlobal = tk.Frame(rootGlobal)
frameTimer = None
frameStats = None
gameController = GameController()
menuGlobal = None
settingsGlobal = None

# Core gameplay objects
boardGlobal = None
timer = None

