from selenium import webdriver
from bs4 import BeautifulSoup
import time

# -------------------------------1. 웹 페이지 접근
# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3)

for page_no in range(1, 11):

    driver.get('https://pelicana.co.kr/store/stroe_search.html?page=%d')
    html = driver.page_source
    # print(html)

    time.sleep(5)

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('#mt20 tr.td')
    for head in title:
        namePath = head.attrs['data-original']
        num = head.attrs['alt'].strip().replace('/', '_')
        print(namePath, num)
# 매장명 - 전화번호
