import sys
# input = sys.stdin.readline
arr=[]
str_input = input()
for i in str_input:
    arr.append(i)
    
arr.sort(reverse=True)

for i in arr:
    print(i, end="")    