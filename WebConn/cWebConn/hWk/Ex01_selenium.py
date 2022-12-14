import cx_Oracle as oci
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import folium

import API

map_osm = folium.Map(location=[37.572807, 126.975918],
                     zoom_start=18)

# (1) 페이지에서 매장명, 전화번호, 주소 추출

# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)

# 페이지 수 만큼 돌림
for page_no in range(1, 75):

    driver.get('http://ejadam.co.kr/bbs/board.php?bo_table=store&page=%d' % page_no)
    html = driver.page_source

    # print(html)
    time.sleep(5)

    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.select('table tbody tr')

    # 매장명 - 전화번호
    for data in datas:
        dLi = data.select('td')         # td 얻어옴

        name = dLi[0].select_one('a').text.strip() # 첫번째 td 밑의 a태그의 text
        number = dLi[1].text.strip()               # 두번째 td
        addr = dLi[2].text.strip()                 # 세번째 td



        res = [name, number, addr] # 입력할 배열 생성
        # print(res) 확인용 print문


        # Contact 객체를 생성하고 DB 에 입력
        conn = oci.connect('project1/jadam@192.168.0.2:1521/xe')


        sql = '''
            INSERT INTO jadam(name, tel, addr)
                VALUES(:0, :1, :2)
            '''
        cursor = conn.cursor()
        cursor.execute(sql, res)   # jadam 테이블에 리스트 내용 insert 함



        # **************************************

        # 위도, 경도를 얻어옴
        wk = API.addr_to_w_k(addr)
        # print('위도 :', wk[0], '경도 :', wk[1])

        res2 = [str(wk[0]), str(wk[1]), addr]
        sql2 = '''
            UPDATE jadam
            SET wido = :0 ,
                gydo = :1
            WHERE addr = :2
        '''
        cursor = conn.cursor()
        cursor.execute(sql2, res2)   # jadam 테이블에 리스트 내용 insert 함

        cursor.close()
        conn.commit()
        conn.close()

        # **************************************
        folium.Marker(location=[wk[0], wk[1]],
                      popup=res[0],
                      icon=folium.Icon(color='green', icon='star')).add_to(map_osm)

        print('지점명 :', res[0], '전화번호 :', res[1], '주소 :', res[2], '위도 :', res2[0], '경도 :', res2[1])

map_osm.save('./map/map.html')