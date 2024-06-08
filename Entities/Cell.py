import tkinter as tk


class Cell:
    def __init__(self, x, y):
        self.__button = None
        self.__value = 0
        self.__revealed = False
        self.__flagged = False
        self.__x = x
        self.__y = y

    def __defineCellBehavior(self):
        """Qui dovra' essere implementata lo logica del bottone"""
        pass

    def __revealCell(self):
        pass

    def __flagCell(self):
        pass

    def __updateCellStyle(self):
        pass

    def __updateCellText(self):
        pass

    def __onLeftClick(self):
        pass

    def __onRightClick(self):
        pass

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
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
