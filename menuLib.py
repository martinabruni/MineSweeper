import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
import cv2
# import Settings
from PIL import Image, ImageTk
from config import*

def open_second_module(frame, btn):
    btn.config(bg="white", fg="gray")
    frame.destroy()
    # Settings.run_module(root)  
    

    
   
def create_button(frame,text, command):
    return tk.Button(frame, text=text, width=button_width, height=button_height, bg="gray", fg="white", command=command)
   


    
    #IMMAGINE

def set_image():
    image = cv2.imread(image_path)
    image = cv2.resize(image, (150, 150))  
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(image))

    return photo


def set_Frame(root, frame):
    frame = tk.Frame(root, bg="black", bd=5, relief="groove")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

def fill_Frame(frame):
    image = set_image()
    #IMMMAGINE 
    image_label = tk.Label(frame, image=image, bg="black")
    image_label.place(relx=0.5, rely=0.2, anchor='center')

    #TITOLO
    
    custom_font = tkFont.Font(family="Terminal", size=75)

    label = tk.Label(frame, text=" CAMPO MINATO",font=custom_font,fg="white", bg="black")
    label.place(relx=0.5, rely=0.4, anchor='center')

    #BUTTON

    buttonStart = create_button(frame,"Start", lambda: on_buttonStart_click(frame, buttonStart))
    buttonStart.place(relx=0.5, rely=0.6, anchor='center')

    buttonSettings =create_button(frame,"Settings", lambda: on_buttonStart_click(frame, buttonSettings))
    buttonSettings.place(relx=0.5, rely=0.7, anchor='center')



    

    



