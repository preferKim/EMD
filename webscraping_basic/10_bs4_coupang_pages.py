# 쿠팡에서 1페이지부터 5페이지까지 돌면서 스크래핑
import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}


# 사람이 접속하는 것처럼 헤더를 위장



for i in range(1, 5 + 1):
    print("페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

    for item in items:
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            print("<광고상품은 제외합니다>")
            continue        
            
        name = item.find("div", attrs={"class": "name"}).get_text()  # 제품명
        
        # 애플 제품 제외:
        if "Apple" in name:
            # print(" <Apple 제품 제외합니다>")
            continue
        
        price = item.find(
            "strong", attrs={"class": "price-value"}).get_text()  # 가격
        
        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class": "rating"})  # 평점
        if rate:  # rate가 없는 상품도 있으므로
            rate = rate.get_text()
        else:
            # print(" <평점없는 상품 제외합니다>")
            continue
        
        rate_count = item.find("span", attrs={"class": "rating-total-count"})  # 평점
        if rate_count:  # rate가 없는 상품도 있으므로
            rate_count = rate_count.get_text()[1:-1] # 예: (26)
        else:
            #print(" <평점 갯수 없는 상품 제외합니다>")
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]    
        
        if float(rate) >= 4.5 and int(rate_count) > 50:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_count})개")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100) # 줄 긋기