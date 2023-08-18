n = input()
score = list(map(int,input().split()))
mymax = max(score)
sum = sum(score)

# (A / M*100  +  B/M*100  + C/M*100) / 3 = (A+B+C)*100/M/3 
print(sum*100/mymax/int(n))
