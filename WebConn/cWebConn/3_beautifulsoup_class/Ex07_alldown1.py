"""
    HTML 내부에 있는 링크를 추출하는 함수
        - a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse, request   # 한 줄에 다 적어도 된다
# from urllib import request

'''
    함수명 : urljoin
    인자   : url
    리턴값 : url 주소
    역할   : 받은 값을 링크로 만든다
'''
def enum_links(html,base):      # html에 response 받고 base에 url을 받는다
    #-------------------------------------
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a')    # 'a'태그 출력할 것이다.
    # print(links)

    result = []
    for a in links:
        href = a.attrs['href']
        # print(href)
        url = parse.urljoin(base, href)
        print(url)
        result.append(url)

    return result   # 응답을 넘김


if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'        # index.docu 생략됐지만 실행됨
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)  #
    print(result)   # 응답한 result 출력