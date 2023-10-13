# Chapter06-04
# Future 동시성 python 3.2 부터 지원
# 비동기 작업 실행 순차적이지 않은 작업
# A -> B -> END
# 지연 시간(Block) CPU 및 리소스 낭비 방지 -> (FILE)Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.futures
# 1. 멀티스레딩/ 멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures 사용법1
# concurrent.futures 사용법2
# global interface lock 오히려 단일 스레드를 쓰는 것 보다 연산 시간이 더 많이 걸림
# GIL : 두 개이상의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점을 방지하기 위해
#       GIL 실행, 리소스 전체에 락이 걸림 -> Context Switch(문맥 교환)

# GIL : 멀티프로세싱 사용, CPython 사용

import os
import time
from concurrent import futures

WORK_LIST = [10000, 100000, 1000000, 10000000]


# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n + 1))


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))
    # 시작 시간
    start_tm=time.time()
    result=[]
    # 결과 건수
    # ProcessPoolExecutor, ThreadPoolExecutor
    with futures.ProcessPoolExecutor() as executor:
        result = executor.map(sum_generator,WORK_LIST)

    # 종료 시간
    end_tm = time.time()-start_tm

    msg = '\n Result -> {} Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result),end_tm))


# 실행
if __name__ =='__main__':
    main()

# 현재 상황에서는 processpoolexecutor작업이 좀더 빠르다 (cpu를 사용하는 작업)
