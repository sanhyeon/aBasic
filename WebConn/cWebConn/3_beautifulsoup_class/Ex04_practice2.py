from bs4 import BeautifulSoup
from urllib import request as req
from urllib.parse import quote_plus



html3 = req.urlopen("https://wikidocs.net/")
soup3 = BeautifulSoup(html3,'html.parser')

item3 = soup3.select("#books .media")
print(item3)

for it3 in item3:
    bt = it3.select('.book-subject')[0].text    # 제목
    # print(bt)
    bn = it3.select('.menu_link')[0].text   # 저자
    # print(bn)
    print(bt, ': ',bn)
    bl = it3.select('.book-image')[0].attrs['src']  # 책 링크
    parse = "https://wikidocs.net"
    i = quote_plus(parse+bl, safe="://")

    req.urlretrieve(i,'imgs4/'+bt+'.jpg')
