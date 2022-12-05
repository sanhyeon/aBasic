
# import datetime
# today = datetime.date.today()
# print('today is ', today)

from datetime import date, timedelta
today = date.today()
print('today is ', today)

# 날짜 구하기
print('년도 : ', today.year)
# 월
print('월 : ', today.month)
# 일
print('일 : ', today.day)
# 요일
print('요일 : ', today.weekday())

# 날짜 계산
print('어제 : ', today + timedelta(weeks=-1))
# 일주일전 날짜
print('일주일전 : ', today + timedelta(days=-7))
# 10일 후 날짜
print('10일 후 : ', today + timedelta(days=10))

from datetime import datetime # datetime 시분초
day = datetime.today()
print(day)

import datetime
day = datetime.datetime.today()
print(day)

# 날짜를 문자열 형태 ( strftime() 이용 )
print(day.strftime('%Y년 %m월 %d일 %H:%M'))

# 문자열을 날짜형태 ( strptime() 이용)
naljja = '2022-12-25 12:50:59'
print(type(naljja))
mydate = datetime.datetime.strptime(naljja, '%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))