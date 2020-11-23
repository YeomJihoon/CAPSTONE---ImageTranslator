import tkinter
import tkinter.filedialog
from tkinter import *

# Image Load

def imgload():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Load Image File",
                      filetypes=(("jpg files", "*.jpg"), ("gif files", "*.gif"), ("bmp files", "*.bmp"),
                                 ("png files", "*.png"), ("webp files", "*.webp"))) # GUI 인터페이스로 파일부르기
    print(filename)
    

# Tesseract
def tes():
    print("TES")

# OCR
def ocr():
    tes()
    print("OCR")


# Translator
def tl():
    ocr()
    print("TRANSLATOR")

# Output
def out():
    tl()
    print("OUTPUT")

# Main Program

root = tkinter.Tk()
root.title("Leona IMG Translator")
root.geometry('1024x768')
root.resizable(width=0,height=0)  # 메인프로그램 창 조정


namelbl = tkinter.Label(root, text = "이미지 경로")
nameent = tkinter.Entry(root, width = 100)
namebtn = tkinter.Button(root, text = "불러오기", width = 11, height = 3, command = imgload)
transbtn = tkinter.Button(root, text = "번역", width = 11, height = 3, command = out)

result = tkinter.Text(root, width = 68, height = 50, bg = "WHITE")

# 필요한 내부 위젯

namelbl.place(x=20,y=40)
nameent.place(x=100,y=41)
namebtn.place(x=820,y=20)
transbtn.place(x=920,y=20)

result.place(x=526,y=90)

root.mainloop() # 닫기 누르지 않는 이상 유지
