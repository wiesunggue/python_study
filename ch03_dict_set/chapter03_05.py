# 매핑형
from collections import OrderedDict
# 키를 삽입한 순서를 유지해서 순서를 예측할 수 있다
# popitem()은 가장 마지막에 삽입한 항목을 꺼내지만
# popitem(last=True)를 통해서 처음 삽입한 항목을 꺼낸다.

from collections import defaultdict

from collections import ChainMap
# 매핑들의 항목을 가지고 있으며 한번에 모두 검색할 수 있다.
# 각 매핑을 차례로 검색하고 그중 하나라도 있으면 성공

import builtins # 사용법을 좀 더 봐야 할듯?
pylookup = ChainMap(locals(),globals(),vars())

from collections import Counter
# 모든 키에 정수형 카운터를 가지고 있는 매핑형

ct = Counter('abracadabra')
print(ct)
ct.update('aaaaazzz')
print(ct)

print(ct.most_common(2))

from collections import UserDict
# 표준 dict처럼 작동하는 매핑을 순수 파이썬으로 구현한 클래스
