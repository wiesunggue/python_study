# Chapter06-02
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램안에서 여러일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator Ex1

def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')


temp = iter(generator_ex1())
print(temp)

# print(next(temp))
# print(next(temp))
# print(next(temp)) next가 존재한다는 말은 for문에서 호출 가능함

for v in generator_ex1():
    print(v)

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())  # print하면 제너레이터가 나온다 즉, 그냥 접근 불가능하다

print(temp2)
for i in temp3:
    print(i)

# Generator Ex3(중요 함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby...

import itertools

gen1 = itertools.count(1, 2.5)  # 시작점, 증가 단위를 입력 무한하게 증가함
# 1000미만일 때까지만 증가하는 제너레이터
gen2 = itertools.takewhile(lambda n: n < 100, itertools.count(1, 2.5))
# 조건에 거짓일 때 출력 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

#for v in gen3:
#    print(v)

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1,11)])
for v in gen4:
    print(v)

# 연결1
gen5 = itertools.chain('ABCDE',range(1,11,2))

print(list(gen5))

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))

print(list(gen6))

# 개별
gen7 = itertools.product('ABCDE')
print(list(gen7))
# 개별
gen8 = itertools.product('ABCDE',repeat=2) # 5개의 문자로 만들 수 있는 모든 경우의 수를 만든다 (a, a)~(e, e)까지


# 그룹화 각각 개수만큼 반환
gen9 = itertools.groupby('AAABBCCCDDEE')
# print(list(gen9))

for chr, group in gen9:
    print(chr,' : ', list(group))
