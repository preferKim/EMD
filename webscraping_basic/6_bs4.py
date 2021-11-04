# 네이버웹툰 
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()


# res.text를 lxml로 parsing 후, BeautifulSoup객체로 만들어 soup에 저장
soup = BeautifulSoup(res.text, "lxml") 

### 페이지에 대한 자체 이해도가 높을 때 
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup객체에서 처음 발견되는 a element 출력 
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href 속성 '값' 정보를 출력

### 웹 페이지를 잘 모를때

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))  # class ="Nbtn_upload" 인 a element를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class ="Nbtn_upload" 인 어떤 element를 찾아줘
# rank1 = soup.find("li", attrs={"class":"rank01"}) # class = "rank01"인 li 태그를 찾아줘
# print(rank1.a) # 'rank1'객체에서 a태그에 대한 정보만 출력
#print(rank1.a.get_text())
#print(rank1.next_sibling) # 태그 사이에 개행정보가 있어서 출력이 안됨
#print(rank1.next_sibling.next_sibling) # 한 번더 next sibling
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# # print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # 개행정보 때문
# print(rank2.a.get_text())
# # print(rank1.parent)
# rank2 = rank1.find_next_sibling("li") # 'li'인 다음 시블링만 찾음, 개행상관없음
# # print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# # print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2)

# ranks = rank1.find_next_siblings("li") # rank1 기준 li 형제들 가져옴
# print(ranks)

# text="나노마신-073. 제29장. 주군이 돌아왔다" 인 a 태그 가져옴
webtoon = soup.find("a", text="나노마신-073")
print(webtoon)
