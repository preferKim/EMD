import time
from selenium import webdriver

# 브라우저 객체 생성
browser = webdriver.Chrome("./chromedriver.exe")

# 1. 네이버 이동
browser.get("http://naver.com") 

# 2. 로그인 이동
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()


time.sleep(3)

# 5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")


### 브라우저 조작
# elem = browser.find_element_by_class_name("link_login")
# elem.click()
# browser.back()
# browser.forward()
# browser.refresh()
# elem = browser.find_element_by_id("query")

# from selenium.webdriver.common.keys import Keys
# elem.send_keys("나도 코딩")
# elem.send_keys(Keys.ENTER)

# elem = broswer.find_element_by_tag_name("a")
# elem = broswer.find_elements_by_tag_name("a")