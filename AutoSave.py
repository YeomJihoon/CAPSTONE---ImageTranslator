import numpy as np
import cv2
import pytesseract

# 1~100 반복

for i in range(1, 101):
    si = str(i)
    file = "F:\\Users\\BRA\\Desktop\\Graduate\\src\\" + si + ".jpg" # 파일이름 지정
    image = cv2.imread(file, 1) # 이미지 RGB 색상 맞게 불러옴

    config = r'-l eng --psm 4'

    from pytesseract import Output
    d = pytesseract.image_to_data(image, output_type=Output.DICT, config=config)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        if(d['text'][i] != ""):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)  # 검출된 텍스트 영역에 박스

    text = pytesseract.image_to_string(image, config = config) # 검출된 텍스트

    f = open("F:\\Users\\BRA\\Desktop\\Graduate\\Result\\" + si + ".txt", 'w', -1, "utf-8")
    f.write(text)
    f.close() # 텍스트파일로 저장

    cv2.imwrite("F:\\Users\\BRA\\Desktop\\Graduate\\Result\\" + si + ".jpg", image)

print("END")
