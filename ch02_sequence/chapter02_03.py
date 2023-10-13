from collections import namedtuple

# 튜플은 단순 불변 리스트가 아니다
# 필드명이 없는 레코드로 사용 가능한 튜플

lax_coordinates = (33.9425, -118.408056)
city,year,pop,chg, area = ('Tokyo',2003,32450,0.66,8014)
traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s'%(passport))

for country, _ in traveler_ids:
    print(country)

# 튜플 언패킹
# 병렬 할당
# *로 언패킹

# 병렬 할당시 초과 항목을 잡을 수 있다.
a,b, *rest = range(5) # 남는 경우
print(a,b,rest) # rest = [2,3,4]

a,b, *rest = range(3) # 변수의 개수와 일치하는 경우
print(a,b,rest) # rest = [2]

a,b,*rest = range(2) # 변수의 개수가 더 많은 경우
print(a,b,rest) # rest = []

# 어느 부분에도 적용하여 사용이 가능하다.
a, *body, c, d = range(5)
print(a, body, c, d) # body = [1,2]

# 내포된 튜플
#튜플의 경우 (a,b,(c,d)) 형식으로도 사용이 가능하다

# 명명된 튜플
City = namedtuple('City','name country population coordinates') # 항목마다 이름이 존재하는 튜플
tokyo = City('Tokyo', 'JP',36.933, (35.689722, 139.691667))
print(tokyo)

print(City._fields) # 튜플이 가진 이름 출력

LatLong = namedtuple('LatLong','lat long')
delhi_data = ('Delhi NCR','IN', 21.935, LatLong(28.613889,77.208889))
print(delhi_data)
delhi = City._make(delhi_data) # 네임드 튜플이 안에 들어있는 튜플을 만드는 방식 => City(*delhi_data)와 같은 표현이다.
print(delhi)
print(delhi._asdict()) # collections.OrderedDict 객체를 반환한다.

