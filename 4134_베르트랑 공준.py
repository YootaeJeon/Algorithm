'''
조건으로 제어
n = int(input())

while n != 0:
    print("test")
    n = int(input())
'''

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    
    
    for i in range(n+1, 2*n + 1):
        if is_prime(i):
            count+=1
    
    print(count)