''' 
5
6   > 1     3  3 > 1                    | 3+3 로 1개 
8   > 1     2  3 5 7 > 3 5  > 1          | 3+5 로 1개 
10  > 2     2  3  5 7 > 3 7  > 2            | 3+7 , 5+5, 7+3 > 2개 (순서상관없음)
12  > 1     2  3  5  7 11 > 1                 |5+7 > 1개  
100 > 6     2 3 7 11 13 17 19 23 > 6개     | 6개나오나봐...

>>

n = 10

3 + 7 o
5 + 5 o
7 + 3 x (중복)

(왼쪽)  (오른쪽)

1   +   9
2   +   8
3   +   7   ← 여기까지 보면 충분
4   +   6
5   +   5   ← 중앙 (n/2)
6   +   4   ← 여기부터는 중복
7   +   3
8   +   2
9   +   1

'''
import sys
input = sys.stdin.readline

MAX = 1000000

# 소수 구하기
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False

# 소수인것만 True
for i in range(2, int(MAX ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, MAX + 1, i): # 중복은 이전단계에서 제거됨
            prime[j] = False

t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    
    for i in range(2, n // 2 + 1):
        # 10일 경우   prime[0 1 2 3 4 5 6 7 8 9 10...]
        # prime[2] = 2  prime[8] = 8
        if prime[i] and prime[n - i]: # i는 2부터 계속 증가하면서 prime[n-i]가 둘다 소수면  
            count += 1
            
    print(count)
