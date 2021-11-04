# 리뷰가 높고 평점이 좋은 노트북을 검색, 광고는 거름
import requests
import re
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
# 사람이 접속하는 것처럼 헤더를 위장
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}))
# soup = BeautifulSoup(res)
# items에서 이름과 가격 출력
count = 0
for item in items:
    # 광고 제품은 제외 
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("<광고상품은 제외합니다>")
        continue        
        
    name = item.find("div", attrs={"class": "name"}).get_text()  # 제품명
    
    # 애플 제품 제외:
    if "Apple" in name:
        print(" <Apple 제품 제외합니다>")
        continue
    
    price = item.find(
        "strong", attrs={"class": "price-value"}).get_text()  # 가격
    
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class": "rating"})  # 평점
    if rate:  # rate가 없는 상품도 있으므로
        rate = rate.get_text()
    else:
        print(" <평점없는 상품 제외합니다>")
        continue
    
    rate_count = item.find("span", attrs={"class": "rating-total-count"})  # 평점
    if rate_count:  # rate가 없는 상품도 있으므로
        rate_count = rate_count.get_text() # 예: (26)
        rate_count = rate_count[1:-1]
    else:
        print(" <평점 갯수 없는 상품 제외합니다>")
        continue
    
    if float(rate) >= 4.5 and int(rate_count) > 1000:
        print(name, price, rate, rate_count, sep=" | ")
    count += 1
print(count)


