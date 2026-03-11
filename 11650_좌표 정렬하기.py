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

# 틀렸음 -> 자료형 때문
n = int(input())
arr = []
for i in range(n):
    arr.append(input().split()) # 좌표가 문자열 리스트로 저장
    # 문자열 정렬은 숫자 크기가 아니라 문자 순서로 비교합니다.
arr.sort()

for i in arr:
    print(' '.join(i))

'''

n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())

arr.sort()

for i in arr:
    print(' '.join(i))
