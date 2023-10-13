# 7.4 변수 범위 규칙

def f1(a):
    print(a)
    print(b)
b=6
f1(3)

def f2(a):
    print(a)
    print(b)
    #b=9 #에러가 난다. 여기서는 b를 대입할 수 없다. => 변수에 대입하는 것이 지역 변수 선언으로 사용되었다.
f2(3)

# 바이트코드 비교
from dis import dis
dis(f1)
dis(f2)