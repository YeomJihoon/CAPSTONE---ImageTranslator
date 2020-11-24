from tkinter import filedialog
import tkinter
import cv2
from PIL import Image, ImageTk


loader = tkinter.Tk()

def load():
    filename = filedialog.askopenfilename(initialdir="/", title = "select file")
    return filename

name = load()
image = ImageTk.PhotoImage(Image.open(name))

label = tkinter.Label(loader, image = image)
label.pack()

loader.mainloop()
