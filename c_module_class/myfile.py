# import mymodule
#
# print('오늘의 날씨 : ', mymodule.get_weather())
# print('오늘은 ', mymodule.get_date(), '요일입니다')

# import mymodule as mm - 별칭을 붙혀서 사용가능 별칭으로만 사용해야 함
#
# print('오늘의 날씨 : ', mm.get_weather())
# print('오늘은 ', mm.get_date(), '요일입니다')

from mypackage.mymodule import get_weather, get_date # import에 get을 가져오면 print에 mymodule을 쓸 필요없음

print('오늘의 날씨 : ', get_weather())
print('오늘은 ', get_date(), '요일입니다')