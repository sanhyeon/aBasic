"""
    기상청 사이트에서 필요한 데이타를 추출하고자 한다면?
        - 데이타 가져오기     ` requests 모듈
                             ` urllib.request 모듈의 urlopen() 이용
        - 데이타 추출    BeautifulSoup 이용
"""

from bs4 import BeautifulSoup
from urllib import request as req


# 1. 데이타 가져오기
#  http://www.kma.go.kr > [생활과산업] > [서비스] > [인터넷] > RSS
rssUrl = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
res = req.urlopen(rssUrl)
print(res)  # [결과] http.client.HTTPResponse object

# 2. 필요 데이타 추출하기
soup = BeautifulSoup(res, 'html.parser')
print(soup) # 파싱 결과확인
print('-'*100)

# 제목 / 도시 / 시간대별 날씨상태등 추출하여 출력

print('도시명: ', data['name'])
print('날씨 :', data['weather'][0]['description'])    #[0]쓰이는 이유: 처음이라 지정한 뒤 찾으려는 값 가져오려고
# 최저온도
print('최저온도: ', data['main']['temp_min'])
# 최고온도
print('최고온도: ', data['main']['temp_max'])

# 습도
print('습도 : ', data['main']['humidity'])
# 기압
print('기압 : ', data['main']['pressure'])