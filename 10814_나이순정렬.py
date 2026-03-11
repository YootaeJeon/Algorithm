'''
n = int(input())

age_name_arr = []

for i, _ in enumerate(range(n)):
    x, y = map(str, input().split())
    age_name_arr.append((i,int(x),y))
    
# print(age_name_arr)

age_name_arr.sort(key=lambda x: (x[1], x[0]))

for w in age_name_arr:
    print(w[1], end=" ")
    print(w[2])
    

정답은 맞음
GPT 풀이
'''
    
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    age, name = input().split()
    arr.append((int(age), name))

arr.sort(key=lambda x: x[0])

for age, name in arr:
    print(age, name)