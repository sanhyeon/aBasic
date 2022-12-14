"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

'''
    함수명 : urlretrieve
    인자   : url
    리턴값 : savepath
    역할   : 받은 값을 넣을 파일을 만들고 그 파일에 library에 넣는다
'''
def download_file(url):
    p = parse.urlparse(url)
    #print('1-', p)
    savepath = './' + p.netloc + p.path
    #print('2-', savepath)

    if re.search('/$', savepath):
        savepath += 'index.html'        # index.html을 붙힌다
        print('3-', savepath)

    savedir = os.path.dirname(savepath)     # docs.python.org 파일 생성
    if not os.path.exists(savedir):
        os.makedirs(savedir, exist_ok=True)

    savedir = os.path.exists(savepath)
    if not os.path.exists(savedir):
            os.makedirs(savedir)
    try:
        request.urlretrieve(url, savepath)
        time.sleep(2)
        print('download -', url)
        return savepath

    except:
        print('fail download :',url)
        return  None
if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)



