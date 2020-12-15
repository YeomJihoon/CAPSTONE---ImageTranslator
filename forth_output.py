import cv2
import tkinter
import tkinter.filedialog
import os
import sys
import pytesseract
import urllib.request
import numpy
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract'
client_id = "p8nQmLg0xZAfuG5Y1OyB"
client_secret = "BbIxxp0QES"


# Image Loader

def load():
    f = open("filename.txt", 'r',-1,'utf-8')
    route = f.readline()       # 현재 route.txt 에 저장된 경로를 읽음
    filename = filedialog.askopenfilename(initialdir=route, title = "Select Image File",
                                          filetypes=(("jpg files", "*.jpg"), ("gif files", "*.gif"), ("bmp files", "*.bmp"),
                                         ("png files", "*.png"), ("webp files", "*.webp")))  # 이미지불러오기(현재 확장자 5종지원)
    
    f = open("filename.txt", 'w',-1,'utf-8')
    f.write(filename)
    f.close()   # route.txt 에 최근 파일 경로를 덮어씌움. 프로그램 종료할 때 지워짐
   
    file_enc = open(filename.encode("utf-8"), "rb")
    byteA = bytearray(file_enc.read())
    npArr = numpy.asarray(byteA, dtype=numpy.uint8)   # 경로 변환

    image = cv2.imdecode(npArr, cv2.IMREAD_UNCHANGED)
    
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

    nameEntry = tkinter.Entry(main, width = 100)
    nameEntry.insert(0,filename)
    nameEntry.place(x = 100, y = 41)  # 경로 글자로 표시
    
# Tesseract
def tes():
    f = open("filename.txt",'r',-1,'utf-8')
    route = f.readline()
    f.close()                       # 파일 불러옴
    
    route_enc = open(route.encode("utf-8"), "rb")
    byteA = bytearray(route_enc.read())
    npArr = numpy.asarray(byteA, dtype=numpy.uint8)   # 경로 변환

    Tesimage = cv2.imdecode(npArr, cv2.IMREAD_UNCHANGED)

    color_cvt = cv2.cvtColor(Tesimage, cv2.COLOR_BGR2RGB)  # 컬러 변환

    temp_file = "{}.png".format(os.getpid())
    cv2.imwrite(temp_file, color_cvt)   # 임시 이미지 파일 생성

    text = pytesseract.image_to_string(Image.open(route))  # 텍스트 tesseract로 검출
    os.remove(temp_file)                                      # 임시 이미지 파일 제거

    f = open("searchtext.txt", 'w', -1, "utf-8")
    f.write(text)
    f.close()     # 검출한 텍스트 저장
    
# Translator
def tl():
    tes()
    f = open("searchtext.txt", 'r', -1, "utf-8")
    text = f.read()
    f.close()

    encQuery = urllib.parse.quote(text)
    data = "query=" + encQuery
    url = "https://openapi.naver.com/v1/papago/detectLangs"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    lang = response_body.decode('utf-8')  # 탐지한 언어
    lang = lang[13:]           # 앞문자 자르기
    lang = lang[:-2]           # 뒷문자 자르기

    encText = urllib.parse.quote(text)
    data = "source=" + lang + "&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    dec = response_body.decode('utf-8')
    translatedText = dec[dec.find('"translatedText"')+18:dec.find('"engineType"')-2] # 번역문만 잘라냄

    f = open("translatetext.txt", 'w', -1, "utf-8")
    f.write(translatedText)
    f.close()

# Output
def out():
    tl()
    f1 = open("searchtext.txt", 'r', -1, "utf-8")

    f2 = open("translatetext.txt", 'r', -1, "utf-8")
    t2 = f2.read()

    t2copy = t2.replace("\\n", "\n")  # 문자열 수정
    f2.close()
    f2 = open("translatetext.txt", 'w', -1, "utf-8")
    f2.write(t2copy)
    f2.close()

    f2 = open("translatetext.txt", 'r', -1, "utf-8")  # 원문, 번역문 파일 불러오기

    
    outframe = tkinter.Frame(main)
    scrbar = tkinter.Scrollbar(outframe)
    scrbar.pack(side = "right", fill = "y")
    outbox = tkinter.Text(outframe, width = 68, height = 50, yscrollcommand = scrbar.set) # 프레임, 텍스트박스, 스크롤바
    
    while True:
        line = f1.readline()
        if not line: break
        outbox.insert(tkinter.CURRENT, line)
        line = f2.readline()
        if not line: break
        outbox.insert(tkinter.CURRENT, "\n-> ")
        outbox.insert(tkinter.CURRENT, line)
        outbox.insert(tkinter.CURRENT, "\n")      # 텍스트박스에 출력
        
    f1.close()
    f2.close()

    outbox.pack(side="left")

    scrbar["command"] = outbox.yview

    outframe.pack(side="right")  

    outframe.place(x = 526, y = 90)     # 위젯 위치 조정
    
    
    
# Main Program

f = open("filename.txt", 'w',-1,'utf-8')
data = "/"
f.write(data)
f.close()                     # 경로저장파일 route.txt -> 프로그램 실행시 리셋

main = tkinter.Tk()
main.title("Leona IMG Translator") # 타이틀
main.geometry("1024x768")          # 창 크기 1024x768
main.resizable(width=0,height=0)   # 창 크기 조절 불가능

nameLabel = tkinter.Label(main, text = "이미지 경로")
nameButton = tkinter.Button(main, text = "불러오기", width = 11, height = 3, command = load)
transButton = tkinter.Button(main, text = "번역", width = 11, height = 3, command = out)   # 상단 위젯

nameLabel.place(x = 20, y = 40)
nameButton.place(x = 820, y = 20)
transButton.place(x = 920, y = 20) # 위젯 위치조정

main.mainloop() # 닫지 않는 이상 유지
