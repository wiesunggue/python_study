# 5.5 사용자 정의 콜러블형
# 파이썬 함수가 실제 객체일 뿐만 아니라, 모든 파이썬 객체가 함수처럼 동작하게 만들 수 있다.
# 단지 __call__() 인스턴스 메서드를 구현하면 된다

import random

class BingoCage:
    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pcik from empty BingoCage') # 비어있을 경우 예외를 출력한다
    
    def __call__(self): # bingo.pick을 단축한 형태로 bingo()로 사용가능하게 정의한다.
        return self.pick()
    
bingo = BingoCage(range(100))
print(bingo.pick())
print(bingo())
print(callable(bingo))

