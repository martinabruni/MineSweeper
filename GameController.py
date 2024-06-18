from Utils.lib import *
from Utils import globals as g

class GameController:
    def __init__(self, root: tk.Tk, frame: tk.Frame):
        self.__root = root
        self.__frame = frame
        self.__size = g.boardSizeGlobal
        self.__bombPercentage = g.bombsPercentage

    # Elisa
    def createMenu(self):
        globals.menuGlobal.initializeMenu()

    # Elisa
    def createMenuSettings(self):
        pass

    def createBoard(self):
        setCoreGameUI()
        g.boardGlobal = g.Board(self.__size, self.__bombPercentage, self.__frame)
        g.boardGlobal.initializeBoard()

    # Devid
    def resetGame(self):
        # distruggere la board
        # ricreare il menu
        pass

    def destroyMenu(self):
        # distruggere il frame
        pass

    def destroyBoard(self):
        # distrugge il frame
        pass

    def checkWin(self):
        pass

    def checkLose(self):
        pass

    def updateUI(self):
        pass


# Daniela
if __name__ == "__main__":
    pass