n = int(input())

for i in range(n):
    stack = []
    vps = list(input())
    count = 0
    for line in vps:
        if line =='(':
           count += 1
        elif line ==')':
           count -= 1
        
        if count <0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")

