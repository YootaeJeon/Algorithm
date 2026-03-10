
import sys
from collections import deque

n = int(input())

queue = deque([])

for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif com[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])


# 시간초과 : 리스트를 이용해서 큐를 구현하려고 했으나 시간 초과 오류가 발생. 
# 리스트로 선언해서 pop(0)를 하게 되면, 첫 번째 요소를 pop 하고나서 나머지 요소들의 인덱스를 1칸씩 당기는 과정에서 O(n)의 계산량이 발생하기 때문
# import sys
# n = int(input())
# queue = []

# for i in range(n):
#     com = sys.stdin.readline().split()
#     if com[0] == 'push':
#         queue.append(com[1])
#     elif com[0] == 'pop':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue.pop(0))  
#     elif com[0] == 'size':
#         print(len(queue))
#     elif com[0] == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)
#     elif com[0] == 'front':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])
#     elif com[0] == 'back':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[-1])
