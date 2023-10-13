# Chapter05-02
# 일급 함수(일급 객체)
# 클로저 기초

# 파이썬 변수 범위(scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)


# func_v1(10) #에러난다

# Ex2
b = 20


def func_v2(a):
    print(a)
    print(b)


func_v2(10)
# Ex3
c = 30


def func_v3(a):
    global c  # 지역변수를 전역변수로 만든다 # global은 되도록 사용하지 마라!!!!!
    print(a)
    print(c)  # c를 로컬 변수로 인식해서 함수 내에서 c를 나중에 선언한다면 에러가 남
    c = 40


print(c)
func_v3(10)
print(c)

# Closure(클로저) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메세지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드 프로그래밍에 강점

a=100
print(a+100)
print(a+1000) #a는 변하지 않는다

# 결과 누적(함수 사용)
print(sum(range(1,51)))
print(sum(range(51,101)))



# 클래스 이용
class Averager():
    def __init__(self):
        self._series =[]
    # 클래스를 함수처럼 사용 가능하게 만드는 매직 메소드
    def __call__(self,v):
        self._series.append(v)
        print(f'inner >> {self._series} / {len(self._series)}')
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = Averager()
# 함수의 상태를 기억할 수 있도록 만든다

# 누적
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(70))