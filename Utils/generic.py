import tkinter as tk
from GameController import GameController
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
imageSettings = "Assets/settingsImage.png"
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
endGame = False

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

