# 7.5 클로저
# 클로저는 익명 함수와 다르다
# 함수 본체 외부에 정의된 비전역 변수에 접근할 수 있다는 것이 중요

# 값을 기록하는 함수를 만들기

# 1. 클래스를 이용해서 만들기
class Averager():
    def __init__(self):
        self.series = []
    def __call__(self,new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)
    
avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))

# 2. 고위 함수를 이용해서 만들기
def make_averager():
    series = []
    
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    
    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

# series = []로 초기화 하기 때문에 지역변수이다
# average내에 있는 series는 자유 변수이다  => 지역 범위 내에 있지 않은 변수를 의미한다
# 이 때 series는 __closure__속성에 저장된다.

print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)
# 클로저는 함수를 정의할 때 존재하던 자유 변수에 대한 바인딩을 유지하는 함수이다
# 따라서 함수를 정의하는 범위가 사라진 후에 함수를 호출해도 자유 변수에 접근할 수 있다
