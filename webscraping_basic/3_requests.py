import requests
# res = requests.get("http://naver.com")
res = requests.get("http://google.com")
res.raise_for_status() # 문제 생겼을 때 바로 오류 발생시키고 종류
# res = requests.get("https://github.com/Balparang")
print("응답코드 :", res.status_code) # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     pritn("ans")

print(len(res.text))
print(res.text) # 긁어옴
# 파일로 만들어서보기
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
