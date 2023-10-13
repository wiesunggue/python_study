# Chapter04-02
# 시퀸스형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b
# 두 식은 같다
print(divmod(100, 9)) # 두 인수 입력
print(divmod(*(100, 9))) # 하나의 튜플을 2개의 인수로 풀어서 입력

print(*divmod(100, 9))  # 반환을 unpacking 해서 출력한다

x, y, *rest = range(10)
print(x, y, rest)  # x = 0, y = 1, rest = [2,...,9]

x, y, *rest = range(2)
print(x, y, rest)  # x = 0, y = 1, rest = []

x, y, z, *rest = 1, 2, 3, 4, 5
print(x, y, z, rest)  # rest에 남은게 리스트로 들어갔다

# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))
# l = l*2 와 l *=2는 같다 (리스트), id 재할당 X
# m = m*2 와 m *=2는 다르다 (튜플), id 재할당 O
l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l))
print(m, id(m))

# sort vs sorted
# reverse, key=len, keys=str.lower, key = func....

# sorted : 정렬 후 새로운 객체 반환(원본 수정하지 않음)
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len)) # 잛은거 기준으로 정렬
print('sorted - ', sorted(f_list, key=lambda x: x[-1]))
print('sorted - ', sorted(f_list, key=lambda x: x[-1], reverse=True))

print('sorted - ', f_list)
# sort : 정렬 후 객체 직접 변경
print('sort - ',f_list.sort())

# 반환 값 확인(None) #sort는 반환 값이 없음
print('sort -',f_list.sort(),f_list)
print('sort - ', f_list.sort(reverse=True),f_list)
print('sort - ', f_list.sort(key = len),f_list)
print('sort - ', f_list.sort(key = lambda x : x[-1]),f_list)
print('sort - ', f_list.sort(key = lambda x : x[-1]),f_list)

# list vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환)
#