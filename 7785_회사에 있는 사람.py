#######################################
# N = int(input())
# arr = []
# result = []
# for i in range(N):
#     x,y = map(str,input().split())
#     arr.append([x,y])

# for i in range(len(arr)):
#     if arr[i][1] == 'enter':
#         result.append(arr[i][0])
        
# print(result[-1])         
# 
# enter 들어가고 leave면 빠진다. 이걸로 접근해보자 
########################################
# dict 이름이 같으면 enter -> leave 최종만 남음
# N = int(input())
# dict = {}
# result = []

# for i in range(N):
#     x,y = map(str,input().split())
#     dict[x] = y

# for i in dict:  # aree , askar, ...등 key값
#     if dict[i]=='enter':
#         print(f"추가되었습니다. : {i}")
#         result.append(i)  #baha는 leave여서 추가 안됨
#     elif dict[i]=='leave':
#         print(f"삭제되었습니다. : {i}")
#         result.remove(i)  # 추가 된적 없는데 지우려니 에러
        
# print(sorted(result[-1]))

# 에러발생 
'''
문제 상황 예시

입력

Baha enter
Askar enter
Baha leave
Artem enter

dict에는 이렇게 저장됩니다.

{
 'Baha': 'leave',
 'Askar': 'enter',
 'Artem': 'enter'
}

이제 반복문 돌면
Baha → leave

하지만

result = []

아직 Baha가 result에 추가된 적이 없습니다.

그래서
result.remove("Baha")

→ ValueError 발생

list.remove(x): x not in list

'''
# 내 방식 코드 
N = int(input())
dict = {}
result = []

for i in range(N):
    x,y = map(str,input().split())
    dict[x] = y

for i in dict:  # aree , askar, ...등 key값
    if dict[i]=='enter':
        result.append(i)
        
for name in sorted(result,reverse=True):
    print(name)

        
