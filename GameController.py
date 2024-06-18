from Utils.lib import *
from Utils import globals as g


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
        g.rootGlobal.quit()

    def createBoard(self):
        setCoreGameUI()
        g.boardGlobal = g.Board(g.frameGlobal)
        g.boardGlobal.initializeBoard()

    # Devid
    def resetGame(self):
        # distruggere la board
        self.destroyBoard()
        # ricreare il menu
        self.createMenu()

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
