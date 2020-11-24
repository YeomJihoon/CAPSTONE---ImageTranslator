from tkinter import filedialog
import tkinter
import cv2
from PIL import Image, ImageTk


loader = tkinter.Tk()

def load(route):
    filename = filedialog.askopenfilename(initialdir=route, title = "select file")
    
    return filename

route = "/"     # 첫 켰을 때 기본경로 값 없음

name = load(route)
route_split = name.split("/")
del route_split[-1]
route = "/".join(route_split)  # 켜진 상태에서 다시 로드할 때 전 이미지와 같은 경로에서 시작

image = Image.open(name)

img_hor = image.size[0]
img_ver = image.size[1]
if ((img_hor/1024) > (img_ver/768)):
    rate = img_hor/1024
else:
    rate = img_ver/768               # 사이즈 변경을 위한 비율정하

resizing = image.resize((int(img_hor/rate),int(img_ver/rate)))  # 이미지 크기 변경

outimage = ImageTk.PhotoImage(resizing)
label = tkinter.Label(loader, image = outimage, width = 1024, height = 768)
label.pack()  # 크기 변경된 이미지를 출력

loader.mainloop()
