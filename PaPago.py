import os
import sys
import urllib.request
client_id = "p8nQmLg0xZAfuG5Y1OyB"
client_secret = "BbIxxp0QES"

file = "c:\example-english.txt"  # 파일지정
f = open(file,'r',-1,'utf-8')    # UTF-8 파일임을 명시
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
