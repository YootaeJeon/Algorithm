'''
틀림 - 출력형식..아...
-------------------------------------
input_num = int(input())
list_array =[]

for i in range(input_num):
    list_array.append(int(input()))
    
print(sorted(list_array))  >> 아 세로 출력이었음
-----------------------------------
수정-좋은 정렬이 아님 /맞긴 맞으나...횟수줄일수있음
input_num = int(input())
list_array =[]

for i in range(input_num):
    list_array.append(int(input()))
    
# print(list_array) # [5 4 3 2 1]
'''

'''
# i = 0 (값 5)
    j가 돌면서 비교

    5 < 4 ? False
    5 < 3 ? False
    5 < 2 ? False
    5 < 1 ? False
# i = 1 (값 4)
    j 비교
    4 < 5 → True → swap
    결과
    [4,5,3,2,1]
    
작은 값이 발견되면
앞으로 이동
'''

'''
                      
for i in range(input_num):  # 값 5넣으면 맨 앞 부터시작
    for j in range(input_num): # 값 5넣으면 맨 앞 부터 시작 
        if list_array[i]<list_array[j]:   # i 배열이 j 배열보다 작으면 바꿔라. 
            temp  > 런타임 에러 
            temp = list_array[i]
            list_array[i] = list_array[j]
            list_array[j] = temp;
        
print(list_array)
-----------------------------------------

*swap은 이렇게 더 많이 씀
temp = list_array[i]
list_array[i] = list_array[j]
list_array[j] = temp

변경 파이썬버전
list_array[i], list_array[j] = list_array[j], list_array[i]
-------------------------------------
버블정렬
'''
n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in arr:
    print(i)