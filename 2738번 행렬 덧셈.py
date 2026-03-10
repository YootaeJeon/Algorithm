A, B = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()

# 런타임 에러
# n, m = map(int, input().split())

# A = []
# B = []

# for i in range(n):
#     A.append(input().split())

# for i in range(m):
#     B.append(input().split())

# for row in range(n):
#     for col in range(n):
#         print(A[row][col] + B[row][col], end=' ')
#     print()