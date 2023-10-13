# 4.1 문자 문제

s = 'café'
print(len(s))
b = s.encode('utf8') #caf까지는 그대로 있지만 é가 utf8에서 2 바이트로 구분되기 때문이다.
print(b)
print(len(b)) # b의 길이가 5로 판단된다.
print(b.decode('utf8'))

# bytes와 bytearray는 format, format_map의 메서드를 제외하고 str이 지원하는 메서드는 전부 지원함
