

import tkinter as tk
import tkinter.font as tkFont
import cv2

from PIL import Image, ImageTk

class Frame:
    
    def __init__(self, root, sizeTitle, textTitle,frameImage):
        self.__root = root
        
        self.__sizeTitle=sizeTitle
        self.__textTitle=textTitle
        self.__frameImage=frameImage
        self.__image = None
        
        self.__frame = tk.Frame(self.__root)
        self.setFrame()
        self.setTitle()
        self.setImage()
      
        
    @property
    def root(self):
        return self.__root

    @property
    def frame(self):
        return self.__frame
    
    def setFrame(self):
        self.__frame = tk.Frame(self.__root, bg="black", bd=5, relief="groove")
        self.__frame.pack(fill="both", expand=True, padx=10, pady=10)
        
    def setTitle(self):
        customFont = tkFont.Font(family="Terminal", size=self.__sizeTitle)
        label = tk.Label(self.__frame, text=self.__textTitle, font=customFont, fg="white", bg="black")
        label.place(relx=0.5, rely=0.4, anchor='center')
    
    def setImage(self):
        image = cv2.imread(self.__frameImage)
        image = cv2.resize(image, (150, 150))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.image = ImageTk.PhotoImage(image=Image.fromarray(image))
        
        imageLabel = tk.Label(self.__frame, image=self.image, bg="black")
        imageLabel.place(relx=0.5, rely=0.2, anchor='center')


if __name__ == "__main__":
    
    root = tk.Tk()
    setRootFullScreen(root)
    frame_instance = Frame(root, 20, "Titolo del Gioco", "Assets/icona.png")
    
    root.mainloop()




