# list.sort()와 sorted() 내장 함수
# list.sort()는 사본을 만들지 않고, 리스트 내부를 변경해서 정렬함, 타깃 객체를 변경하고,
# 새로운 리스트를 생성하지 않았음을 알려주기 위해서 None를 반환 => 파이썬 전반적인 관례

# sorted() 내장 함수는 새로운 리스트를 생성해서 반환한다. => 불변, 제너레이터 등 모든 객체를 인수로 받을 수 있음

fruits = ['grape','raspberry','apple','banana']

# 정렬하는 다양한 방법들
print(sorted(fruits))
print(sorted(fruits,reverse=True))
print(sorted(fruits,key=len))
print(sorted(fruits,key=len,reverse=True))
print(fruits)
print(fruits.sort())
print(fruits)

