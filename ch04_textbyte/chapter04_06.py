#04.06 제대로 비교하기 위해 유니코드 정규화하기
s1 = 'café'         # e와 악센트를 결합한다
s2 = 'cafe\u0301'   # e와 악센트를 분리한다(출력시 s1과 동일하다.)
print(s1, s2)
print(len(s1),len(s2))
print(s1==s2)
# 코드 포인트 U+0301과 é 두개의 시퀀스를 동일하게 처리하는 것이 원칙이지만 파이썬은 두개의 코드 포인트 시퀀스를 보고 이 둘이 서로 동일하지 않다고 판단한다.

# 문제에 대한 해결책
# unicodedata.normalize()함수가 제공하는 유니코드 정규화를 활용해야 한다.
# 인수로 들어가는 것은 'NFC', 'NFD', 'NFKC', NFKD'가 있다.

#NFC와 NFD
# NFC는 가장 짧은 문자로 변환하는 한편 NFD는 기본문자와 결합문자로 구분한다.(결합 문자의 경우 2byte 사용)
from unicodedata import normalize
print(len(normalize('NFC',s1)),len(normalize('NFC',s2))) # 결합된 것을 기준으로 판단한다.
print(len(normalize('NFD',s1)),len(normalize('NFD',s2))) # 분리된 것을 기준으로 판단한다.
print(normalize('NFC',s1)==normalize('NFC',s2)) # 변환 시 같은 문자로 판단한다.
print(normalize('NFD',s1)==normalize('NFD',s2)) # 변환 시 같은 문자로 판단한다.

# NFC는 키보드를 통해 입력 받는 방식으로 웹을 위한 W3C가 추천하는 문자 모델이다

#NFKC와 NFKD
# 여기서 K가 추가된 것은 호환성을 의미한다.
from unicodedata import normalize, name
half='½'
print(normalize('NFKC',half)) # NFKC를 통해서 1/2로 변환한다. 이도 검색 편의를 위해서 사용될 수 있다.
four_squared = '42'
print(normalize('NFKC',four_squared)) #normalize를 통해서 4^2를 42로 변환하여 처리한다 ex 검색 결과를 표시할 때 4^2가 아닌 42도 보여준다면 더 좋을 것이므로.
micro = 'μ'
micro_kc=normalize('NFKC',micro) # micro도 표시는 같지만 2개가 존재하는데 이를 치환할 수 있다.
print(micro,micro_kc)

print(ord(micro),ord(micro_kc))
print(name(micro),name(micro_kc))

# 케이스 폴딩
# 모든 텍스트를 소문자로 변환하는 연산
# latine1 문자만 담고 있는 경우 s의 경우 s.casefold(), s.lower()를 실행한 결과가 동일

eszett = 'ß'
name(eszett)
eszett_cf = eszett.casefold()
print(eszett,eszett_cf)

# 정규화된 텍스트 매칭을 위한 유틸리티 함수
# NFC와 NFD는 안전하며 적절하게 문자열을 비교할 수 있도록 한다.
# NFC는 대부분의 애플리케이션에서 활용 가능한 최고의 정규화된 형태이며, str.casefold는 대소문자 구분을 없이 문자열을 비교하는 가장 좋은 방법이다.

def nfc_equal(str1,str2):
    '''nfc equal은 NFC변환을 했을 때 같은지에 대한 판단을 진행 "é" vs "e\u0301"은 같은가? => 참'''
    return normalize("NFC",str1)==normalize('NFC',str2)
def fold_equal(str1,str2):
    '''fold equal은 NFC변환 이후, casefold를 통해서 추가적인 변환을 진행함+소문자로의 변환도 함께 진행
    casefold는 소문자로 변환하는 것 뿐만 아니라 'ß'를 ss와 같이 치환하는 추가적인 과정이 있음
    '''
    return normalize('NFC',str1).casefold()==normalize('NFC',str2).casefold()

# nfc_equal fold_equal 여러 언어로 구성된 텍스트의 경우
s1 = 'café'
s2 = 'cafe\u0301'
print(s1==s2)
print(nfc_equal(s1,s2))
print(nfc_equal('A','a'))
print(nfc_equal('1/2','½'))
print(fold_equal(s1,s2))
print(fold_equal('A','a'))
print(fold_equal('1/2','½')) # 이는 NFKC와 같은 연산이 필요하다. 일반적으로는 다르다
print('½'.casefold()) # casefold는 몇몇 문자만 치환하여 준다. 여기에 ½는 포함되지 않는다.

# 극단적인 정규화 : 발음 구별 기호 제거하기
# 문자열 검색시 오탐을 줄이기 위한 방법

# 라틴어의 경우 장점이 있다
import unicodedata
import string

def shave_marks(txt):
    '''발음 구별 기호를 모두 제거한다.'''
    norm_txt = unicodedata.normalize('NFD',txt) # 모든 문자를 기본 문자와 결합 문자로 구별한다.(특수문자의 경우 2byte를 활용)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c)) # 결합 표시를 모두 걸러낸다.
    
    return unicodedata.normalize('NFC',shaved) # 문자를 재결합한다.

order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
print(shave_marks(order)) # 악센트를 전부 제거
greek = 'Ζέφυρος, Zéfiro'
print(shave_marks(greek)) # 악센트를 전부 제거함

def shave_marks_latin(txt):
    """라틴 기반 문자에서 발음 구별 기호를 모두 제거한다."""
    norm_txt = unicodedata.normalize('NFD', txt)  # <1>
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:   # <2>
            continue  # ignore diacritic on Latin base char
        keepers.append(c)                             # <3>
        # if it isn't combining char, it's a new base char
        if not unicodedata.combining(c):              # <4>
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)   # <5>
# END SHAVE_MARKS_LATIN

# 서양 활자(타이포그래픽)을 아스키로 변환하기
single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",  # <1>
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({  # <2>
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)  # <3>


def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)  # <4>


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))     # <5>
    no_marks = no_marks.replace('ß', 'ss')          # <6>
    return unicodedata.normalize('NFKC', no_marks)  # <7>
# END ASCIIZE
single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",  # <1> # ƒ:f와 같은 방식으로 치환하는 메소드(딕셔너리-매핑테이블)
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({  # <2>
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})
multi_map.update(single_map)  # <3> 딕셔너리에 없다면 추가하고, 있다면 수정한다.

print(multi_map)
print(single_map)
def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)  # <4>
# translate 함수(문자열) : dictionary(매핑 테이블)을 입력받으며 입력 받은 키를 값으로 치환한다.
# translate를 활용하기 위해서는 str.maketrans를 통해서 매핑 테이블을 작성해야 한다 단순 딕셔너리가 아닌 딕셔너리를 통해 변환된 문자의 정수값이 들어가야 한다.
# ex) aa='1234567' aa.translate(str.maketrans('1','2'))
def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))     # <5>
    no_marks = no_marks.replace('ß', 'ss')          # <6>
    return unicodedata.normalize('NFKC', no_marks)  # <7>
# END ASCIIZE