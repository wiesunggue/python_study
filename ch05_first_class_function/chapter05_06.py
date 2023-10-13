# 5.6 함수 인트로스펙션
# 함수 객체는 doc이외에도 많은 객체들이 존재한다
x=1
def factorial(n : int=10)->int:
    '''returns n!'''
    global x
    a=3 #1
    return 1 if n<2 else n*factorial(n-1)
print(dir(factorial))

# 대부분은 일반적인 속성이지만 아닌 것이 몇가지 존재한다
class C: pass
obj = C()
def func(): pass
print("함수에만 존재하는 속성들 : ",sorted(set(dir(func))-set(dir(obj))))



# __annotations__ 매개변수 및 반환값에 대한 주석(n : int, func->int등으로 annotation이 있어야 한다)
# __call__ 콜러블 객체 프로토콜에 따른 ()연산 구현
# __closure__ 자유 변수 등 함수 클로저
# __code__ 바이트코드로 컴파일된 함수 메타데이터 및 함수 본체
# __defautls__ 형식 매개변수의 기본값
# __get__ 읽기 전용 디스크립터 프로토콜 구현
# __globals__ 함수가 정의된 모듈의 전역 변수
# __kwdefautls__ 키워드 전용 형식 매개변수의 기본값
# __name__ 함수의 이름
# __qualname__ random.choice()와 같은 함수 전체 명칭

print('__annotations__ : ',factorial.__annotations__)
print('__call__ : ',factorial.__call__(5))
print('__closure__ : ',factorial.__closure__)
print('__code__ : ',factorial.__code__)
print('__defaults__ : ',factorial.__defaults__)
print('__get__ : ',factorial.__get__(5))
print('__globals__ : ',factorial.__globals__)
print('__kwdefaults__ : ',factorial.__kwdefaults__)
print('__name__ : ',factorial.__name__)
print('__qualname__ : ',factorial.__qualname__)