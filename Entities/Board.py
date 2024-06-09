import random

from Cell import Cell


class Board:
    def __init__(self, size: int, bombPercentage: int):
        self.__board = [[Cell(x, y) for y in range(size + 1)] for x in range(size + 1)]
        self.__size = size
        self.__bombs = int(size * size * (bombPercentage / 100))

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
        for i in range(max(cell.x - 1, 0), min(cell.x + 2, self.__size + 1)):
            for j in range(max(cell.y - 1, 0), min(cell.y + 2, self.__size + 1)):
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


# codice di test per vedere se la logica funziona
if __name__ == "__main__":
    board = Board(5, 10)
    board.initializeBoard()
    board.printBoard()
