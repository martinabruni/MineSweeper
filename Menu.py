import tkinter as tk
import menuLib as mL
import tkinter.font as tkFont
from tkinter import Menubutton, PhotoImage
import cv2
from PIL import Image, ImageTk
from config import*
from Settings import Settings

class Menu:
   
   def __init__(self, root,frame):
       self.__frame= frame
       self.__root= root
       self.__buttonStar=None
       self.__buttonSettings=None
       self.set_root()
       self.set_Frame()
       self.fill_Frame()
   
   @property
   def started(self):
       return self.__started 

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
        
   
   def set_Frame(self):
        self.__frame = tk.Frame(self.__root, bg="black", bd=5, relief="groove")
        self.__frame.pack(fill="both", expand=True, padx=10, pady=10)
   
   def open_second_module(self):
        self.__buttonSettings.config(bg="white", fg="gray")
        self.__frame.destroy()
        Settings.run_module(self.__root)
        
   def open_game(self):
        self.__buttonStart.config(bg="white", fg="gray")
        self.__frame.destroy()
        MineSweeperUI(self.__root).createBoard()
   
   #IMMAGINE
   def set_image(self):
        image = cv2.imread(image_path)
        image = cv2.resize(image, (150, 150))  
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(image))
        return photo
   

   def fill_Frame(self):
        
        # image = self.set_image()
        # image_label = tk.Label(self.__frame, image=image, bg="black")
        # image_label.place(relx=0.5, rely=0.2, anchor='center')

    #TITOLO
    
        custom_font = tkFont.Font(family="Terminal", size=75)
        label = tk.Label(self.__frame, text=" CAMPO MINATO",font=custom_font,fg="white", bg="black")
        label.place(relx=0.5, rely=0.4, anchor='center')

    #BUTTON

        self.__buttonStart = tk.Button(self.__frame,text="Start",width=10, height=2, bg="gray", fg="white", command=self.open_game)
        self.__buttonStart.place(relx=0.5, rely=0.6, anchor='center')

        self.__buttonSettings =tk.Button(self.__frame,text="Settings",width=10, height=2, bg="gray", fg="white", command= self.open_second_module)
        self.__buttonSettings.place(relx=0.5, rely=0.7, anchor='center')

    
   
     
    
   
    

