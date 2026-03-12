'''
★ (존재여부확인 → set)

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

S = []
check = []
count = 0 

for i in range(N):
    S.append(input().strip())

for i in range(M):
    check.append(input().strip())
    
for i in S:
    for j in check:
        if j == i:
            count+=1
        
print(count)

# 시간초과 : input = sys.stdin.readline 추가 
# "art" in "startlink"  → True
하지만 문제는 완전히 같은 문자열인지 확인해야 합니다.
# N ≤ 10,000M ≤ 10,000
계산량
10000 × 10000
= 100,000,000 → 시간초과 가능
'''

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

S = set()

for _ in range(N):
    S.add(input().strip())

count = 0

for _ in range(M):
    word = input().strip()
    if word in S:
        count += 1

print(count)