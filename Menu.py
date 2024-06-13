import tkinter as tk
import menuLib as mL
import tkinter.font as tkFont
from tkinter import Menubutton, PhotoImage
import cv2
# import Settings
from PIL import Image, ImageTk
from config import*
import Settings

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
        
   
   def set_Frame(root, frame):
        frame = tk.Frame(root, bg="black", bd=5, relief="groove")
        frame.pack(fill="both", expand=True, padx=10, pady=10)
   
   def open_second_module(self, btn):
        btn.config(bg="white", fg="gray")
        self.__frame.destroy()
        Settings.run_module(self.__root)  
    
    #IMMAGINE

   def set_image():
        image = cv2.imread(image_path)
        image = cv2.resize(image, (150, 150))  
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(image))
        return photo
    
   mL.set_Frame(root,frame)
    
   def fill_Frame(self):
        image = Menu.set_image()
     #IMMMAGINE 
        image_label = tk.Label(self.__frame, image=image, bg="black")
        image_label.place(relx=0.5, rely=0.2, anchor='center')

    #TITOLO
    
        custom_font = tkFont.Font(family="Terminal", size=75)
        label = tk.Label(self.__frame, text=" CAMPO MINATO",font=custom_font,fg="white", bg="black")
        label.place(relx=0.5, rely=0.4, anchor='center')

    #BUTTON

        buttonStart = mL.create_button(self.__frame,"Start", on_buttonStart_click(self.__frame, buttonStart))
        buttonStart.place(relx=0.5, rely=0.6, anchor='center')

        buttonSettings =mL.create_button(self.__frame,"Settings",Menu.open_second_module(self.__frame, buttonSettings))
        buttonSettings.place(relx=0.5, rely=0.7, anchor='center')

    
   
     
    
   
    

