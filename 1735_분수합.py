a,b = map(int,input().split())
c,d =  map(int,input().split())

# 최소공배수 구하고 그거에 맞게 분자에 곱해주기?
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

result_gcd = gcd(b,d) # 왜 5?

lcm =  b*d // result_gcd


분모 = lcm
곱하기_1 = lcm // b
곱하기_2 = lcm // d
분자 = a*곱하기_1 + c*곱하기_2
print(분자, lcm)