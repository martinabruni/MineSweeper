import random
import tkinter as tk
from Entities.Cell import Cell


class Board:
    def __init__(self, size: int, bombPercentage: int, frame: tk.Frame):
        self.__board = [[Cell(x, y, frame) for y in range(size)] for x in range(size)]
        self.__size = size
        self.__bombs = int(size * size * (bombPercentage / 100))
        self.__frame = frame

    @property
    def board(self):
        return self.__board
    @property
    def size(self):
        return self.__size

    def initializeBoard(self):
        self.__placeBombs()
        self.__assignValues()

    def __placeBombs(self):
        placedBombs = 0
        while placedBombs < self.__bombs:
            x, y = random.randint(0, self.__size - 1), random.randint(0, self.__size - 1)
            if self.__board[x][y].value != -1:
                self.__board[x][y].value = -1
                placedBombs += 1

    def __assignValues(self):
        for row in self.__board:
            for cell in row:
                if cell.value == -1:
                    continue
                cell.value = self.__countAdiacentBombs(cell)

    def __countAdiacentBombs(self, cell: Cell):
        adiacentBombs = 0
        for i in range(max(cell.x - 1, 0), min(cell.x + 2, self.__size)):
            for j in range(max(cell.y - 1, 0), min(cell.y + 2, self.__size)):
                if cell.x == i and cell.y == j:
                    continue
                else:
                    if self.__board[i][j].value == -1:
                        adiacentBombs += 1
        return adiacentBombs

    def printBoard(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print(f"{str(self.__board[i][j].value)}", end=" ")
            print()

    def printAllCells(self):
        for row in self.__board:
            for cell in row:
                cell.printCell()


# codice di test per vedere se la logica funziona
if __name__ == "__main__":
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    b = Board(10, 5, frame)
    b.initializeBoard()
    b.printBoard()
    root.mainloop()
