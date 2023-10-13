# 7.2 파이썬이 데커레이터를 실행하는 시점
# 데커레이터의 특징은 데커레이트된 함수가 정의된 직후에 실행된다는 것

registry = []

def registor(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@registor
def f1():
    print('running f1()')

@registor
def f2():
    print('running f2()')


def f3():
    print('running f3()')
    
def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()
    
if __name__ == '__main__':
    main()