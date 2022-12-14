
from bs4 import BeautifulSoup
from urllib import request

html = request.urlopen('http://www.yes24.com/Product/Search?domain=ALL&query=python')

soup = BeautifulSoup(html, 'html.parser')

# [1]
#infos = soup.select('#yesSchList div.itemUnit a.gd_name')
#print(infos)
#for info in infos:
#    print(info.text)

#print(len(infos), '권이 검색되었습니다')

# [2]
imgUrls = soup.select('#yesSchList div.itemUnit img')
#print(imgUrls)
for imgUrl in imgUrls:
    # 이미지링크를 출력 : src
    # 책제목을 출력 : alt
    imgPath = imgUrl.attrs['data-original']
    bookName = imgUrl.attrs['alt'].strip().replace('/','_')
    print(bookName, imgPath)
    request.urlretrieve(imgPath, 'imgs/' + bookName + '.jpg')
