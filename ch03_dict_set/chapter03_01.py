# collections.abc 모듈
# Mapping 과 MutableMapping 추상 베이스 클래스(ABC)를 제공한다

import collections.abc
my_dict = {}
print(isinstance(my_dict,collections.abc.Mapping))

# 해시 가능 : 수명 주기동안 결코 변하지 않는 해시값을 가지고, 다른 객체와 비교할 수 있으면 해시 가능하다고 한다
# 동일한 객체는 반드시 해시값이 동일해야 한다
# 불변형은 기본적으로 해시 가능
# 해시 가능하면 dictionary의 키로 활용이 가능하다

tt = (1,2,(1,2))
print(hash(tt))
t1 = (1,2,[30,40])
#print(hash(t1)) # 리스트는 해시 불가능
tf = (1,2, frozenset([30,40]))
print(hash(tf))

# 딕셔너리 기본형
a = dict(one=1,two=2,three=3)
b = {'one':1,'two':2,'three':3}
c = dict(zip(['one','two','three'],[1,2,3]))
d = dict([('two',2),('one',1),('three',3)])
e = dict({'three':3,'one':1,'two':2})
print(a==b==c==d==e)