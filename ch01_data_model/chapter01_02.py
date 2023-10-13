from math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x +other.x
        y = self.y +other.y

        return Vector(x,y)

    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)


# __repr__ 메서드
# 객체를 문자열로 표현하기 위한 메서드
# 이게 정의되지 않았다면 <Vector object at 0x00...> 같은게 나온다

print(Vector(3,4))

# __bool__ 메서드
# __bool__이나 __len__ 이 정의되지 않았다면 기본적으로 참을 반환한다.
# 하지만 __len__이 정의되어 있다면 __len__을 반환한다.
