N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_S = set()
B_S = set()

for _ in A:
    A_S.add(_)
    
for _ in B:
    B_S.add(_)

result = A_S ^ B_S

print(len(result))
