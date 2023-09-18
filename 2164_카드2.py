
''' 의사코드
input 6     > output 4

6 스택 6 5 4 3 2 1 pop(1)  맨 아래(2) 현 상태 스택 2 6 5 4 3 
                   pop(3) 맨 아래(4) 현 상태 스택 4 2 6 5 
                   pop(5) 맨 아래(6) 현 상태 스택 6 4 2 
                   pop(2) 맨 아래(4) 현 상태 스택 4 6 
                   pop(6) >>>>>>>>>>>>>>>>>>>>> 4 출력
'''
from collections import deque
#import sys
#input= sys.stdin.readline().split()

#큐 접근 : 시간  초과 발생 > 데큐이용
n = deque(range(1, int(input())+1,))

while len(n) != 1:
    n.popleft()
    n.rotate(-1)
print(n[0])