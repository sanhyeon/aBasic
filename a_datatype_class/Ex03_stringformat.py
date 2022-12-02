
# -----------------------------------------
#  문자열 포맷
#       0- 문자열 포맷팅
#               print('내가 좋아하는 숫자는 ', 100 )
#       1- format() 이용
#               print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
#       2- % 사용
#               print('내가 좋아하는 숫자는 %d 이다' % 100 )
#       성능(속도)는 %이 더 빠르다고는 하지만 코드가 깔끔하게 하는 것이 더 중요하다고 하고는
#       어느 것으로 선택하라고는 안 나옴


# format()이용


# [참고] http://pyformat.info

# % 이용 - printf() 역할
name = '홍길동'
age = 22
height = 170.456
print('이름: {0}, 나이: {1}, 키:{2:0.1f}'.format(name,age,height))

print('이름 : %s, 나이 : %d, 키 : %.1f' % (name,age,height))





#--------------------------------------------------
# 실수인 경우



a = 11

b = 9

print('a' + 'b')

fact = "Python is funny"

print(str(fact.count('n') + fact.find('n') + fact.rfind('n')))

text = 'Gachon CS50 - programming with python'

text2 = " Human cs50 knowledge belongs to the world "

text.lower()

print(text[:5] + text[-1] + text[6] + text2.split()[0])

class_name = 'introduction programming with python'

for i in class_name:

    if i == 'python':
        i = i.upper()

print(class_name)


a = '10'

b = '5-2'.split('-')[1]

print(a * 3 + b)


a = "abcd e f g"

b = a.split()

c = (a[:3][0])

d = (b[:3][0][0])

print(c + d)

result = "CODE2018"

print("{0},{1}".format(result[-1], result[-2]))

text = 'Gachon CS50 - programming with python'

text2 = " Human cs50 knowledge belongs to the world "

text.lower()

