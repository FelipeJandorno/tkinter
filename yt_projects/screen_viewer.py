from tkinter import *
from PIL import ImageTk, Image
import os

class screen_viewer():
    def __init__(self, tk_frame, img_path: str):
        self.tk_frame = tk_frame
        self.img_list = []
        self.n_file = 0
        self.this_img = None
        self.img_path = img_path

        # Creating Screen Viewer
        self.Save_Files(self.img_path)
        self.Buttons()
    
    def Save_Files(self, img_path: str):
        for file in os.listdir(img_path):
            self.img_list.append(ImageTk.PhotoImage(Image.open(img_path+"/"+file)))
        print(self.img_list)
    
    def Open_files(self):
        try:
            if self.img_list == []:
                Label(self.tk_frame, text="There is no image uploaded!").grid(row=0, column=1, columnspan=5)
            else:
                Label(self.tk_frame, image=self.img_list[self.n_file]).grid(row=0, column=1, columnspan=5)
                Label(self.tk_frame, text=self.n_file).grid(row=2, column=0)
        except IndexError:
            self.n_file = 0
            Label(self.tk_frame, image=self.img_list[self.n_file]).grid(row=0, column=1, columnspan=5)
            Label(self.tk_frame, text=self.n_file).grid(row=2, column=0)
            
    def OnButtonNextClick(self):
        self.n_file = self.n_file + 1
        self.Open_files()
    
    def OnButtonBackClick(self):
        self.n_file = self.n_file - 1
        self.Open_files()
        
    def OnButtonExitClick(self):
        self.tk_frame.destroy()
    
    def Buttons(self):
        if self.img_list == []:
            button_next = Button(self.tk_frame, text="Next", width=20, command=self.OnButtonNextClick, state=DISABLED).grid(row=1, column=0)
            button_back = Button(self.tk_frame, text="Back", width=20, command=self.OnButtonBackClick, state=DISABLED).grid(row=1, column=2)
            button_exit = Button(self.tk_frame, text="Exit", width=20, command=self.OnButtonExitClick, state=ACTIVE).grid(row=1, column=4)
        else:
            button_next = Button(self.tk_frame, text="Next", width=20, command=self.OnButtonNextClick, state=ACTIVE).grid(row=1, column=1, ipadx=50)
            button_back = Button(self.tk_frame, text="Back", width=20, command=self.OnButtonBackClick, state=ACTIVE).grid(row=1, column=3, ipadx=50)
            button_exit = Button(self.tk_frame, text="Exit", width=20, command=self.OnButtonExitClick, state=ACTIVE).grid(row=1, column=4, ipadx=50)
        


# Creating Tkinter Screen
root = Tk()
root.geometry("720x500")
root.title("Screen Viewer")

# Creating Viewer
my_viewer = screen_viewer(root, r"D:\felipe\github\tkinter\yt_projects\img_dir")
my_viewer.Open_files()

root.mainloop() 
