from tkinter import *
from PIL import ImageTk, Image
import os

class screen_viewer():
    def __init__(self, tk_frame: Frame(), img_path: str):
        self.img_path = img_path
        self.img_list = []
    
    def open_files(self):
        for file in os.listdir(self.img_path):
            self.img_list.append(ImageTk.PhotoImage(Image.open(self.img_path+file)))
        print(self.img_list)

root = Tk()
my_viewer = screen_viewer(root, "img_dir/")
my_viewer.open_files()

root.mainloop() 