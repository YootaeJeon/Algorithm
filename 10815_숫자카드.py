import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split())) # 1 2 3 4 5
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split())) # 1 2 3 4 5 6 7 8 

_dict = {}  # 속도는 dictionary!
for i in range(len(cards)): # i = 1 2 3 4 5 
    _dict[cards[i]] = 0  # 아무 숫자로 mapping

for j in range(M):
    if checks[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')
      
'''
 GPT 5.4 풀이
 #GPT
import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

for num in check:
    if num in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')

'''       