import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

# 'a'태그를 가지고 class명이 title인 element를 모두 가져와 cartoons에 저장함
cartoons = soup.find_all('a', attrs={"class": "title"})

# cartoons에 저장된 element를 하나씩 뽑아내 출력함
for cartoon in cartoons:
    # cartoon에서 텍스트를 읽어옴, 제목을 읽어오는 것
    title = cartoon.get_text()

    # cartoon에서 링크를 읽어옴, 딕셔너리 형태로 참조함
    link = cartoon["href"]

    # 얻어온 제목과 링크를 프린트함. 이때, link는 완전한 형태가 아니라서 https://comic.naver.com을 추가해줌
    print(title, "https://comic.naver.com" + link)