# 근데 1초인데 흠 ... 우선 생각나는 대로 해보기 

# 1,000이하인거 꼭 확인할 것...이중for문가능
'''
s[0:1] → a
s[0:2] → ab
s[0:3] → abc

s= ababc

i-0
j-1~5 s[0:1] s[0:2] s[0:3] s[0:4] s[0:5] 
         a     ab     aba    abab   ababc 
         
i-1
j-2~5  s[1:2] s[1:3] s[1:4] s[1:5]
          b     ba     bab   babc 
  
'''
s = input()

result = set()

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        result.add(s[i:j])

print(len(result))