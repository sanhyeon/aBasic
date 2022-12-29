import json
import time


def ListCrawling():
    print('ListCrawling 시작')
    pageNum = 1  # 페이지 번호 ( 1~153 )
    fDict = {}  # 결과값 저장 Dictionary
    cnt = 0  # 저장된 Data 수

    # 페이지 수 만큼 돌림
    for i in range(1, 2):
        print('---------------------')
        print(str(pageNum), '크롤링 시작')

        # 크롤링 --------

        import requests

        # cURL 변환 사이트 사용 : https://curlconverter.com/
        cookies = {
            '_fbp': 'fb.2.1671700331457.790934251',
            '_gid': 'GA1.3.971343431.1672215262',
            'searchListType': 'list',
            'JSESSIONID': '7E0F43C96FD001C862733A988F2149FD.instance1',
            '_gat_UA-92880258-1': '1',
            '_gat_UA-252290524-1': '1',
            '_ga': 'GA1.3.1523019435.1671700331',
            '_ga_LYY1LJZCC4': 'GS1.1.1672279133.4.0.1672279163.30.0.0',
            '_ga_6FHD6PPZEF': 'GS1.1.1672279133.4.0.1672279163.0.0.0',
            '_ga_4XLNR00KRE': 'GS1.1.1672279133.4.0.1672279163.0.0.0',
        }

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': '_fbp=fb.2.1671700331457.790934251; _gid=GA1.3.971343431.1672215262; searchListType=list; JSESSIONID=7E0F43C96FD001C862733A988F2149FD.instance1; _gat_UA-92880258-1=1; _gat_UA-252290524-1=1; _ga=GA1.3.1523019435.1671700331; _ga_LYY1LJZCC4=GS1.1.1672279133.4.0.1672279163.30.0.0; _ga_6FHD6PPZEF=GS1.1.1672279133.4.0.1672279163.0.0.0; _ga_4XLNR00KRE=GS1.1.1672279133.4.0.1672279163.0.0.0',
            'Origin': 'https://korean.visitkorea.or.kr',
            'Referer': 'https://korean.visitkorea.or.kr/list/fes_list.do?choiceTag=&choiceTagId=',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        # 페이지 값을 변경시켜서 json 결과를 받아옴.
        data = {
            'cmd': 'FESTIVAL_CONTENT_LIST_VIEW',
            'year': 'All',
            'month': 'All',
            'areaCode': 'All',
            'sigunguCode': 'All',
            'tagId': 'All',
            'locationx': '0',
            'locationy': '0',
            'sortkind': '1',
            'page': str(pageNum),  # 페이지번호 자동으로 넘겨줌
            'cnt': '10',
        }
        response = requests.post('https://korean.visitkorea.or.kr/call', cookies=cookies, headers=headers, data=data)
        fJson = json.loads(response.text)
        fList = fJson['body']['result']  # result 부분에서 param 추출

        # 상세보기 페이지로 넘어갈 param을 Dictionary로 저장
        for f in fList:
            cnt += 1
            # print(cnt,'::',f)
            cotId = f['cotId']
            cat1 = f['cat1']
            cat2 = f['cat2']
            areaCode = f['areaCode']
            title = f['title']
            fDict[title] = [cotId, cat1, cat2, areaCode]

            # print(cnt, ':: title :', title, ' , cotId :', cotId, ', cat1 :', cat1, ', cat2 :', cat2, ',
            # areaCode :', areaCode)

        # --------------

        time.sleep(5)  # 페이지 로딩 시간
        pageNum += 1  # 다음 페이지로 이동

    print('---------------------')
    print('ListCrawling 끝')
    return fDict

if __name__=="__main__" :
    ListCrawling()