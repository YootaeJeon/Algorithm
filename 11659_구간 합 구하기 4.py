import sys
input = sys.stdin.readline

# + 계속 시간 초과가 나서 검색을 해봤는데, 파이썬의 경우 input()이 아닌 sys.stdin.readline()을 써야 시간초과가 나지 않는다고 한다.
# 합 배열 공식
#A[i]
#S[i] = S[i-1] + A[i]

# 구간 합 공식
#S[j] - S[i-1]

data_n, q_n = map(int,input().split())  # 데이터 개수 5 , 질의개수 3
data_range = list(map(int,input().split())) # 5개 : 5 4 3 2 1 
sum_data_range = [0] # 합 배열 변수 선언 
temp =  0 # 변수 선언 


for i in data_range: # 5 4 3 2 1
    temp = temp + i
    sum_data_range.append(temp)

#print(sum_data_range)

for i in range(q_n):
    s, e = map(int, input().split())
    print(sum_data_range[e]-sum_data_range[s-1])
