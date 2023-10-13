# 융통성 있게 키를 조회하는 매핑
# 키가 없으면 특별한 값을 반환하는 매핑
# 1. dict 대신 defaultdict를 활용
# 2. dict 등의 매핑형을 상속해서 __missing__()메서드를 추가하는 방법

# defaultdict의 사용
import collections
import sys
import re

WORD_RE = re.compile(r'\w+')

index = collections.defaultdict(list) # defaultdict(자료형) list, int, float, tuple등등 파이썬의 기본 자료형
with open('zen.txt', encoding='utf8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location) # word가 index내에 없으면 빈 리스트를 생성해서 index[word]에 할당하고 나서 반환하므로 append 연산은 언제나 성공한다.
            
            
for word in sorted(index, key=str.upper):
    print(word, index[word])
    
# missing 메서드가 정의된 dict
class StrKeyDict(dict): # dict 상속
    
    def __missing__(self,key):
        if isinstance(key, str): # 키가 문자열인지 확인한다. 확인하고, 없다면 KeyError을 반환한다.
            raise KeyError(key)
        return self[str(key)] # 키에서 문자열을 만들고 조회한다
    
    def get(self, key, default=None):
        try:
            return self[key] # self[key]를 활용해서 getitem메서드에 위임한다. => missing이 작동할 기회를 준다
        except:
            return default #KeyError이 발생하면 missing이 실패한 것이므로 default를 반환한다.
        
    def __contains__(self,key):
        return key in self.keys() or str(key) in self.keys() # 수정하지 않은 키를 검색하고 나서, 키에서 만든 문자열로 검색한다
    
d = StrKeyDict([('2','two'),('4','four')])
print(d['2'])
print(d['4'])
#print(d[1])
print(d.get(1,'N/A'))
print(2 in d, 1 in d)
print(d[2])