import sys
input = sys.stdin.readline

MAX = 246912

# 에라토스테네스의 체
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if prime[i]:         #시작 # 끝  # 증가 단위
        for j in range(i * i, MAX + 1, i):
            prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if prime[i]:
            count += 1
            
    print(count)
    
# i =2, > 4,6,8.... false 제거됨 ...
# i =3, > 9, 12 ,15...false 3 소수 ...
# i = 4  이미 제거되서 실행 x 
# i= 5, > 25, 30, 35,40..false 5소수...