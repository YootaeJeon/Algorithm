import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
arr = [int(input()) for _ in range(N)]

for n in arr:
    while True:
        if is_prime(n):
            print(n)
            break
        n+=1