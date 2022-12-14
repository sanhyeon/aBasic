"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""

#import urllib
from urllib import parse

baseUrl = 'http://www.example.com/html/a.html'

print(parse.urljoin(baseUrl, 'b.html'))         # 기존에 url에 입력한 url로 바꿈

print(parse.urljoin(baseUrl, 'sub/c.html'))
    # sub 밑에 url이 들어감
print(parse.urljoin(baseUrl, '/sub/d.html'))
    # 상대경로로 해서 url이 들어감

print(parse.urljoin(baseUrl, '../temp/e.html'))
    # http://www.example.com/temp/e.html

print(parse.urljoin((baseUrl, 'http://www.daum.net')))
    # http://www.example.com