#04.05 텍스트 파일 다루기
# 유니코드 샌드위치
# 1. bytes->str 디코딩
# 2. 100% str
# 3. str->bytes 인코딩

# 가능하면 빠르게 bytes를 str로 변환해야 한다.
# 출력할 때는 가능한 늦게 str을 bytes로 인고딩한다.

# 저장은 utf8로 해줌
open('cafe.txt','w',encoding='utf_8').write('café')

# 출력은 utf8이 아닌 시스템 기본 인코딩(Windows 1252, cp949등) 인코딩을 활용하여 읽게 된다.
# 해당 코드는 파이썬의 기본인코딩으로 utf-8을 활용하는 GNU/리눅스나 MAC OS X에서 코드를 실행하면 문제없이 동작한다(기본 언어가 utf-8이다)
print(open('cafe.txt','r').read())
# 이는 플랫폼에서의 호환성 문제를 발생시킨다.

fp = open('cafe.txt','w',encoding='utf_8')
print(fp)
fp.write('café')
fp.close()

import os
print(os.stat('cafe.txt').st_size) # 저장된 유티코드 문자 수를 반환
fp2 = open('cafe.txt')
print('fp2 : ',fp2)
print(fp2.encoding)
print(fp2.read())
fp3 = open('cafe.txt',encoding='utf_8')
print('fp3 : ',fp3)
print(fp3.encoding)
print(fp3.read())
fp4 = open('cafe.txt','rb') # 이진 모드로 글자를 읽음
print('fp4 : ',fp4) # fp1,2,3에서는 TextIOWrapper가 반환되지만 fp4에서는 BufferedReader객체가 반환된다
print(fp4.read()) #bytes가 반환된다.

# 기본 인코딩 설정
# 해당 코드는 운영 체제마다 다르게 동작한다.
# 따라서 기본 인코딩에 의존하지 않는 것이 가장 좋다.
import sys, locale
expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """
my_file = open('dummy','w')
for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30),'->',repr(value))
    
# 인코딩 설정을 필수로 해야한다!

print(locale.getpreferredencoding(do_setlocale=True)) # 사용자 환경 설정에 따라 텍스트 데이터에 사용되는 인코딩을 반환한다.
# 사용자 환경 설정은 시스템마다 다르게 표현되며, 프로그램 코드를 통해서 구할 수 없는 시스템이므로 이 함수가 반환하는 값은 추정치이다.

