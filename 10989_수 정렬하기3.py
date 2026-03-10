import sys

input = sys.stdin.readline

# 백준 10989 수 정렬하기 3 는 2751과 완전히 다른 문제입니다. 
# 핵심은 메모리 제한입니다.

'''
arr = []
for i in range(n):
    arr.append(int(input()))

만약 N = 10,000,000이면 정수 1000만개 저장

1. 문제 조건
N ≤ 10,000,000
수의 범위: 1 ~ 10,000
메모리 제한: 8MB

2. 파이썬에서 int 메모리

파이썬 int 하나는 약28 byte정도 사용합니다.
그래서 10,000,000 × 28 byte ≈ 280MB

3. 이 문제의 핵심 아이디어
숫자 범위가 매우 작습니다.
1 ~ 10000
그래서 Counting Sort (계수 정렬)을 사용해야 합니다.

4. 해결 방법

숫자 개수만 세는 배열을 만듭니다.

index = 숫자
value = 등장 횟수

예

입력
5
2
3
2
1
3

배열
count[1] = 1
count[2] = 2
count[3] = 2
'''
#import sys
#input = sys.stdin.readline

n = int(input())

count = [0] * 10001  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0...0]

for _ in range(n): # 5
    num = int(input())    
    count[num] += 1   # count[5] 의 결과값에 +1   2번 똑같은 결과가 나오면 count[5] 의 결과값은 최종 2

for i in range(10001):      # i가 0부터 10000까지 한 번씩 확인됩니다.
    for _ in range(count[i]):  # 누적된 결과 확인으로 출력 
        print(i)               # 만약 count[i] = 0이면 range(0)이라서 한 번도 안 돕니다.