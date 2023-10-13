# 7.7 간단한 데커레이터 구현하기


import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' %(elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
# 데코레이터의 작동 방식
# factorial = clock(factorial)이 대입된다
# 반환값이 clocked이므로 factorial은 clocked를 반환하도록 한다
# 이에 따라서 factorial(n)의 실행은 clocked(n)의 실행과 동일하다.
if __name__ == '__main__':
    print('*'*40, 'Calling snooze(.123)')
    snooze(.123)
    print('*'*40, 'Calling factorial(6)')
    print('6! = ',factorial(6))
    
# 개선된 clock 데커레이터
import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg)for arg in args))
        if kwargs:
            pairs = ['%s=%r'%(k,w)for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %s' %(elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
print('6! = ', factorial(6))