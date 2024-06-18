import random
import tkinter as tk

from Entities.Cell import Cell
from Utils import globals as g


class Board:
    def __init__(self, frame: tk.Frame):
        self.__size = g.boardSizeGlobal
        self.__bombs = int(self.__size ** 2 * (g.bombsPercentageGlobal / 100))
        self.__board = [[Cell(x, y, frame) for y in range(self.__size)] for x in range(self.__size)]
        self.__bombsList = []
        self.__frame = frame

    @property
    def board(self):
        return self.__board

    @property
    def size(self):
        return self.__size

    @property
    def bombsList(self):
        return self.__bombsList

    def initializeBoard(self):
        g.revealedCellsGlobal = 0
        self.__placeBombs()
        self.__assignValues()
        self.printBoard()

    def __placeBombs(self):
        placedBombs = 0
        while placedBombs < self.__bombs:
            x, y = random.randint(0, self.__size - 1), random.randint(0, self.__size - 1)
            if self.__board[x][y].value != -1:
                newBomb = self.__board[x][y]
                newBomb.value = -1
                self.__bombsList.append(newBomb)
                placedBombs += 1

    def __assignValues(self):
        for row in self.__board:
            for cell in row:
                if cell.value == -1:
                    continue
                cell.value = self.__countAdiacentBombs(cell)
                self.__addAdjacentCell(cell)

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

    def __addAdjacentCell(self, cell: Cell):
        if cell.value == 0:
            for i in range(max(cell.x - 1, 0), min(cell.x + 2, self.__size)):
                for j in range(max(cell.y - 1, 0), min(cell.y + 2, self.__size)):
                    if cell.x == i and cell.y == j:
                        continue
                    else:
                        cell.adjacentCell.append(self.__board[i][j])

    def revealBombs(self):
        for bomb in self.__bombsList:
            bomb.revealCell()

    def printBoard(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print(f"{str(self.__board[i][j].value)}", end=" ")
            print()
        print("============================")

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
