import tkinter as tk
import menuLib as mL
import tkinter.font as tkFont
from tkinter import PhotoImage
import cv2
# import Settings
from PIL import Image, ImageTk
from config import*

class Menu:
   
   def __init__(self, frame,root):
     self.__frame= frame
     self.__root= root
     
   @property
   def root(self):
     return self.__root
   
   @property
   def frame(self):
     return self.__frame
     
   def set_root(self):
    self.__root.title("Campo Minato")
    self.__root.geometry("1500x800")

    self.__root.configure(bg="black")
    
    #IMMAGINE

    def set_image():
        image = cv2.imread(image_path)
        image = cv2.resize(image, (150, 150))  
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(image))

        return photo
    
   
     
    
   
    

