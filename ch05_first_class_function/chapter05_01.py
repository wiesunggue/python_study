# chapter 5 일급 함수
# 5.1 함수를 객체처럼 다루기
# 함수는 function class의 객체이다

def factorial(n):
    '''returns n!'''
    return 1 if n<2 else n*factorial(n-1)
print(factorial(42))
print(factorial.__doc__) # doc는 함수 객체의 속성
print(type(factorial)) # class 'function'

fact = factorial
print(fact)
print(fact(5))

print(map(factorial,range(11)))
print(list(map(factorial,range(11))))

# 일급 함수가 있다면 함수형 스타일로 프로그래밍이 가능함
