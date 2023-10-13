# Chapter06-01
# 병행성(Concurrency)
# 이터레이터, 제너레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args... : iterable

# 반복 가능한 이유 -> iter(x) 함수 호출
t = 'ABCDEFGHIJKLNMOPQRSTQVWXYZ'

for c in t:
    print(c)


# while
w = iter(t)

print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))

while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# 반복형 확인
from collections import abc
print(dir(t))
print(hasattr(t,'__iter__'))
print(isinstance(t,abc.Iterable))

print()
print()

# next
class WordSplitter:
    def __init__(self,text):
        self._idx =0
        self._text = text.split(' ')
    # next를 정의하는것( for 에서 사용 가능한 형태, next로 하나씩 호출)
    def __next__(self):
        #print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Interation.')
        self._idx += 1
        return word
    ## print에서의 결과값
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tommorrow')

print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(wi)

print()
print()

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Corotine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self,text):
        self._text = text.split(' ')

    # 자동으로 예외 처리 해준다 # 내부적으로 다음에 실행할 값의 위치정보를 기억하고 있음
    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터

        return

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tommorrow')

wt = iter(wg)
print(wt,wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

