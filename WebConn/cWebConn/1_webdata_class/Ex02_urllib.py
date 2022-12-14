
# 내장모듈이용

from urllib import request

url = 'https://www.google.com'
site = request.urlopen(url)

page = site.read()
print(page)
print('-'*50)
print(site.status)  # 상태값 받아오기

headers = site.getheaders() # 헤더값 받아오기
print(headers)

for header in  headers:
    print(header[0],'>>',headers[1])