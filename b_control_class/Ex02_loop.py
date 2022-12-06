'''
# ------------------------------------------------------

   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들
'''

a = 112                  # 숫자형
b = ['1' , '2' , '3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry)

# 딕셔너리인 경우
for entry in e:
    print(e[entry])
else:
    print('end')


# 1부터 10까지의 합 구하기
'''
iny sum = 0;
for(int i = 1; i <=10; i++ )
sum +=i;

for <타켓변수> in 집합객체 :
        문장들
'''
sum = 0
for i in range(1, 11):
        sum += i
print('sum=', sum)

# 1부터 10가지의 홀수의 합 구하기
sum = 0
for i in range(1, 11, 2): # 1, 3, 5. 7. 9
        sum += i
print('sum=', sum)


# [과제] 2단부터 9단까지 이중 반복문으로 출력
mul = 0
for j in range(2, 10):
    print(' ')
    for i in range(1, 10):
        print(j, '*', i, '=', j*i)


li = ['z','y','x']
while li:
    data = li.pop()
    print(data)
else:
    print('end')

