import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import time

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

driver = webdriver.Chrome()
url = "https://google.com"
# url = 'https://accounts.google.com/signin/v2/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
driver.get(url)
# driver.maximize_window()
action = ActionChains(driver) # action을 통해 driver제어

### 로그인
# 로그인 버튼 클릭
# driver.find_element(By.CLASS_NAME, "gb_3.gb_4.gb_3d.gb_ja.gb_3c").click()
driver.find_element_by_css_selector(".gb_Me").click()

# 구글 아이디 입력
action.send_keys("mycruel4@dgu.ac.kr").perform()

# '다음' 버튼 클릭
driver.find_element_by_css_selector('.VfPpkd-dgl2Hf-ppHlrf-sM5MNb').click()
time.sleep(2)

# 비밀번호 입력
driver.find_element_by_css_selector(".whsOnd.zHQkBf").send_keys("유저 패스워드")

# 다음 버튼 클릭
driver.find_element_by_css_selector('.VfPpkd-dgl2Hf-ppHlrf-sM5MNb').click()

# Gmail로 이동
time.sleep(2)
driver.get("https://mail.google.com/mail/u/0/#inbox")
time.sleep(3)

# 메일 제목만 가져와서 출력
titles = driver.find_elements_by_css_selector(".bog")
for title in titles:
    print(title.text)

