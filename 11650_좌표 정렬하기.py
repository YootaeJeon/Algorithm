'''
5
3 4
1 1
1 -1
2 2
3 3
===
1 -1
1 1
2 2
3 3
3 4
'''

n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())

arr.sort()

for i in arr:
    print(' '.join(i))
