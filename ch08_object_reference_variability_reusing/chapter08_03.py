# 8.3 기본 복사는 얕은 복사

l1 = [3,[55,44],(7,8,9)]
l2 = list(l1)
print(l2)
print(l1==l2)
print(l1 is l2)
# 얕은 복사가 일어나서 사본이 생성되었다.(아예 다른 값) -> 모든 값을 전부 복사해야 한다.
l1.append(100)
l1[1].remove(55)
print('l1',l1)
print('l2',l2)
l2[1]+=[33,22] # list의 경우 참조를 복사하는 것이기 때문에 l2를 바꿔도 l1이 같이 바뀌게 됨
l2[2]+=(10,11) # +=(10,11)연산의 경우 새 튜플을 생성해서 값을 추가하기 때문에 별도의 참조를 새로 생성하여 동작한다.
print('l1',l1)
print('l2',l2)

# 8.3.1 객체의 깊은 복사와 얕은 복사
# copy모듈에 제공하는 deepcopy()함수는 깊은 복사를, copy()함수는 얕은 복사를 지원한다.

class Bus:
    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1),id(bus2),id(bus3))
bus1.drop('Bill')
print(bus2.passengers) # 얕은 복사이기 때문에 참조를 복사한 것이고 bus2.passengers도 같이 삭제된다.
print(id(bus1.passengers),id(bus2.passengers),id(bus3.passengers))
print(bus3.passengers) # 깊은 복사이기 때문에 참조를 복사하지 않고 실제 list를 복사하였다. 즉 Bill이 삭제되지 않았다.

import copy
a = [10,20]
b = [a,30]
a.append(b)
print(a) # 순환 참조

c = copy.deepcopy(a)
print(c)
# 순환 참조되어서 참조된 내부까지 복사되었다.
d = copy.copy(a)
print(d)