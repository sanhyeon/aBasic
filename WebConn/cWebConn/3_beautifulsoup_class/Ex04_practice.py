from urllib.request import urlopen
from bs4 import BeautifulSoup

#html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

#soup = BeautifulSoup(html, 'html.parser')

#a = soup.select('#text span.green')

#for green in a:
#    print(green.text)

html = urlopen('http://www.pythonscraping.com/pages/page3.html')

soup = BeautifulSoup(html,'html.parser')
title = soup.select('#Giftlist tr.gift')
for head in title:
    namePath = head.attrs['data-original']
    cost = head.attrs['alt'].strip().replace('/', '_')
    print(namePath,cost)


