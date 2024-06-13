import tkinter as tk
from Entities.Board import Board
import menuLib as mL

class MineSweeperUI:
    """Questa classe gestisce l'interfaccia utente"""

    def __init__(self, root: tk.Tk):
        self.__root = root
        self.__frame = None

    # Elisa
    def createMenu(self):
        mL.set_root(self.__root)
        mL.set_Frame(self.__root, self.__frame)
        mL.fill_Frame(self.__frame)
    
    # Elisa
    def createMenuSettings(self):
        pass

    # Daniela
    def createBoard(self):
        pass

    def resetGame(self):
        pass

    def destroyMenu(self):
        pass

    def destroyBoard(self):
        pass

    def checkWin(self):
        pass

    def checkLose(self):
        pass

    def updateUI(self):
        pass

# Daniela
if __name__ == "__main__":
    root = tk.Tk()
    MineSweeperUI(root).createMenu()
    root.mainloop()