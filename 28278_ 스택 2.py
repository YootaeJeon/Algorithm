'''
9  # 9개 정수를 스택에 넣기 
4           # 4: 스택이 비어있으면 1, 아니면 0을 출력한다. > 1 출력
1 3         # 1 X: 정수 를 스택에 넣는다. (1 ≤  ≤ 100,000)         3 넣기
1 5        # 1 X: 정수 를 스택에 넣는다. (1 ≤  ≤ 100,000)          5 넣기 
3          # 3: 스택에 들어있는 정수의 개수를 출력한다. > 2  출력
2          # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다 > 3 5 상황에서 5뺴고 5출력 > 5출력
5          # 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다. > 3출력 
2          # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다. > 3출력
2          # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다  > -1 
5          # 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다. > -1 


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

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == '1':  # push
        stack.append(int(cmd[1]))
        
    elif cmd[0] == '2':  # pop
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    elif cmd[0] == '3':  # size
        print(len(stack))
        
    elif cmd[0] == '4':  # empty
        print(0 if stack else 1)
        
    elif cmd[0] == '5':  # top
        if stack:
            print(stack[-1])
        else:
            print(-1)


'''

# 한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야 할 때는
# input()으로 입력 받는다면 시간초과가 발생할 수 있다.

import sys
input = sys.stdin.readline #시간초과왜뜨냐
N = int(input()) #명령문 9개 (라인입력)
stack = []

for _ in range(N):
    command = input().rstrip()
    
    #push
    if len(command) > 2:  # 입력이면 rstrip으로 인해 10 이상 가능 
        stack.append(int(command[2:]))
    
    #pop                  # 맨위 pop 하고 pop 출력
    elif command == '2':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    
    #size                # 사이즈 출력
    elif command == '3':
        print(len(stack))

    #empty               # 0으로 비면 1, 아니면 0
    elif command == '4': # 비면 1, 아니면 0 
        print(1 if len(stack)==0 else 0)
    
    #top                 #  pop 이 아닌 맨위의 top 출력
    elif command == '5': # 맨위 출력 , 아니면 -1
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            

    