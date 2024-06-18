import tkinter as tk
import tkinter.font as tkFont
import cv2

from PIL import Image, ImageTk
from Utils import generic
class Frame:

    def __init__(self, sizeTitle, textTitle, imagePath):
        self.__sizeTitle = sizeTitle
        self.__textTitle = textTitle
        self.__image = imagePath


    def initializeMenu(self):
        self.setFrame()
        self.setTitle()
        self.setImage()

    def setFrame(self):
        generic.frameGlobal = tk.Frame(generic.rootGlobal, bg="black", bd=5, relief="groove")
        generic.frameGlobal.pack(fill="both", expand=True, padx=10, pady=10)

    def setTitle(self):
        customFont = tkFont.Font(family="Terminal", size=self.__sizeTitle)
        label = tk.Label(generic.frameGlobal, text=self.__textTitle, font=customFont, fg="white", bg="black")
        label.place(relx=0.5, rely=0.4, anchor='center')

    def setImage(self):
        image = cv2.imread(self.__image)
        image = cv2.resize(image, (150, 150))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.__image = ImageTk.PhotoImage(image=Image.fromarray(image))
        imageLabel = tk.Label(generic.frameGlobal, image=self.__image, bg="black")
        imageLabel.place(relx=0.5, rely=0.2, anchor='center')


if __name__ == "__main__":
    root = tk.Tk()
    # setRootFullScreen(root)
    frame_instance = Frame(root, 20, "Titolo del Gioco", "Assets/icona.png")
    frame_instance.initializeMenu()
    root.mainloop()
