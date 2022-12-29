from selenium import webdriver
from bs4 import BeautifulSoup
import time
import folium

# (1) 페이지에서 매장명, 전화번호, 주소 추출

# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(5)

f = open('location.txt', 'w')
f.write('지점명, 전화번호, 주소, 위도, 경도\n')


# 페이지 수 만큼 돌림
for page_no in range(1, 154):

    print('******** page'+str(page_no)+' ********')

driver.get('https://korean.visitkorea.or.kr/list/fes_list.do?choiceTag=&choiceTagId=')
html = driver.page_source

pageNum = 1
for i in range(1,4) :
    # 크롤링 --------

    # --------------
    time.sleep(5)
    pageNum += 1


    # 다음 페이지의 xpath 설정 : 5 배수일 경우 숫자 변경하는 것 필요 (if문 사용하기)
    xpath = '/html/body/div[2]/div[2]/div[1]/div[2]/a['+str(pageNum)+']'

    # 다음 페이지 클릭
    curr3 = driver.find_element_by_xpath(xpath)
    print(curr3.text)
    curr3.click()
#driver.quit()