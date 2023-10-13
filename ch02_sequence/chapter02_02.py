import array
symbols = "ABCDEDFG"
codes = []

# 2가지 표현 방식

# 리스트 추가
for symbol in symbols:
    codes.append(ord(symbol))

# 지능형 리스트
codes = [ord(symbol) for symbol in symbols]
print(codes)

x = 'ABC'
# 고유한 지역 범위를 가져 다음과 같은 코드도 문제가 생기지 않는다!
dummy = [ord(x) for x in x]
print(dummy)

beyond_ascii = [ord(s) for s in symbols if ord(s)>68]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c>68, map(ord, symbols)))
print(beyond_ascii)

# 데카르트 곱 표현하기
colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)

# 제너레이터 표현식 ()로 만들기
print(tuple(ord(symbol) for symbol in symbols))

ar = array.array('I', (ord(symbol) for symbol in symbols))
print(ar)

# 제너레이터 데카르트 곱 => 필요할 때 불러와서 메모리를 더 절약할 수 있다.
for tshirt in ('%s %s' %(c, s) for c in colors for s in sizes):
    print(tshirt)

