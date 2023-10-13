# Chapter04-04
# 시퀸스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict

from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only
d_frozen = MappingProxyType(d)
print(id(d), d)
print(id(d_frozen), d_frozen)

# 수정 가능
d['key2'] = 'val2'
print(d)
# 수정 불가능
# d_frozen['key2'] ='val2'
# print(d_frozen)

print()
print()

s1 = {'Apple','Orange','Apple','Orange','Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # s4 = {} 로 하면 dict선언이다
s5 = frozenset({'Apple','Orange','Apple','Orange','Kiwi'})

s1.add('Melon')
print(s1)
# s5.add('Melon') frozenset에서는 add를 할 수 없다
# print(s5)

print(s1,type(s1))
print(s2,type(s2))
print(s3,type(s3))
print(s4,type(s4))
print(s5,type(s5))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
# dis 는 선언 과정을 출력해서 보여줌
from dis import dis

print('------')
print(dis('{10}'))
print('------')
print(dis('set(10)')) # 이렇게 선언 하는것이 더 과정이 복잡하다 dis를 통해서 선언 과정을 볼 수 있다.

# 지능형 집합(comprehending Set)

print('------')
from unicodedata import name
print({name(chr(i),'') for i in range(1,256)})
