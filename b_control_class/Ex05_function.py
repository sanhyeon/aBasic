"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""

# (0) 인자도 리턴값도 없는 함수
def func():
    print('inside func')
    #return 'ok'
func()
result = func() # None
print(result)

# (1) 리턴값이 여러개 있는 함수
def func(arg):
    return arg+5, arg-5, arg*5

result = func(10)
print(result)

a, b, c = func(10)
print(a, b, c)

# (2) 위치인자 (postitional argument)       - 순서대로
def func(greeting, name):
    print(greeting, '!!!!', name, '님')

func('하이','박길동')
func('홍길동','안녕')

# (3) 키워드인자 (keyword argument )         - 키워드 찾아가는 인자
func(name='홍길동', greeting='안녕')

# (4) 인자의 기본값                           - 값이 안 들어올때 기본값 입력
def func(greeting, name="홍길동"):
    print(greeting, '!!!!', name, '님')


func('하이', '박길동')
func('안녕')










'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''

def func(a,b,c=0,*args):   # *args 뒤에 있는 것을 이걸로 튜플로 받음
    sum = a + b + c
    for i in args:
        sum += i
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))

# --------------------------------------------------------------
# (5) 키워드 인자 모으기
def func(a, b, c=100, *args, **kwargs): # **kwargs 뒤에 있는 키워드 인자를 한꺼번에 dictionary로 받음
    sum = a + b + c
    for i in args:  # args 안에 i가 있다
        sum += i
    for k in kwargs:    # kwargs 안에 k가 있다
        sum += kwargs[k]
    return  sum

print(func(10, 20))
print(func(1, 2, 3))
print(func(1, 2, 3, 4, 5, 6))
print(func(1, 2, kor=10, eng=20))
print(func(1, 2, 3, 4, java=5, math=6, ))