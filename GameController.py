from Utils.lib import *
from Utils import generic as g
from Entities.Timer import TimerApp

class GameController:
    def __init__(self):
        pass
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
        g.escapeRoot.destroy()

    def createBoard(self):
        g.timer = TimerApp(g.rootGlobal)
        g.timer.reset_timer()
        setCoreGameUI()
        setWinCondition()
        g.boardGlobal = g.Board(g.frameGlobal)
        g.boardGlobal.initializeBoard()

    # Devid
    def backToMenu(self):
        g.frameGlobal.destroy()
        g.escapeRoot.destroy()
        g.timer.label.destroy()
        self.createMenu()

    def restartGame(self):
        g.frameGlobal.destroy()
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


# Daniela
if __name__ == "__main__":
    pass
