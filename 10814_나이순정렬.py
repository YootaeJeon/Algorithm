n = int(input())

age_name_arr = []

for i, _ in enumerate(range(n)):
    x, y = map(str, input().split())
    age_name_arr.append((i,int(x),y))
    
# print(age_name_arr)

age_name_arr.sort(key=lambda x: (x[1], x[0]))

for w in age_name_arr:
    print(w[1], end=" ")
    print(w[2])