import re
# 차량번호, abcd, book, desk
# ca?e 
# care, cafe, case, cave
# caae, cabe, cace, ...

p = re.compile("ca.e") # p: pattern, 
# '.' (ca.e): 하나의 문자를의미 (정상)care, cafe | caffe(에러)
# ^ (^de): 문자열의 시작 >desk, destination (O) | fade(X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)

# m = p.match("caffe")
# print(m.group()) # 매치되지 않으면 에러가 발생
def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")
        
m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)