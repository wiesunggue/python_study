# 7.6 nonlocal 선언
# 앞에서 구현한 make_averager()는 그리 효율적이지 않다.
# 모든 값을 다 저장하고, average()가 연산될 때마다 sum을 연산하였다
# 이 보다 합계와 항목 수를 계산해 두면 더 효율적인 구현을 할 수 있다

def make_averager():
    count = 0
    total = 0
    
    def averager(new_value):
        count += 1
        total += new_value
        return total / count
    
    return averager

# 구현이 잘못되었다.
# 이는 averager()본체 안에서 count 변수를 할당하므로 count를 지역 변수로 만든다.
# series의 리스트가 정상적으로 작동했던 이유는 series변수에 할당하는 것이 아니기 때문이다.
# 하지만 숫자, 문자열, 튜플과 같은 것은 값을 읽을 수 만 있고, 갱신할 수는 없다
# 이로 인해서 count를 대입하면 암묵적으로 count라는 지역 변수를 만든다
# count가 자유 변수가 아니므로 더이상 closure가 아니다

# nonlocal을 통해서 자유변수임을 지정할 수 있다.

def make_averager2():
    count = 0
    total = 0
    
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    
    return averager

avg=make_averager2()
print(avg(10))
print(avg(11))
print(avg(12))
