# 시퀀스
# 컨테이너 시퀀스
# => 서로 다른 자료형의 항목들을 담을 수 있는 list, tuple, collections.deque형

# 균일 시퀀스
# => 단 하나의 자료형만 담을 수 있는 str, bytes, bytearray, memoryview, array.array형

# 따라서 균일 시퀀스가 더 적은 메모리를 사용한다

# 가변 시퀀스
# => list, bytearray, array.array, collections.deque, memoryview 형

# 불변 시퀀스
# => tuple, str, bytes 형

# array 형 사용법
# 먼저 타입을 지정해준다 'b' -> signed char 1byte, 'B' -> unsigned char 1byte, 'i' -> signed int4, 'I' -> uint16, 'f' -> float32 'd' -> float64
arr = memoryview(bytes(10))
print(arr)