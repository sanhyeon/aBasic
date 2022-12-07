"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""

''' 자바인 경우
class Sample {
    String data = "Hello";
    String name;
    Sample(String name){
        this.name = name;
    }
}
Sample s = new Sample("홍길동");
'''

class Sample:
    data = 'Hello'
    def __init__(self, name, age):
        self.name = name        #멤버 변수 선언
        self.age = age
        print('__init__ 호출')
    def __del__(self):
        print('__del__호출')
s = Sample('홍길동', 55)
print(s.data)
print(s.name)
print(s.age)
del s
print('-'*20)











"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
 
[자바인 경우]
class Sample{
    int a;
    static int b;
}
sample s1 = new Sample();
sample s2 = new Sample();
sample s3 = new Sample();
"""

class Book:
    cnt = 0

    def __init__(self, title):
        self.title = title
        self.cnt += 1

    def output(self):
        pass

    @classmethod
    def output2(cls):
        cls.cnt += 1

b1 = Book('행복이란')
b2 = Book('먹고살자')
b1.output2()
b2.output2()
print(Book.cnt)



'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''
class Animal:
    def move(self):
        print('동물은 움직인다')

class Human(Animal):
    def move(self):
        print('인간은 두발로 걷는다')

class Wolf(Animal):
    def move(self):
        print('늑대는 네발로 달린다')


class Werewolf(Wolf, Human):
    def move(self):
        print('늑대인간은 두 발로 달린다')
print('-'*20)
ww = Werewolf()
ww.move() #

h = Human()
h.move()
w = Wolf()
w.move()
