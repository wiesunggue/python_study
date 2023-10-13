# 04.04 인코딩/디코딩 문제 해결하기
# UnicodeError 라는 범용 예외가 있지만, UnicodeEncodeError나 UnicodeDecodeError같은 구체적인 예외가 발생
# 이 예외들은 어떻게 처리할까?

# UnicodeEncodeError 처리하기
city = 'São Paulo'
print(city.encode('utf_8')) #3개의 encoding방식 utf8, utf16, cp437
print(city.encode('utf_16'))
print(city.encode('iso8859_1'))
#print(city.encode('cp437')) #error가 난다.(ã를 인코딩 할 수가 없다.)

print(city.encode('cp437',errors='ignore')) # error가 난 부분을 무시한다
print(city.encode('cp437',errors='replace')) # error가 난 부분을 ?로 대체한다.
print(city.encode('cp437',errors='xmlcharrefreplace')) # xml개체로 치환한다.

# UnicodeDecoderError 처리하기
octets = b'Montr\xe9al' # \xe9부분이 치환된다. Montreal이 원래 문자
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))
#print(octets.decode('utf_8')) # 해당 문자는 decode할 수 없다
print(octets.decode('utf_8',errors='replace')) # utf-8에서는 알 수 없는 문자를 �로 표기한다(U+FFFD)의 코드

# Syntax Error

# coding: cp1252
print('01á, Mundo!')
# 파이썬 코드는 반드시 utf-8로 코딩되지 않아도 된다.

# 바이트 시퀀스의 인코딩 방식을 알아내는 방법
# 없다. 반드시 인코딩 정보를 별도로 가져와야 한다
# Chatdet은 인코딩의 특징을 활용하여 여러 인코딩 방식을 알아낸다. ex \x00과 같은 형식 특정 인코딩에서만 사용하는 형식

# utf포멧은 BOM(Byte Order Mark)를 표시할 수 있다.
# BOM : 유용한 깨진 문자

u16 = 'El Niño'.encode('utf16')
print(u16) #b'\xff\xfe가 문자 앞에 추가되었다. 이는 인텔 CPU의 리틀엔디언 바이트 순서를 나타낸다.
print(list(u16))
# 만약 b'\xef\xbb\xbf'가 추가되었다면 utf-8파일일 가능성이 높다. 하지만, 파이썬은 이를 인식하지 못한다.
