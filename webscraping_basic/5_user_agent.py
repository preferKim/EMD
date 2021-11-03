# user agent string 검색 -> what is my user agent .com 
# 접속 브라우저에 따라 User Agent 가 다름 
import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

res = requests.get(url, headers=headers) # 헤더를 'headers'로 넘김 
res.raise_for_status() # 문제 생겼을 때 바로 오류 발생시키고 종류
with open("mygithub.html", "w", encoding="utf8") as f:
    f.write(res.text)
