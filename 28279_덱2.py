import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dq = deque()   # stack → dq

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == '1':  # 앞에 추가
        dq.appendleft(int(cmd[1]))
        
    elif cmd[0] == '2':  # 뒤에 추가
        dq.append(int(cmd[1]))
        
    elif cmd[0] == '3':  # 앞에서 제거
        if dq:
            print(dq.popleft())
        else:
            print(-1)
            
    elif cmd[0] == '4':  # 뒤에서 제거
        if dq:
            print(dq.pop())
        else:
            print(-1)
            
    elif cmd[0] == '5':  # 크기
        print(len(dq))
        
    elif cmd[0] == '6':  # 비었는지
        print(0 if dq else 1)
        
    elif cmd[0] == '7':  # 앞 값
        if dq:
            print(dq[0])
        else:
            print(-1)
            
    elif cmd[0] == '8':  # 뒤 값
        if dq:
            print(dq[-1])
        else:
            print(-1)