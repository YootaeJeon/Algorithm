N,M = map(int,input().split())

while M > 0:
    n,m = M, N % M

lcm = N*M // n
print(lcm)
    