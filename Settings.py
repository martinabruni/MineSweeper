import tkinter as tk
import tkinter.font as tkFont
import cv2
# import Settings
from PIL import Image, ImageTk
import menuLib as mL
from globals import *


class Settings:
    def __init__(self, root, frame):
        self.__root = root
        self.__frame = frame
        self.run_model()

    @property
    def root(self):
        return self.__root

    @property
    def frame(self):
        return self.__frame

    def run_model(self, root):
        def set_image():
            image = cv2.imread(imageSettings)
            image = cv2.resize(image, (150, 150))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            photo = ImageTk.PhotoImage(image=Image.fromarray(image))

            return photo

        mL.set_Frame(root, frame)

        def fill_Frame(self):
            image = set_image()
            # IMMMAGINE
            image_label = tk.Label(self.__frame, image=image, bg="black")
            image_label.place(relx=0.5, rely=0.2, anchor='center')

            # TITOLO

            custom_font = tkFont.Font(family="Terminal", size=25)

            label = tk.Label(self.__frame, text=" SETTINGS", font=custom_font, fg="white", bg="black")
            label.place(relx=0.5, rely=0.4, anchor='center')

            # BUTTON

            buttonSave = mL.createButton(self.__frame, "Save", open_second_module(self.__frame, buttonSave))
            buttonSave.place(relx=0.5, rely=0.7, anchor='center')
