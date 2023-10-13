# 참조로써의 함수 매개변수

def f(a,b):
    a +=b
    return a

x = 1
y = 2
print(f(x,y))
print(x,y) # x는 변하지 않는다
a=[1,2]
b=[3,4]
print(f(a,b))
print(a,b) # a는 변한다
t = (10,20)
u = (30,40)
print(f(t,u))
print(t,u) # 튜플 t는 변하지 않는다.

# 함수 전달의 경우 인수로 전달받은 모든 가변 객체를 변경할 수 있지만, 객체의 정체성 자체는 변경할 수 없다.
# list의 경우 list를 참조 위치를 복사하여 전달한 것이기 때문에 리스트가 변한 것이고
# 튜플의 경우 참조 사본을 복사하였지만 +=연산에서 새 튜플을 할당하기 때문에 t값이 변하지 않는다
# x,y의 경우는 잘 모르겠음

# 8.4.1 가변형 매개변수 기본값으로 사용하기: 좋지 못한 생각

class HauntedBus:
    """유령 승객이 출몰하는 버스 모델"""

    def __init__(self, passengers=[]):
        self.passengers = passengers
    def pick(self, name):
        self.passengers.append(name)
    def drop(self,name):
        self.passengers.remove(name)

bus1 = HauntedBus(['Alice','Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick('Dave')
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)
print(bus1.passengers)

# 해당 오류는 []가 참조 연산이 되면서 bus2에서 생성할 때 클래스 속 모든 passengers가 같은 []를 가르키도록 되었다.
# 따라서 default값으로 None을 사용하거나 인수의 사본을 self.passengers에 할당하는것이 올바른 방법이다.

# 8.4.2 가변 매개변수에 대한 방어적 프로그래밍
