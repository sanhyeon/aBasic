import requests
from bs4 import BeautifulSoup

from cWebConn.hWk.Ex01_selenium import soup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    ul = soup.find("ul", class_="list_news")

    result = []

    for span in ul.find_all('span', class_='tit'):
        result.append(span.get_text())

    return result


def main():
    answer = []
    url = "https://sports.donga.com/ent"

    for i in range(0, 5):
        req = requests.get(url, params={'p': i + 20 + 1})
        soup = BeautifulSoup(req.text, "html.parser")

        answer += crawling(soup)

    # crawling 함수의 결과를 출력합니다.
    print(answer)


if __name__ == "__main__":
    main()
# 실습 - 각 기사의 href 수집하기

# 단일 페이지에 여러 가지 링크가 있는 경우가 있습니다. 기사를 클릭하면 해당 기사를 볼 수 있는 url로 이동할 수 있습니다. 이런 url로 이동하는 링크들을 수집하고자 합니다.

# HTML Tag 중, 연동된 href를 수집하여 리스트형 변수 list_href에 담아 출력하는 실습을 진행합니다.

# https://sports.donga.com/ent?p=1&c=02

import requests
from bs4 import BeautifulSoup


def get_href(soup):
    # soup에 저장되어 있는 각 기사에 접근할 수 있는 href들을 담고 있는 리스트를 반환해주세요.
    ul = soup.find("ul", class_="list_news")

    result = []

    for span in ul.find_all("span", class_="tit"):
        result.append(span.find("a")["href"])

    return result


def main():
    list_href = []

    url = "https://sports.donga.com/ent?p=1&c=02"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    list_href = get_href(soup)
    print(list_href)


if __name__ == "__main__":
    main()


{"href": ..., "onclick": ...}


a = soup.find("a")
a["href"]




a.attrs


# 실습 - 네이트 최신뉴스 href 수집하기

# 웹 페이지 href 링크들을 수집하여 리스트형 변수 list_href에 담아 출력해봅니다.
# https://news.nate.com/recent?mid=n0100

import requests
from bs4 import BeautifulSoup


def get_href(soup):
    # 각 기사에 접근할 수 있는 href를 리스트로 반환하세요.
    div_list = soup.find_all("div", class_="mduSubjectList")

    result = []
    for div in div_list:
        result.append("https:" + div.find("a")["href"])

    return result


def main():
    list_href = []

    # href 수집할 사이트 주소 입력
    url = "https://news.nate.com/recent?mid=n0100"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)

    print(list_href)


if __name__ == "__main__":
    main()
# 실습 -  sbs 뉴스 최신 기사 목록의 내용 수집하기

# 수집하는 페이지에 연동되어 있는 href를 추출하여 href 주소에 있는 내용을 크롤링하고자 합니다.
# 앞의 실습은 언론 기사의 href만 크롤링했다면, 이번에는 각 기사의 내용까지 수집하는 법을 실습해봅니다.
# 사용 url : https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS

import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    # 각각의 href 페이지에 들어있는 기사 내용을 반환합니다.
    div = soup.find("div", class_="text_area")

    result = div.get_text()

    return result


def get_href(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    # 상위 페이지에서의 href를 찾아 리스트로 반환합니다.
    div = soup.find("div", class_="w_news_list type_issue")

    result = []

    for a in div.find_all("a", class_="news"):
        result.append("https://news.sbs.co.kr" + a["href"])

    return result


def main():
    list_href = []
    list_content = []

    url = "https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)
    print(list_href)

    for url in list_href:
        href_req = requests.get(url)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result = crawling(href_soup)
        list_content.append(result)

    print(list_content)


if __name__ == "__main__":
    main()
# 실습 - 다양한 섹션의 속보 기사 href 추출하기
# “정치”, “경제”, “사회”, “생활”, “세계”, “과학” 으로 나뉘어진 다양한 분야의 속보 기사를 추출하고자 합니다.
# https://news.naver.com/main/list.nhn?sid1=100
# 위 url에서, sid1 부분으로 분야를 설정할 수 있습니다.

import requests
from bs4 import BeautifulSoup


def get_href(soup):
    # 각 분야별 속보 기사에 접근할 수 있는 href를 리스트로 반환하세요.
    ul = soup.find("ul", class_="type06_headline")

    result = []

    for a in ul.find_all("a", class_="nclicks(fls.list)"):
        result.append(a["href"])

    return result


def get_request(section):
    # 입력된 분야에 맞는 request 객체를 반환하세요.
    # 아래 url에 쿼리를 적용한 것을 반환합니다.
    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    url = "https://news.naver.com/main/list.nhn"

    sections = {
        "정치": 100,
        "경제": 101,
        "사회": 102,
        "생활": 103,
        "세계": 104,
        "과학": 105
    }

    req = requests.get(url, headers=custom_header,
                       params={"sid1": sections[section]})  # params 매개변수를 올바르게 설정하세요.

    return req


def main():
    list_href = []

    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')

    req = get_request(section)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)

    print(list_href)


