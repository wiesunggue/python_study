# Chapter05-01
# 일급 함수(일급 객체)
# 함수형 프로그래밍
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 함수 객체

def factorial(n):
    '''Factorial Function -> n : int '''

    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(dir(factorial))  # 함수를 객체 취급한다
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial
print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce
print("str****", list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 7) if i % 2])

print()
print()

# reduce 누적 집계를 내는데 사용한다
from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))

# 익명 함수( lambda)
# 가급적 주석 작성 하는게 좋다!!
# 가급적 함수 작성
# 일반 함수 형태로 리팩토링 권장

print(reduce(lambda x, t: x + t, range(1, 11)))  # add 함수를 익명 함수로 구현한 것

print()
print()

# Collable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# __call__이 있다면 호출 가능

print(callable(str), callable(A), callable(list), callable(var_func), callable(3.14))

# partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5)  # 인수에 순서대로 대입
print(five(10))

six = partial(five, 6)  # 인수를 추가 고정
print(six())
print([five(i) for i in range(1, 11) if i % 5 == 0])
print(list(map(five, filter(lambda x: x % 5 == 0, range(1, 11)))))
# 인수 여러개 고정
# partial(함수, a,b,c)

print(dir(factorial))
