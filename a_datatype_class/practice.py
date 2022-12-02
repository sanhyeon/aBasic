button, rest = map(int,input().split()) # button = 입력 시간 , rest = 같은 숫자 연속입력 시 기다리는 시간
result = 0
check = 0
text = list(input())
al_dic = {
          2 : ['A', 'B', 'C'],
          3 : ['D', 'E', 'F'],
          4 : ['G', 'H', 'I'],
          5 : ['J', 'K', 'L'],
          6 : ['M', 'N', 'O'],
          7 : ['P', 'Q', 'R', 'S'],
          8 : ['T', 'U', 'V'],
          9 : ['W', 'X', 'Y', 'Z']}
for alpha in text :
    count = [number for number, chars in al_dic.items() if alpha in chars] # 해당 문자가 있는 키 값 전달
    if not count : # 공백일 경우
        result += button
        check = 0
    else :
        # 문자가 위치한 인덱스를 찾아 +1을 하면 그것이 곧 연속적으로 입력해야하는 횟수가 된다
        t = [c for c in range(len(al_dic[count[0]])) if alpha == al_dic[count[0]][c]] # count키값에 맞는 value 리스트에서
                                                                                      # alpha가 위치한 인덱스값
        if check == count : # 이전 문자와 비교
            result += rest + button*(t[0]+1)
        else :
            result += button*(t[0]+1)
        check = count
print(result)
import numpy
list = [int(x) for x in input('정수리스트입력: ').split()]
print('평균= {0}\n표준편차 {1}'.format(numpy.mean(list), numpy.std(list)))
recs=[]
for i in range(5):
  rec=int(input("정수를 입력하세요:"))
  recs.append(rec)
aver=sum(recs)/len(recs)
print("평균 %d " %aver)
# sum=0
# for i in range(5):
# sum += eval(input("정수를입력하세요: "))
# print("평균= {0}".format(sum/5))


print(input("문자를 입력하세요 => ")[::-1])

#string = input('문자열을입력하시오: ')
#p = {'':1, 'a':2, 'b':2, 'c':2,'d':3,'e':3,'f':3,'g':4,'h':4,'i':4,
#'j':5,'k':5,'l':5,'m':6,'n':6,'o':6,'p':7,'q':7,'r':7,'s':7,'t':8,'u':8,
#'v':8,'w':9,'x':9,'y':9,'z':9}
#for char in string:
#print(p.get(char.lower()), end='')

