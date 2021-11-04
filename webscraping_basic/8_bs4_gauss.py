# 구글에 beautifulsoup 쳐서 레퍼런스 확인
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# soup 객체에서 td태그 중 class가 title인 값을 cartoons에 저장
# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[1].a.get_text() # cartoons[1] 에서 텍스트 추출
# link = "https://comic.naver.com/" + cartoons[1].a["href"]
# print(title,link)

# 만화제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com"+ cartoon.a["href"]
#     print(title, link)

# 평점 구하기
cartoons = soup.find_all("div", attrs={"class": "rating_type"})
# rate = cartoons[2].strong.get_text()
# print(rate)
total_rates = 0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)  # rate 현재 string type
print("전체점수 :", total_rates)
print("평균점수 : ", total_rates / len(cartoons))
