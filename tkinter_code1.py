from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code")

my_img = ImageTk.PhotoImage(Image.open("img.png"))
myLabel = Label(image=my_img).pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()
root.mainloop()