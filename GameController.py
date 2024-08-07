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
        g.frameTimer.pack(pady=10, fill="x")
        g.timer = TimerApp(g.frameTimer)
        g.timer.reset_timer()

    def createStats(self):
        bombs = tk.StringVar()
        bombs.set(f"Bombe: {g.boardSizeGlobal**2 - g.winCondition} ")
        posButtons = 0.15
        bombslabel = tk.Label(g.frameTimer, textvariable=bombs, font=("Terminal", 15), bg="black", fg="red")
        bombslabel.place(relx=0.10, rely=posButtons, anchor='center')
        self.cells.set(f"Celle da rivelare: {g.winCondition - g.revealedCellsGlobal} ")
        cellslabel = tk.Label(g.frameTimer, textvariable=self.cells, font=("Terminal", 15), bg="black", fg="red")
        cellslabel.place(relx=0.10, rely=posButtons + 0.35, anchor='center')

        button_close = tk.Button(g.frameTimer, text="Quit", command=g.gameController.quitGame, bg="red", fg="white", width=g.buttonWidth)
        button_close.place(relx=0.95, rely=posButtons, anchor='center')
        button_continue = tk.Button(g.frameTimer, text="Restart", command=g.gameController.restartGame, bg="green", fg="white", width=g.buttonWidth)
        button_continue.place(relx=0.95, rely=posButtons+0.35, anchor='center')
        button_exit = tk.Button(g.frameTimer, text="Menu", command=g.gameController.createMenu, bg="orange", fg="white", width=g.buttonWidth)
        button_exit.place(relx=0.95, rely=posButtons+0.7, anchor='center')


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
            g.endGame = True
            return True
        else:
            return False

    def checkLose(self, cellValue: int) -> bool:
        if cellValue == -1:
            g.timer.stop_timer()
            g.endGame = True
            return True
        else:
            return False

    def updateUI(self):
        if g.frameGlobal:
            g.frameGlobal.destroy()
            g.frameGlobal = None
            g.frameStats = None
        if g.escapeRoot:
            g.escapeRoot.destroy()
            g.escapeRoot = None
        if g.frameTimer:
            g.frameTimer.destroy()
            g.frameTimer = None
        if g.timer:
            g.timer.label.destroy()

    def __startMusic(self):
        pygame.mixer.init()  # Inizializza il mixer audio di pygame
        pygame.mixer.music.load(g.music)  # Carica il file musicale
        pygame.mixer.music.set_volume(g.volumeLevel)
        pygame.mixer.music.play(-1)  # Riproduci la music in loop (-1 significa loop infinito)