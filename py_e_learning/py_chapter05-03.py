# Chapter05-03
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능


# 대충 성질이
# 1. 함수와 내부 함수 동시에 선언
# 2. 외부함수에서 내부함수로 참조 가능하지만 직접 사용하거나 (함수를 써서 상태를 변경 가능, 직접 대입연산 하려면 새 변수 선언으로 취급함)
# 3. 외부함수는 내부 함수를 반환함
# 4. 사용은 클래스 처럼 하면 됨( c = 외부함수(aa))

# Closure 사용
def closure_ex1():
    # Free variable
    # 클로저 영역
    series = []

    def averager(v):
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager


avg_closure1 = closure_ex1()
# 클래스에서 __call__과 같은 역할을 함
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__closure__[0].cell_contents)


# 잘못된 클로저 사용
#def closure_ex2():
#    # Free variable
#    cnt = 0
#    total = 0

#    def averager(v):
#        cnt += 1 #cnt를 재정의 하는거라 안된다
#        total += v
#        return total / cnt

 #   return averager


#avg_closure2 = closure_ex2()


# print(avg_closure2(10)) # 예외 발생

def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total # 다시 사용하려면 nonlocal을 이용해야 한다
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_ex3()
print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(55))

def exp(ms):
    msg = 'Hi, ' + ms
    def pr(aa):
        nonlocal msg
        msg=msg+aa
        print(msg)
        return msg
    return pr

c = exp('hello')
c('  0')
c('  1')
c('  2')
c('  3')