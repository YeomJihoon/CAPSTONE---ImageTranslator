import cv2
import tkinter
import tkinter.filedialog
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# Image Loader

def load():
    f = open("recent.txt", 'r')
    route = f.readline()       # 현재 route.txt 에 저장된 경로를 읽음
    filename = filedialog.askopenfilename(initialdir=route, title = "Select Image File",
                                          filetypes=(("jpg files", "*.jpg"), ("gif files", "*.gif"), ("bmp files", "*.bmp"),
                                         ("png files", "*.png"), ("webp files", "*.webp")))  # 이미지불러오기(현재 확장자 5종지원)
    
    f = open("recent.txt", 'w')
    f.write(filename)
    f.close()   # route.txt 에 최근 파일 경로를 덮어씌움. 프로그램 종료할 때 지워짐
   
    image = cv2.imread(filename)
    imginfo = image.shape
    widthrate = imginfo[1]/482
    heightrate = imginfo[0]/650
    
    imgcvt = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    if (widthrate > heightrate):
        resizerate = widthrate
    else:
        resizerate = heightrate

    imgcvt = cv2.resize(imgcvt, dsize = (0,0), fx = (1/resizerate), fy = (1/resizerate), interpolation = cv2.INTER_LINEAR)
    imgcvt = Image.fromarray(imgcvt)
    imgtk = ImageTk.PhotoImage(image = imgcvt)  # 이미지 표시 준비(크기 및 채널 조정)

    imglabel = tkinter.Label(main, image = imgtk, width = 482, height = 650)
    imglabel.image = imgtk
    imglabel.place(x = 20, y = 88)    # 이미지 표시    

    
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

f = open("recent.txt", 'w')
data = "/"
f.write(data)
f.close()                     # 경로저장파일 route.txt -> 프로그램 실행시 리셋

main = tkinter.Tk()
main.title("Leona IMG Translator") # 타이틀
main.geometry("1024x768")          # 창 크기 1024x768
main.resizable(width=0,height=0)   # 창 크기 조절 불가능

nameLabel = tkinter.Label(main, text = "이미지 경로")
nameEntry = tkinter.Entry(main, width = 100, state = "readonly")
nameButton = tkinter.Button(main, text = "불러오기", width = 11, height = 3, command = load)
transButton = tkinter.Button(main, text = "번역", width = 11, height = 3, command = out)   # 상단 위젯

transBox = tkinter.Text(main, width = 68, height = 50)           # 번역결과물 위젯

nameLabel.place(x = 20, y = 40)
nameEntry.place(x = 100, y = 41)
nameButton.place(x = 820, y = 20)
transButton.place(x = 920, y = 20)
transBox.place(x = 522, y = 88)   # 위젯 위치조정

main.mainloop() # 닫지 않는 이상 유지
