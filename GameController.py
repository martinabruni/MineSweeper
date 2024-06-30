from Utils.lib import *
from Utils import generic as g
from Entities.Timer import TimerApp
import pygame


class GameController:
    def __init__(self):
        self.cells = tk.StringVar()
        self.app = None
        self.__startMusic()

    # Elisa
    def createMenu(self):
        self.updateUI()
        g.menuGlobal = g.Menu(g.sizeTitle, g.gameTitle, g.imagePath)
        g.menuGlobal.initializeMenu()

    # Elisa
    def createMenuSettings(self):
        self.updateUI()
        g.settingsGlobal = g.Settings(g.sizeTitle, g.settingsTitle, g.imageSettings)
        g.settingsGlobal.initializeMenu()

    def createGame(self):
        self.createBoard()
        self.createTimer()
        self.createStats()

    def createBoard(self):
        setCoreGameUI()
        setWinCondition()
        g.boardGlobal = g.Board(g.frameGlobal)

    def createTimer(self):
        g.frameTimer = tk.Frame(g.rootGlobal, bg="black")
        g.frameTimer.pack(pady=10)
        g.timer = TimerApp(g.frameTimer)
        g.timer.reset_timer()

    def createStats(self):
        g.frameStats = tk.Frame(g.rootGlobal, bg="black")
        g.frameStats.pack(side="left", padx=1, pady=10)
        bombs = tk.StringVar()
        bombs.set(f"Bombe: {g.boardSizeGlobal**2 - g.winCondition} ")
        bombslabel = tk.Label(g.frameStats, textvariable=bombs, font=("Terminal", 22), bg="black", fg="red")
        bombslabel.grid(row=0, column=1, columnspan=1, padx=0,pady=0)
        self.cells.set(f"    Celle da rivelare: {g.winCondition - g.revealedCellsGlobal} ")
        cellslabel = tk.Label(g.frameStats, textvariable=self.cells, font=("Terminal", 22), bg="black", fg="red")
        cellslabel.grid(row=1, column=1, columnspan=2, padx=0, pady=0)

    def updateCellsLabel(self):
        self.cells.set(f"    Celle da rivelare: {g.winCondition - g.revealedCellsGlobal}")

    def quitGame(self):
        if g.escapeRoot:
            g.escapeRoot.destroy()
        g.rootGlobal.destroy()

    def restartGame(self):
        self.updateUI()
        self.createGame()

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
        if g.frameGlobal:
            g.frameGlobal.destroy()
            g.frameGlobal = None
        if g.frameStats:
            g.frameStats.destroy()
            g.frameStats = None
        if g.escapeRoot:
            g.escapeRoot.destroy()
            g.escapeRoot = None
        if g.frameTimer:
            g.frameTimer.destroy()
            g.frameTimer = None
        if g.timer:
            g.timer.label.destroy()

    # MOSECA
    def __startMusic(self):
        pygame.mixer.init()  # Inizializza il mixer audio di pygame
        pygame.mixer.music.load(g.music)  # Carica il file musicale
        pygame.mixer.music.set_volume(g.volumeLevel)
        pygame.mixer.music.play(-1)  # Riproduci la music in loop (-1 significa loop infinito)


# Daniela
if __name__ == "__main__":
    pass
