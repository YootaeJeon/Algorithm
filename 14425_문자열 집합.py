import sys
input = sys.stdin.readline
N,M = map(int,input().split())

S = []
check = []
count = 0 
for i in range(N):
    S.append(input())

for i in range(N):
    check.append(input())
    
for i in S:
    for j in check:
        if j in i:
            count+=1
        
print(count)

    