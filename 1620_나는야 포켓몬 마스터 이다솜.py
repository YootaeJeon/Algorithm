# # 시간초과
# import sys
# input = sys.stdin.readline

# N, M = map(int,input().split())

# pkm_list = {}

# for number in range(N):
#     pkm_list[number]=str(input())
    
# for n in range(M):
#     q = input().strip()
    
#     if q.isdigit(): # 5 ...이런 숫자면 key니깐 검색
#         print(pkm_list[int(q)])  # 이름 출력 
#     else:           # 이름으로 검색 (value) 
#         for key, value in pkm_list.items():
#             if value == q:
#                 print(key)

''' 
질문 M개
↓
이름 검색할 때
↓
dict 전체 탐색

N ≤ 100000
M ≤ 100000
이름 찾을 때 전체 탐색을 하게 됩니다. > 시간초과
'''
# GPT 코드
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(1, N+1):
    name = input().strip()
    name_to_num[name] = i # 이름에다가 번호
    num_to_name[i] = name

for _ in range(M):
    q = input().strip()
    
    if q.isdigit():
        print(num_to_name[int(q)])
    else:
        print(name_to_num[q])