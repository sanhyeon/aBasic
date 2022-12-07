# import mypackage.mymodule     - print에 mypackage.module을 다 입력해야 한다.
#
# print('오늘의 날씨 : ', mypackage.mymodule.get_weather())
# print('오늘은 ', mypackage.mymodule.get_date(), '요일입니다')

# from mypackage import mymodule    - print에 이전과는 달리 mymodule만 입력하면 된다.
#
# print('오늘의 날씨 : ', mymodule.get_weather())
# print('오늘은 ', mymodule.get_date(), '요일입니다')

from mypackage import mymodule as mm # 별칭을 사용하여 print에 별칭만 사용해야 한다.

print('오늘의 날씨 : ', mm.get_weather())
print('오늘은 ', mm.get_date(), '요일입니다')