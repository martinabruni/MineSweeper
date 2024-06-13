import tkinter as tk
from Entities.Board import Board

class MineSweeperUI:
    """Questa classe gestisce l'interfaccia utente"""

    def __init__(self, root: tk.Tk):
        self.__root = root
        self.__size = 5
        self.__bombPercentage = 20

    # Elisa
    def createMenu(self):
        pass
    
    # Elisa
    def createMenuSettings(self):
        pass

    def createBoard(self):
        # creare un frame
        self.__frame = tk.Frame(self.__root, bg="black", bd=10, relief="groove")
        # impacchettare il frame
        self.__frame.pack(fill="both", expand=True, padx=10, pady=10)
        # creare un oggetto di una classe (scoprila)
        self.__board = Board(self.__size, self.__bombPercentage, self.__frame)
        # chiamare il metodo di quell'oggetto che crea la Board
        self.__board.initializeBoard()

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
    root = tk.Tk()
    game_ui = MineSweeperUI(root)
    game_ui.createBoard()
    root.mainloop()