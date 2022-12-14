from selenium import webdriver

usr = 'ksm04002@naver.com'
pwd = 'sdjk@025415'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://www.instagram.com/')

email = driver.find_element_by_id('email')
passwd = driver.find_element_by_id('pass')

email.send_keys(usr)
passwd.send_keys(pwd)

btn = driver.find_element_by_name('login')
btn.click()
driver.implicitly_wait(2)
