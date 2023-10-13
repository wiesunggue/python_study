# 5.2 고위 함수
# 함수를 인수로 받거나, 함수를 결과로 반환하는 함수를 "고위함수"라고 한다

# 고위함수 예제
# sorted 함수는 key로 함수를 입력받는다
fruits = ['strawberry','fig','apple','cherry','raspberry','banana']
print(sorted(fruits,key=len))

def reverse(word):
    '''단어를 역순으로 변환하는 함수 : apple -> elppa'''
    return word[::-1]
print(sorted(fruits,key=reverse))


def factorial(n):
    '''returns n!'''
    return 1 if n<2 else n*factorial(n-1)
fact = factorial
# 대표적인 고위함수
# map, filter, reduce

# map(), filter(), reduce()의 대안

# map filter를 대신해 지능형 리스트로 생성하기
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])

print(list(map(factorial,filter(lambda n:n%2, range(6)))))
print([factorial(n) for n in range(6) if n%2]) # 훨씬 더 직관적이다.

from functools import reduce
from operator import add

print(reduce(add,range(100))) # 결과 누적형 연산
print(sum(range(100)))

# 내장 함수 all과 any
# all : iterable 함수가 전부 참이면 True를 반환
# any : iterable 함수가 하나라도 참이면 True를 반환
print(all([1,2,3,4]))
print(any([0,1,2,3]))
print(all([0,1,2,3]))

