'''
1 > 666
2 > 1666
3 > 2666
6 > 5666


187 > 66666
500 > 166699

1~666 시작하면서 666 걸리면 1...

1~n번 시작하면서 666 걸리면 count + 1 해주기 



1~66666 번까지 돌면 count는 187번 
1~166699 번까지 돌면 count 는 500번

'''

n = int(input())
count = 0
target = 666

# 범위 안정해져있으니 While..돌리자 / x : for i in range():
while True:
    if "666" in str(target):
        count +=1
        
        if count == n:
            print(target)
            break

    target+=1 