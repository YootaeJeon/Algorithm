import sys
# input = sys.stdin.readline

n = int(input())
trees = [int(input()) for _ in range(n)]

# 간격 계산
dist = []
for i in range(1, n):
    dist.append(trees[i] - trees[i-1])

# 최대공약수 구하기
from math import gcd
g = dist[0]
for d in dist[1:]:
    g = gcd(g, d)

# 추가해야 할 나무 개수 계산
result = 0
for d in dist:  # 간격 4들어올때 계산, 6 들어올때 추가 개수 계산..등등...다 합하기
    result += (d // g) - 1

print(result)