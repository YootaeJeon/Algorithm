import sys

input = sys.stdin.readline

'''
시간초과가 나는 이유는 정렬이 아니라 입출력 속도 때문임. (N ≤ 1,000,000)
즉 **백만 줄 입력 + 백만 줄 출력**이라서
기본 `input()` / `print()`가 느릴 수 있습니다.
'''


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
arr.sort()

for j in arr:
    print(j)
    