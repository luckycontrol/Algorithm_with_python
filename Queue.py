from collections import deque
from queue import PriorityQueue
from queue import Queue

queue = deque([1, 2, 3])
# 오른쪽에 삽입
queue.append(4)
# 왼쪽에 삽입
queue.appendleft(5)
# 오른쪽 삭제
queue.pop()
# 왼쪽 삭제
queue.popleft()

que = Queue()
# 삽입
que.put(1)
# 삭제
que.get()

pque = PriorityQueue()
# 삽입
pque.put(1)
# 삭제
pque.get()
# 정렬기준 변경 -> 1번 바나나, 2번 사과, 3번 체리
pque.put((2, 'Apple'))
pque.put((1, 'Banana'))
pque.put((3, 'Cherry'))
