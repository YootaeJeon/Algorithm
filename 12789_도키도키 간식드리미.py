n = int(input()) # 5 
standing = list(map(int, input().split())) # 5 4 1 3 2 
stack = []
target = 1
 
while standing: # 5 4 1 3 2 
    if standing[0] == target:  #  만일 1 번이 들어온다면 내보낸다. 2번..3..번..4..번..5번...
        standing.pop(0)
        target += 1
    else:
        stack.append(standing.pop(0)) # stading에서 첫 번째 값을 stack에 넣는다.
 
    while stack:
        if stack[-1] == target:  # stack에서 맨 마지막 값이 target 값이면 뺀다.
            stack.pop()
            target += 1
        else:
            break
 
if not stack: 
    print('Nice')
else:
    print('No')
 
# 혹은 이렇게 작성해도 된다.
# print('Nice' if not stack else 'No')