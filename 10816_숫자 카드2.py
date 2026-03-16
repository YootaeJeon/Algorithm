''' 
10
6 3 2 10 10 10 -10 -10 7 3 

8
10 9 -5 2 3 4 5 -10

>> 3 0 0 1 2 0 0 2   # 하니씩 전체보는건 N^2 걸릴거고...


# _dict={}
'''

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
queries = list(map(int, input().split()))

_dict = {}

for c in cards:
    if c in _dict:   # 있으면 증가해라
        _dict[c] += 1
    else:            # 없으면 1로 넣어라
        _dict[c] = 1
    print(_dict)


for q in queries:
    print(_dict.get(q, 0), end=" ")