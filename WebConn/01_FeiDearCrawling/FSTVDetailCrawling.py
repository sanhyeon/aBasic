from selenium import webdriver
from bs4 import BeautifulSoup
import time
import psycopg2 # PostgreSQL 연결 라이브러리
import os
import FSTVListCrawling as list # 축제 목록 json 받아서 처리하는 모듈
from urllib import request as req

# 1. 웹 객체 드라이버 생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)


# 2. 상세 정보 저장할 파일 생성 -- 나중에 해여
# f = open('festival.txt', 'w')
os.makedirs('festival_imgs', exist_ok=True) #이미지 저장 폴더 생성 : 이미 있을 경우에는 넘김

# 3. 상세페이지 이동에 필요한 param 저장
params = list.ListCrawling()

for p in params.values():
    print('-------------')
    cotId = p[0]
    big_category = p[1]
    mid_category = p[2]
    big_area = p[3]


    # 4. 상세페이지 이동
    detail_url = 'https://korean.visitkorea.or.kr/detail/fes_detail.do?cotid=' + cotId + '&big_category=' + big_category + '&mid_category=' + mid_category + '&big_area=' + big_area
    driver.get(detail_url)
    time.sleep(3)  # 페이지 로딩 시간
    html = driver.page_source


    # 5. 데이터 크롤링
    soup = BeautifulSoup(html, 'html.parser')

    # (1) 축제 타이틀
    topTitle = soup.select_one('#topTitle').text
    print('제목 :',topTitle)
    # (2) 축제 서브 타이틀
    subTitle = soup.select_one('#topCp .titTypeWrap h3 em').text
    print('서브제목 :',subTitle)

    # (3) 축제 포스터 이미지
    img = soup.select_one('#pImgList div.swiper-slide.swiper-slide-active img.swiper-lazy.swiper-lazy-loaded')    # 축제 포스터 이미지
    imgsrc = img.attrs['src']
    req.urlretrieve(imgsrc, 'festival_imgs/'+cotId+'.jpg') # 이미지 저장
    print('이미지 :', imgsrc)
    
    # (4-1) 상세정보 탭 늘리기
    detail_div = soup.select_one('.wrap_contView')
    plus_button = detail_div.select_one('div.area_txtView.top')
    plus_button.attrs['class'] = 'area_txtView top on'

    # (4-2) 상세정보
    detail = detail_div.select_one('.inr p')
    detail = detail.text
    print('상세정보 :',detail)

    # (5) 세부정보
    dDetails = soup.select('div.area_txtView.bottom .inr ul li')
    dDict = {}
    for d in dDetails:
        lName = d.select_one('strong').text

        # Dictionary의 key값을 DB의 컬럼명과 동일하게 맞춤
        if lName == "전화번호" :
            lName = "FSTV_TEL"
        elif lName == "시작일" :
            lName = "FSTV_STARTDATE"
        elif lName == "종료일" :
            lName = "FSTV_ENDDATE"
        elif lName == "홈페이지" :
            lName = "FSTV_HOMEPAGE"
        elif lName == "주소" :
            lName = "FSTV_ADDR"
        elif lName == "행사장소" :
            lName = "FSTV_PLACE"
        elif lName == "주최" :
            lName = "FSTV_HOST"
        elif lName == "주관" :
            lName = "FSTV_HOST2"
        elif lName == "이용요금" :
            lName = "FSTV_FEE"
        elif lName == "행사시간" :
            lName = "FSTV_TAG"

        lCont = d.select_one('span').text
        dDict[lName] = lCont
    print('세부정보 :', dDict)

    # (6) 태그
    tags = soup.select('div.tag_cont ul.clfix li')
    tList = []
    for t in tags:
        cont = t.select_one('a span').text
        tList.append(cont)
    print('태그 :', tList)

    # (7) 주소 태그 추가
    # (7-1) 띄어쓰기 기준으로 문자열을 자름 : 맨 앞 부분만 따로 저장
    temp = dDict['FSTV_ADDR'].split(' ')
    addr_temp = temp[0]

    # (7-2) 맨 앞부분이 4글자일 경우 (경상남도, 전라북도 ...) : 첫번째 글자와 세번째 글자를 합침 (경남, 전북 ...)
    if len(addr_temp) == 4 :
        addr = addr_temp[0]+addr_temp[2]
    else :
        #(7-2-1) 4글자 미만이거나 그 초과일 경우 (경기도, 서울특별시 ... ) : 앞의 두 글자만 추출 (경기, 서울 ...)
        addr = addr_temp[0:2]

    # (7-3) # + 따로 합친 글자 -> 태그 리스트에 저장
    area = '#' + addr
    tList.append(area)
    print('주소태그 :',area)

# 6. PostgreSQL 서버 DB Connet
try:
    conn = psycopg2.connect(host="postgresql-feidear.alwaysdata.net", dbname="feidear_data", user="feidear", password="gungang1229")
    cur = conn.cursor()
except:
    print("Not Connected!")

# 7. DB에 값 INSERT
sql =   '''
        INSERT INTO festival(FSTV_NAME, FSTV_SHORT, FSTV_STARTDATE, FSTV_ENDDATE, FSTV_INFO, FSTV_IMAGE, FSTV_TEL, FSTV_HOMEPAGE, FSTV_ADDR, FSTV_PLACE, FSTV_HOST, FSTV_FEE, FSTV_TIME, FSTV_TAG, fstv_area)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)       
        '''
insert=[topTitle, subTitle, dDict['FSTV_STARTDATE'], dDict['FSTV_STARTDATE'], detail, ]
cur.execute(sql,)