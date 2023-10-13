# 파이썬 데이터 모델
# 매직 매소드
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 클래스 안에 정의 할 수 있는 특별한(Built in) 메소드 (이미 만들어짐)

# 클래스 예제 2
# 벡터(x,y) (5,2)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10
class Vector(object):

    def __init__(self, *arg):
        """
        Create a vector, example : v = Vector(5,10)
        """
        if len(arg) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = arg

    def __repr__(self):
        """Return the vector infomations."""
        return 'Vector(%r,%r)' % (self._x, self._y)

    def __add__(self, other):
        """Return the vector addition of self and other"""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        """Return the vector multiply of self and other"""
        return Vector(self._x * other, self._y * other)

    def __bool__(self):
        """__bool__ is False only when vector is (0,0)"""
        return bool(max(self._x, self._y))


print(Vector.__init__.__doc__)

# vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직 매소드 출력
print(Vector.__add__.__doc__)
print(Vector.__mul__.__doc__)
print(Vector.__bool__.__doc__)

print(v1, v2, v3)
print(v1+v2)
print(v1*3)
print(v2*10)
print(bool(v1*0),bool(v3+v1))

if bool(v3):
    print('ok')
else:
    print('No')
