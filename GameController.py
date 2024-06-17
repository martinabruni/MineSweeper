from Utils.lib import *


class GameController:
    def __init__(self, root: tk.Tk):
        self.__root = root
        self.__frame = None
        self.__size = 5
        self.__bombPercentage = 20

    # Elisa
    def createMenu(self):
        globals.Menu(self.__root, self.__frame)

    # Elisa
    def createMenuSettings(self):
        pass

    def createBoard(self):
        self.__root.geometry("")
        self.__frame = tk.Frame(self.__root, bg="black", bd=10, relief="groove")
        self.__frame.place(relx=0.5, rely=0.5, anchor='center')
        self.__board = globals.Board(self.__size, self.__bombPercentage, self.__frame)
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
    game_ui = GameController(root)
    game_ui.createMenu()
    root.mainloop()
