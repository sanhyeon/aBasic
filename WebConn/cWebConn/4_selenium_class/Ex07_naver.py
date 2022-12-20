from selenium import webdriver


import time


driver = webdriver.Chrome("./webdriver/chromedriver")

driver.get("https://v4.map.naver.com")


search_bt = driver.find_element_by_name('q')
search_bt.send_keys('식당')
search_bt.submit()


# 1초의 지연시간을 줍니다.
time.sleep(2)


# 컨테이너(가게 정보) 수
stores = driver.find_elements_by_css_selector("div.lsnx")
for store in stores:
    # 세부 데이터 수집
    name = store.find_element_by_css_selector("dt > a").text
    addr = store.find_element_by_css_selector("dd.addr").text
    phone = store.find_element_by_css_selector("dd.tel").text

    print(name, addr, phone)

driver.close()