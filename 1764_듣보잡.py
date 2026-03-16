import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = set()
B = set()

for _ in range(N):
    A.add(input().strip())

for _ in range(M):
    B.add(input().strip())

result = A & B

print(len(result))

for name in sorted(result):
    print(name)