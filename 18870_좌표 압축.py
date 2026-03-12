'''

N = int(input())
arr = list(map(int,input().split()))
result=[0]*N

for i, check in enumerate(arr):  # 순서대로 선택
    for index in range(N):
        if check == arr[index]:
            pass
        elif  check > arr[index]:
            result[i]+=1 

                        
print(result)

# 좌표 압축은 서로 다른 값 기준입니다.
# 자기보다 작은 값의 개수를 세고 있습니다.
# 중복도 모두 세고 있음

첫 번째 값

check = 1000

전체 배열 비교

1000 > 999 → +1
1000 > 999 → +1
1000 > 999 → +1

그래서

result = 3

사실 지금 코드 아이디어는 Rank 계산 알고리즘에 더 가깝..?
틀림..ㅠ 
-----------------------------------------------
5
2 4 -10 4 -9 > 2 3 0 3 1

1.중복제거 
2. 1차 정렬
-10 -9 2 4 
  0  1 2 3
3. 재배열
    2 4 -10 4  -9
    2 3   0  3  1 

6
1000 999 1000 999 1000 999 > 1 0 1 0 1 0

1.중복제거 
2. 1차 정렬
999 1000
0     1

3. 재배열
1000 999 1000 999 1000 999
1     0    1    0   1   0
'''

N = int(input())                             # 6개
arr = list(map(int,input().split()))         # 1000 999 1000 999 1000 999

sorted_arr = sorted(set(arr))  # 999 1000

dic = { v:i for i,v in enumerate(sorted_arr)}
print(dic)

for num in arr: # 1000 999 1000 999 1000 999 
    print(dic[num], end=' ') # 딕셔너리 key 1000의 ,value 값 나오기 