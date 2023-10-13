# 8.2 정체성, 동질성, 별명
charles = {'name':'Charles L. Dodgson', 'born':1832}
lewis = charles

# is 문법은 id가 같은지만 확인 ==와는 다르다.
print(lewis is charles)
# 같은 id를 가져서 하나의 저장공간을 가르키는 2개의 이름이 할당되었다.
print(id(charles),id(lewis))

lewis['balance']=950
print(charles)

alex = {'name':'Charles L. Dodgson', 'born':1832,'balance':950}
print(alex==charles)
print(alex is charles)

# 8.2.1 ==연산자와 is 연산자간의 선택
x=None
print(x is None)
print(x is not None)
# == 연산의 경우 모든 내부 객체가 같은지를 판단한다.
# list를 비교하게 된다면 상당한 연산이 필요하게 된다.
# 하지만 is 연산의 경우 id가 같은지만 판단하기 때문에 항상 빠르게 수행 가능하다.

# 8.2.2 튜플의 상대적 불변성
t1 = (1,2,[30,40])
t2 = (1,2,[30,40])
print(t1==t2)
print(id(t1[-1]))
t1[-1].append(99)
print(id(t1[-1]))
print(t1==t2) # 튜플의 항목이 달라져서 False가 출력된다.
# 이는 튜플은 단지 참조를 저장하는 것이고, 항목 내부의 값을 저장하는 것이 아니므로 id는 같게 유지된다.
