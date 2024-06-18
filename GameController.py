from Utils.lib import *
from Utils import generic as g


class GameController:
    def __init__(self):
        pass

    # Elisa
    def createMenu(self):
        g.menuGlobal.initializeMenu()

    # Elisa
    def createMenuSettings(self):
        pass

    def quitGame(self):
        g.frameGlobal.destroy()
        g.rootGlobal.destroy()
        g.escapeRoot.destroy()

    def createBoard(self):
        setCoreGameUI()
        g.boardGlobal = g.Board(g.frameGlobal)
        g.boardGlobal.initializeBoard()

    # Devid
    def backToMenu(self):
        self.destroyBoard()
        self.createMenu()
        g.escapeRoot.destroy()

    def restartGame(self):
        self.destroyBoard()
        self.createBoard()
        g.escapeRoot.destroy()

    def destroyMenu(self):
        pass

    def destroyBoard(self):
        # distrugge il frame
        g.frameGlobal.destroy()

    def checkWin(self) -> bool:
        if g.revealedCellsGlobal == g.winCondition:
            return True
        else:
            return False

    def checkLose(self, cellValue: int) -> bool:
        if cellValue == -1:
            return True
        else:
            return False

    def updateUI(self):
        pass


# Daniela
if __name__ == "__main__":
    pass
