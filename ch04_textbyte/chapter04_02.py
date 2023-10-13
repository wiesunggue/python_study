# 4.2 바이트에 대한 기본 지식
# bytes 와 bytearray
# bytes는 불변형이고, bytearray는 가변형

cafe = bytes('café',encoding='utf_8')
print(cafe)

print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[:-1])

import array
numbers = array.array('h',[-2,-1,0,1,2]) #h명령어는 short int 형의 배열을 생성한다.
print(numbers)
octets = bytes(numbers) # 사본이다.
print(octets)
# 버터와 같은 객체로 부터 bytes와 bytearray를 생성하게 되면 언제나 바이트를 복사한다.
# 하지만 memoryview를 활용하면 데이터 구조체 간에 메모리를 공유할 수 있게 해준다.

# struct모듈은 다양한 형의 필드로 구성된 튜플을 분석하고, 이와 반대로 튜플을 패킹된 바이트로 변환하는 함수를 제공
# struct는 bytes, bytearray, memoryview객체와 함께 사용된다.

import struct
fmt = '<3s3sHH'
with open('filter.gif','rb') as fp:
    img = memoryview(fp.read())
    
header = img[:10]
print(bytes(header))
struct.unpack(fmt,header)
del header
del img