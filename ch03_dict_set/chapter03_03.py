# 공통적인 매핑 메소드
# collections 모듈의 defaultdict와 OrderedDict클래스가 구현하는 메소드
#                   dict        defaultdict         OrderedDict     설명
# d.clear           O               O                   O           모든 항목을 제거한다
# d.__contains__(k) O               O                   O           k in d
# d.copy()          O               O                   O           얕게 복사한다
# d.__copy__()                      O                               copy.copy()를 지원한다
# 이외에도 ... default_factory, __delitem__, fromkeys, get, __getitem__, items, __iter__, keys, __len__, __missing__, move_to_end,
# pop, popitem, __reversed__, setdefault, __setitem__, update, values와 같은 모듈이 존재한다.

# default_factory : defaultdict전용 메소드 => 빠진 값을 불러오기 위해 __missing__메소드를 불러오는 콜러블
# __missing__ : defaultdict전용 메소드 => __getitem__이 k키를 찾을 수 없을 때 호출한다
# move_to_end(k) : OrderedDict전용 메소드 => 앞이나 뒤에서 k개의 항목을 이동한다
# setdefault(k,[default]) dict, defaultdict, OrderedDict모두 사용가능 => k in d가 참이면 d[k]를 반환하고, 아니면 d[k] = default로 설정하고 이 값을 반환한다
# update(k,[**kargs]) : dict, defaultdict, OrderedDict모두 사용가능 => (키, 값) 쌍의 매핑이나 반복형 객체에서 가져온 항목들로 d를 갱신한다.

from collections import defaultdict
from collections import OrderedDict # 키를 삽입한 순서를 유지해서 순서를 예측할 수 있다


# update 메서드가 첫 번째 인수 m을 다루는 방식은 덕 타이핑의 대표적인 사례
# m이 keys() 메서드를 가지고 있는지 확인 한 후 만약 메서드를 가지고 있으면 매핑이라고 간주한다
# keys() 메서드가 없으면 update() 메서드는 m의 항목들이 (키,값) 쌍으로 되어 있다고 간주하고, m을 반복한다.
# 대부분의 매핑은 update와 같은 논리로 구현함

# 사용 예시
dict_example = {'림코딩': 30, '김갑환': 33, '장고환': 23}
print(dict_example)

dict_example.update({'림코딩':33,'최번개':26})

#존재하지 않는 키를 setdefault로 처리하기
import sys
import re

WORD_RE = re.compile(r'\w+')
index = {}

with open(sys.argv[1],encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            occurrences = index.get(word,[])
            occurrences.append(location)
            index[word] = occurrences
            
for word in sorted(index, key=str.upper):
    print(word, index[word])
    
# 가장 좋은 방법
index.setdefault('10',[]).append(1234)
print(index)