if __name__ == "__main__":
    main()
# 실습 - 다양한 섹션의 속보 기사 내용 추출하기
# 다양한 섹션의 속보 기사 href 추출하기 실습과 마찬가지로 네이버 뉴스 속보 페이지에서 실습을 진행합니다.
# 사용 url : https://news.naver.com/main/list.nhn
# 이번에는 특정 분야를 입력받으면 해당 분야의 속보 기사들의 href를 얻고, 그 href로 각각의 기사로 접근하여 기사의 내용을 크롤링하려고 합니다.

import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # 기사에서 내용을 추출하고 반환하세요.
    div = soup.find("div", class_="_article_body_contents")

    result = div.get_text().replace("\n", "").replace('// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}',
                                                      '').replace('\t', '')

    return result


def get_href(soup):
    # 각 분야별 속보 기사에 접근할 수 있는 href를 리스트로 반환하세요.
    ul = soup.find("ul", class_="type06_headline")

    result = []

    for a in ul.find_all("a", class_="nclicks(fls.list)"):
        result.append(a["href"])

    return result


def get_request(section):
    # 입력된 분야에 맞는 request 객체를 반환하세요.
    # 아래 url에 쿼리를 적용한 것을 반환합니다.
    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    url = "https://news.naver.com/main/list.nhn"

    sections = {
        "정치": 100,
        "경제": 101,
        "사회": 102,
        "생활": 103,
        "세계": 104,
        "과학": 105
    }

    req = requests.get(url, headers=custom_header,
                       params={"sid1": sections[section]})  # params 매개변수를 올바르게 설정하세요.

    return req


def main():
    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    list_href = []
    result = []

    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')

    req = get_request(section)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)

    for href in list_href:
        href_req = requests.get(href, headers=custom_header)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result.append(crawling(href_soup))
    print(result)


if __name__ == "__main__":
    main()
# 실습 - 특정 영화 리뷰 추출하기
# 리뷰를 알고 싶은 영화의 제목을 입력하면, 해당 영화의 리뷰들의 제목을 알려주는 프로그램을 제작해봅시다.
# 지시사항
# get_url, get_href, crawling 함수를 올바르게 구현하세요.
# get_url : main 함수에서 입력된 영화 제목을 네이버 영화 검색창에 검색하였을 대 나오는 url을 반환해야 합니다.
# get_href : get_url에서 얻은 url로 접근하였을 때, 가장 위에 존재하는 영화의 href를 반환합니다.
# crawling : 이전에 구현하였던 영화 리뷰 추출 방식과 동일합니다.

import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    # 1장 실습의 영화 리뷰 추출 방식과 동일합니다.
    ul = soup.find("ul", class_="rvw_list_area")

    result = []
    for li in ul.find_all("li"):
        result.append(li.find("strong").get_text())

    return result


def get_href(soup):
    # 검색 결과, 가장 위에 있는 영화로 접근할 수 있는 href를 반환하세요.
    ul = soup.find("ul", class_="search_list_1")

    a = ul.find("a")

    href = a["href"].replace("basic", "review")

    return "https://movie.naver.com" + href


def get_url(movie):
    # 입력된 영화를 검색한 결과의 url을 반환하세요.
    return f"https://movie.naver.com/movie/search/result.nhn?query={movie}&section=all&ie=utf8"


def main():
    list_href = []

    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    # 섹션을 입력하세요.
    movie = input('영화 제목을 입력하세요. \n  > ')

    url = get_url(movie)
    print(url)
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    movie_url = get_href(soup)
    print(movie_url)

    href_req = requests.get(movie_url)
    href_soup = BeautifulSoup(href_req.text, "html.parser")

    list_href = crawling(href_soup)
    print(list_href)


if __name__ == "__main__":
    main()