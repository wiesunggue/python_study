# 5.4 일곱 가지 맛의 콜러블 객체
# 호출 연산자인 ()는 사용자 정의 함수 이외에도 다른 객체에도 적용할 수 있다.
# 호출할 수 있는지 알아보려면 callable() 내장 함수를 사용한다.

# callable 7가지 종류
# 사용자 정의 함수, 내장 함수, 내장 메서드, 메서드, 클래스, 클래스 객체, 제너레이터 함수

# 사용자 정의 함수
# def문이나 람다 표현식으로 생성된다

# 내장 함수
# len()이나 time.strftime()처럼 C언어로 구현된 함수(CPython의 경우)

# 내장 메서드
# dict.get()처럼 C언어로 구현된 메서드

# 메서드
# 클레스 본체에 정의된 함수

# 클래스
# 호출될 때 클래스는 자신의 __new__() 메서드를 실행해서 객체를 생성하고, __init__()으로 초기화한 후, 최종적으로 호출자에 객체를 반환한다.
# 파이썬에는 new 연산자가 없으므로 클래스를 호출하는 것은 함수를 호출하는 것과 동일하다
# (일반적으로 클래스를 호출하면 해당 클래스의 객체가 생성되지만, __new__()메서드를 오버라이딩하면 다르게 작동시킬 수도 있다)
# 19.1.3절 __new__를 이용한 융통성 있는 객체 생성에서 다르게 작동하는 예를 설명한다

# 클래그 객체
# 클래스가 __call__()메서드를 구현하면 이 클래스의 객체는 함수로 호출될 수 있다.
# 5.5절 사용자 정의 코러블형을 참고하라

# 제너레이터 함수
# yield 키워드를 사용하는 함수나 메서드. 이 함수가 호출되면 제너레이터 객체를 반환한다.

print(abs, str, 13)
print([callable(obj) for obj in (abs, str, 13)])