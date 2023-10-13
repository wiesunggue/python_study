# 파이썬 데이터 모델
# 매직 매소드
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 클래스 안에 정의 할 수 있는 특별한(Built in) 메소드 (이미 만들어짐)

# 기본형
# 파이썬에서 사용하는 모든 데이터 타입은 클래스
print(int)
print(float)

# 복습 dir은 클래스내에 존재하는 모든 메타 정보를 반환하는 클래스 함수
print(dir(int))
print(dir(int))

# 이것도 역시 클래스
n = 10
print(type(n))

# 정수형 클래스에 정의된 더하기 함수
print(n+100)
print(n.__add__(100))
# 클래스에 있는 코멘트 보는 함수 __doc__
# print(n.__doc__)

print(n.__bool__(),bool(n))
print(n*100,n.__mul__(100))

# 클래스 예제 1
# 과일끼리 더하기
class  Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self): #Fruit 클래스 변수를 출력하면 나온다
        return 'Fruit Class Info : {}, {}'.format(self._name,self._price)

    def __add__(self, x):
        print('Called >> __add__')
        return self._price+x._price

    def __sub__(self,x):
        print('Called >> __sub__')
        return self._price-x._price

    def __le__(self, x): #작거나 같다의 메직 메소드
        print('Called >> __le__')
        if self._price <= x._price:
            return True
        else:
            return False
        
    def __ge__(self, x): #크거나 같다의 메직 메소드
        print('Called >> __ge__')
        if self._price >= x._price:
            return True
        else:
            return False
print(dir(Fruit))
s1=Fruit('Orange',7500)
s2=Fruit('Banana',3000)
print(s1-s2)
print(s2-s1)
print(s1 <= s2) # 7500<=3000
print(s1 >= s2) # 7500>=3000
print(s1)
print(s2)
print(dir(int))