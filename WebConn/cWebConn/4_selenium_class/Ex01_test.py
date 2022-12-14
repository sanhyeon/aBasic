"""
 간단하게 크롬 브라우저를 실행하여 페이지 열기
"""
from selenium import webdriver

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)

# 2. 페이지 접근
driver.get('https://www.naver.com')

# 3. 화면을 캡처해서 저장하기
driver.save.screenshot("naver2.png")
