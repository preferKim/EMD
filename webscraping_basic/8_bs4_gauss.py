import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# soup 객체에서 td태그 중 class가 title인 값을 cartoons에 저장
cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[1].a.get_text() # cartoons[1] 에서 텍스트 추출
# link = "https://comic.naver.com/" + cartoons[1].a["href"]
# print(title,link)

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com"+ cartoon.a["href"]
    print(title, link)