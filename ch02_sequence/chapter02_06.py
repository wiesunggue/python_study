# 시퀀스의 복합 할당
# +=는 __iadd__()를 호출하는 특수 연산자다.
# 하지만 iadd가 선언되지 않은 경우 add를 호출한다.

# *=는 __imul__()를 호출하는 특수 연산자다.
# 하지만 imul가 선언되지 않은 경우 add를 호출한다.

l = [1,2,3]
print(id(l))

l *=2
print(l)
print(id(l))
# => 리스트의 경우 id가 유지된다(기존과 같은 객체임을 의미한다.)


t = (1,2,3)
print(id(t))
t *=2
print(id(t))
# 튜플의 경우 id가 새로 생성된다.(불변 시퀀시 이므로 *=연산을 위해 새로운 튜플을 생성)

# => 가변 시퀀스의 경우 시퀀스가 유지되고,
# => 불변 시퀀스의 경우 시퀀스가 유지되지 않아서 반복적인 연산하기 매우 비효율적이다.

t = (1,2,[30,40]) # 튜플 속 리스트
#t[2]+=[50,60] # 불변 시퀀스처럼 될까 아니면 가변 시퀀스처럼 될까?

# 정답은 불변인 동시 가변 시퀀스처럼 작동한다.
print(t)

# 내부적으로 어떤 일이 확인하는 모듈 dis
import dis
dis.dis('s[a] +=b')

# 가변 항목을 튜플에 넣는것은 좋은 생각이 아니다
# 복합 할당자는 원자적인 연산이 아니다
# 파이썬의 바이트 코드