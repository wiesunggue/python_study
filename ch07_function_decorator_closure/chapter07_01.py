# 7.1 데커레이터 기본 지식
# 데커레이터는 다른 함수를 인수로 받는 콜러블(데커레이트된 함수)이다.
# 데커레이터는 데커레이트된 함수에 어떤 처리를 수행하고, 함수를 다른 함수나 콜러블 객체로 대체한다.
# 예를 들어 다음 코드에서처럼 decorate라는 이름의 데커레이터가 있다고 하자
'''
@decorate
def target():
    print('running target()')

위 코드는 아래와 동일하다
def target():
    print('running target()')

target = decorate(target)
'''

def deco(func):
    func()
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target() # 이 코드는 deco(target)이다. 고위 함수 형태로 target이라는 함수를 입력받는다

# 즉 데커레이터는 함수를 인수로 받는 일반적인 콜러블과 동일하다.
# 이는 런타임에서 프로그램 행위를 변경하는 메타프로그래밍을 할 때 상당히 편리하다.

