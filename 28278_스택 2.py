# 한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야 할 때는 input()으로 입력 받는다면 시간초과가 발생할 수 있다.

import sys
#input = sys.stdin.readline
N = int(input()) #명령문 9개 (라인입력)
stack = []

for _ in range(N):
    command = input().rstrip()
    
    #push
    if len(command) > 2:
        stack.append(int(command[2:]))
    
    #pop
    elif command == '2':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    
    #size
    elif command == '3':
        print(len(stack))

    #empty
    elif command == '4': # 비면 1, 아니면 0 
        print(1 if len(stack)==0 else 0)
    
    #top
    elif command == '5': # 맨위 출력 , 아니면 -1
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            
    #print(command)
    #print(stack)


# for i in N: # 9번 돌면서 명령 수행 (stack)
#     cmd, x = int(input().split())

#     if cmd == 1 : 
#         Arr.append(x)
#     elif cmd == 2 :
#         x = Arr.pop()
#         print(x)
#     elif cmd == 3 :
#         print(len(Arr)) #정수 개수 출력
#     elif cmd == 4 : # 비엇으면 1, 아니면 0
#         if Arr == Null
