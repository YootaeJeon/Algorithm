# 근데 1초인데 흠 ... 우선 생각나는 대로 해보기 

# 1,000이하인거 꼭 확인할 것...이중for문가능

s = input()

result = set()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        result.add(s[i:j])

print(len(result))