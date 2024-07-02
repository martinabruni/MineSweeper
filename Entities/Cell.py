import tkinter as tk
from tkinter import messagebox
from Utils import lib as l
from Utils import generic as g
import GameController


class Cell:
    def __init__(self, x: int, y: int, frame: tk.Frame):
        self.__value = 0
        self.__revealed = False
        self.__flagged = False
        self.__x = x
        self.__y = y
        self.__frame = frame
        self.__defineCellBehavior()
        self.__adjacentCell = []

    def __defineCellBehavior(self):
        self.__button = tk.Button(self.__frame, text="", width=3, height=1, font=("Helvetica", 11, "bold"),
                                  relief=tk.RAISED)
        self.__button.grid(row=self.__x, column=self.__y)
        self.__button.bind("<Button-1>", lambda e: self.__onLeftClick())
        self.__button.bind("<Button-3>", lambda e: self.__onRightClick())

    def revealCell(self):
        self.__revealed = True
        if self.__value == -1:
            self.__button.config(state="disabled", relief=tk.SUNKEN, bg="light grey", text=str(g.bomb))
            return
        elif self.__value == 0:
            self.__button.config(state="disabled", relief=tk.SUNKEN, bg="light grey", text="")
        else:
            self.__button.config(state="disabled", relief=tk.SUNKEN, bg="light grey", text=str(self.__value))

        g.revealedCellsGlobal += 1
        g.gameController.updateCellsLabel()
        if g.gameController.checkWin():
            self.win()

    def __revealAdjacentCell(self):
        self.revealCell()
        for cell in self.__adjacentCell:
            cell.__onLeftClick()

    def lose(self):
        g.boardGlobal.revealBombs()
        l.createEscapeRoot("Hai Perso :(")
        return True

    def win(self):
        l.createEscapeRoot("Hai Vinto :)")
        return True

    def __unFlagCell(self):
        self.__button.config(text="", state="normal")
        self.__flagged = False

    def __flagCell(self):
        self.__flagged = True
        self.__button.config(text=g.redFlag, state="disabled")

    def __onLeftClick(self):
        if g.endGame:
            return
        if g.revealedCellsGlobal == 0:
            g.timer.start_timer()
            g.boardGlobal.initializeBoard(self)
        if self.__flagged or self.__revealed:
            return
        elif g.gameController.checkLose(self.__value):
            self.lose()
        elif self.__value == 0:
            self.__revealAdjacentCell()
        else:
            self.revealCell()

    def __onRightClick(self):
        if g.endGame:
            return
        if self.__revealed:
            return
        elif self.__flagged == False:
            self.__flagCell()
        else:
            self.__unFlagCell()

    def printCell(self):
        print(f"""Bottone {self.__x, self.__y}: {self.__value}""")

    @property
    def x(self) -> int:
        return self.__x

    @property
    def adjacentCell(self):
        return self.__adjacentCell

    @property
    def y(self) -> int:
        return self.__y

    @property
    def button(self) -> tk.Button:
        return self.__button

    @property
    def value(self) -> int:
        return self.__value

    @property
    def revealed(self) -> bool:
        return self.__revealed

    @property
    def flagged(self) -> bool:
        return self.__flagged

    @button.setter
    def button(self, x: tk.Button):
        self.__button = x

    @value.setter
    def value(self, x: int):
        self.__value = x

    @revealed.setter
    def revealed(self, x: bool):
        self.__revealed = x

    @flagged.setter
    def flagged(self, x: bool):
        self.__flagged = x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, x: int):
        self.__y = x