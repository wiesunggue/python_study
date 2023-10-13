# 5.10 함수형 프로그래밍을 위한 패키지

from functools import reduce
from operator import mul
def fact(n):
    return reduce(lambda a,b :a*b, range(1,n+1)) # range부터는 reduce의 입력이다
# 즉 lambda함수로 곱하기를 정의하고, 입력받은 수에 대해 순차적으로 곱하기 연산을 진행하고 그 결과를 반환한다

def fact2(n):
    return reduce(mul,range(1,n+1))
# mul같은 연산은 이미 operator에 정의되어 있다.

# operator 모듈의 itemgetter()과 attrgetter() 함수
metro_data = [('Tokyo','JP',39.933,(35.689722, 139.691667)),
              ('Delhi NCR','IN',21.935,(28.613889,77.208889)),
              ('Mexico City','MX',20.142,(19.433333,-99.133333)),
              ('New York-Newark','US',20.104,(40.808611,-74.020386)),
              ('Sao Paulo','BR',19.649,(-23.547778, -46.635833)),
              ]

# itemgetter예제
# 튜플을 입력하면 해당 인덱스에 맞는 튜플을 반환한다
# itemgetter(1)이므로 도시 약자인 JP, IN, MX가 반환되고 사전순으로 가장 빠른 B가 먼저 출력된다.
from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

# 여러 인덱스를 반환하고 싶을 때는 itemgetter(1,2)처럼 사용 가능하다.
cc_name = itemgetter(1,2)
for city in metro_data:
    print(cc_name(city))
# itemgetter()은 []연산자를 사용하므로 시퀀스 뿐만 아니라 매핑 및 __getitem__()을 구현한 모든 클래스를 지원한다.

# attrgetter()은 이름으로 객체 속성을 추출하는 함수를 생성한다.
from collections import namedtuple
LatLong = namedtuple('LatLong','lat long')
Metropolis = namedtuple('Metropolis','name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))for name,cc,pop,(lat,long) in metro_data]
print(metro_areas[0])
print(metro_areas[0].coord.lat)
from operator import attrgetter
name_lat = attrgetter('name','coord.lat')
for city in sorted(metro_areas,key=attrgetter('coord.lat')):
    print(name_lat(city))
# 이를 활용하면 특정 조건을 기준으로 정렬을 한 후, 원하는 것만 출력할 수 있다.

# operator의 내장함수 methodcaller()
# 원하는 함수를 만들어주는 고위함수!
# 인자로 전달받음 함수를 사용할 수 있으며 partial 처럼 일부 인수를 고정할 수 있다.
from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))

hiphenate = methodcaller('replace',' ','-')
print(hiphenate(s))

# functools.partial()로 인수 고정하기
from functools import partial
from operator import mul
triple = partial(mul,3)

print(triple(7))
print(list(map(triple, range(1,10))))

# partial 함수를 통해 편리한 유니코드 변환 함수 만들기
import unicodedata, functools
nfc = functools.partial(unicodedata.normalize,'NFC')

from tagger import tag

# functools중 lru_cache()함수는 호출 결과를 저장하여 자동으로 함수의 결과를 메모이제이션 해준다
