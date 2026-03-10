# 무조건 5개 각각 라인별로 들어옴
arr = []
# 10 40 30 60 30 
for i in range(5):
    arr.append(int(input()))

arr.sort() # 정렬해주기 

print(int(sum(arr)/5)) # 자연수
# 2 번쨰 중앙값 출력 3번째꺼 
print(arr[2]) 
