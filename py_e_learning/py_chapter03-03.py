# Chapter03-03
# 파이썬 데이터 모델
# 매직 매소드
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 클래스 안에 정의 할 수 있는 특별한(Built in) 메소드 (이미 만들어짐)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
from math import sqrt

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
f = lambda pt1, pt2: sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(f(pt1, pt2))
l_leng1 = sqrt((pt1[0] - pt2[1]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point12', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)
print(pt3)
print(pt4)

l_leng2 = sqrt((pt3[0] - pt4[1]) ** 2 + (pt3[1] - pt4[1]) ** 2)
l_leng3 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng3)
print(l_leng2)
# 즉 네임드 튜플은 인덱스로도 접근 가능하고, 키로도 접근 가능하다.

# 네임드 튜플 접근 방법 총 5가지
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)  # Default = False
# 네임드 튜플은 전부다 클래스 형태로 출력된다
print(Point3)
print(Point4)
# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}
# 객체 생성
p1 = Point1(x=10, y=35)  # 클래스 변수 선언하기
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)  # 딕셔너리를 언패킹 해서 namedtuple로 만든다

print(p1)
print(p2)
print(p3)
# rename test
print(p4)  # Point(x=10, y=20, _2=30, _3=40) 임의의 변수를 만들어서 실행한다
print(p5)

# 사용
print(p1.x + p2.x)

x, y = p3
print(x, y)

# 네임드 튜플 메소드
temp = [52, 38]

p4 = Point1._make(temp)
print(p4)

# field : 필드 네임 확인 키값을 조회
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환, 딕셔너리로 반환해준다
print(p1._asdict())

# 실 사용 실습
# 반20명, 4개의 반(A,B,C,D)
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 추천
student2 = [Classes(rank, number)
            for rank in 'A B C D'.split(' ')
            for number in [str(n)
                           for n in range(1, 21)]]
# namedtupled의 이해 collections of datatype
