N = int(input())

for _ in range(N):
    A, B = map(int, input().split())

    gcd = 1
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            gcd = i  # 최대공약수
    
    lcm = A * B // gcd # 최소공배수
    print(lcm)