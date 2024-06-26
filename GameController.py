from Utils.lib import *
from Utils import generic as g
from Entities.Timer import TimerApp
import pygame

class GameController:
    def __init__(self):
        self.app = None
        self.__startMusic()
    
    # Elisa
    def createMenu(self):
        g.frameGlobal.destroy()
        g.menuGlobal = g.Menu(g.sizeTitle, g.textTitle, g.imagePath)
        g.menuGlobal.initializeMenu()

    # Elisa
    def createMenuSettings(self):
        g.frameGlobal.destroy()
        g.settingsGlobal = g.Settings(g.sizeTitle, g.textTitle, g.imagePath)
        g.settingsGlobal.initializeMenu()

    def quitGame(self):
        g.frameGlobal.destroy()
        g.rootGlobal.destroy()
        if g.escapeRoot:
            g.escapeRoot.destroy()

    def createBoard(self):
        g.frameStats = tk.Frame(g.rootGlobal, bg="black")
        g.frameStats.pack(pady=10)
        g.timer = TimerApp(g.frameStats)
        g.timer.reset_timer()
        setCoreGameUI()
        setWinCondition()
        g.boardGlobal = g.Board(g.frameGlobal)
        g.boardGlobal.initializeBoard()

    # Devid
    def backToMenu(self):
        g.frameGlobal.destroy()
        g.frameStats.destroy()
        g.escapeRoot.destroy()
        g.timer.label.destroy()
        self.createMenu()

    def restartGame(self):
        g.frameGlobal.destroy()
        g.frameStats.destroy()
        g.escapeRoot.destroy()
        g.timer.label.destroy()
        self.createBoard()

    def checkWin(self) -> bool:
        if g.revealedCellsGlobal == g.winCondition:
            g.timer.stop_timer()
            return True
        else:
            return False

    def checkLose(self, cellValue: int) -> bool:
        if cellValue == -1:
            g.timer.stop_timer()
            return True
        else:
            return False

    def updateUI(self):
        pass

    # MOSECA
    def __startMusic(self):
        pygame.mixer.init()  # Inizializza il mixer audio di pygame
        pygame.mixer.music.load(g.music)  # Carica il file musicale
        pygame.mixer.music.set_volume(g.volumeLevel)
        pygame.mixer.music.play(-1)  # Riproduci la music in loop (-1 significa loop infinito)

# Daniela
if __name__ == "__main__":
    pass
