from Utils.lib import *
from Utils import globals as g

class GameController:
    def __init__(self, root: tk.Tk, frame: tk.Frame):
        self.__root = root
        self.__frame = frame
        self.__size = g.boardSizeGlobal
        self.__bombsPercentage = g.bombsPercentageGlobal

    # Elisa
    def createMenu(self):
        globals.menuGlobal.initializeMenu()

    # Elisa
    def createMenuSettings(self):
        pass

    def createBoard(self):
        setCoreGameUI()
        g.boardGlobal = g.Board(self.__frame)
        g.boardGlobal.initializeBoard()

    # Devid
    def resetGame(self):

        pass

    def destroyMenu(self):
        # distruggere il frame
        pass

    def destroyBoard(self):
        # distrugge il frame
        pass

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