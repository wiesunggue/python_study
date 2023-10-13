# 리스트가 답이 아닐 때

# 배열
# 리스트 안에 숫자만 들어간다면 array.array를 사용하는 것이 훨씬 더 효율적이다.
# 배열은 pop, insert, extend등 가변 시퀀스가 제공하는 모든 연산을 지원하며 빠르게 파일에 저장하고 읽어올 수 있는 frombytes와 tofile 메서드도 제공(c만큼 가볍다)

# 메모리 뷰
# 메모리 뷰는 배열 등 데이터 구조체를 복사하지 않고, 메모리를 공유할 수 있게 해준다.
# 데이터셋이 커지는 경우 아주 중요한 기법

# 표준 라이브러리는 아니지만 numpy와 scipy

# 덱과 기타 큐
# 덱 : 큐의 양쪽 어디서든 빠르게 삽입 및 삭제할 수 있도록 설계된 스레드 안전한 양방향 큐(최근 본 항목, 비슷한 것들의 목록을 유지할 때 사용)

import queue
queue.Queue()
# queue : 스레드에서 안전한 Queue, LifoQueue, PRiorityQueue 클래스를 제공
# 이런 클래스는 스레드 간에 안전하게 통신하기 위해서 사용됨
# 모두 0보다 큰 maxsize 인수를 생성자에 전달해서 바인딩 가능하다.
# 새로운 항목의 추가를 블로킹하고 다른 스레드에서 큐 안의 항목을 제거해서 공간을 확보해줄 때까지 기다림 => 활성화된 스레드 수를 조절하기 좋음

import multiprocessing
# multiprocessing : queue.Queue와 비슷하지만 프로세스간 통신을 위해서 설계된 고유한 Queue 클래스를 구현한다.
# 태스크 관리에 특화된 multiprocessing.JoinableQueue 클래스도 제공

import asyncio
# Queue, LifoQueue, PriorityQueue, JoinableQueue를 제공하지만 비동기 프로그램이 환경에서 작업하는데 주안점을 두고 있다.

import heapq
# 가변 시퀀스를 힙 큐나 우선순위 큐로 사용할 수 있게 해주는 heappush()와 heappop() 등의 함수를 제공한다.

# 커다란 실수 배열의 생성 저장 로딩
from array import array
from random import random
floats = array('d',(random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin','wb')
floats.tofile(fp) #array로 이루어진 파일 생성
fp.close()
floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp,10**7)
fp.close()
print(floats==floats2)


# 메모리 뷰
import array
numbers = array.array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv))

print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5]=4
print(numbers)