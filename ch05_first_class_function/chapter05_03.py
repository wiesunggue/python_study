# 5.3익명 함수
# lambda는 파이썬 표현식 내에 익명 함수를 생성
# 익명함수는 ㅊ
fruits = ['strawberry','fig','apple','cherry','raspberry','banana']
print(sorted(fruits,key=lambda word:word[::-1]))

# 런드의 람다 리팩토링 방법
# 람다가 하는 일이 무엇인지 설명하는 주석을 작성한다
# 잠시 주석을 주의 깊게 파악하고, 주석의 본질을 전달하는 이름을 생각해낸다.
# 주석을 제거한다.

