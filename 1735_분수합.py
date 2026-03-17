# a,b = map(int,input().split())
# c,d =  map(int,input().split())

# # 최소공배수 구하고 그거에 맞게 분자에 곱해주기?
# def gcd(a,b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# result_gcd = gcd(b,d) # 왜 5?

# lcm =  b*d // result_gcd


# 분모 = lcm
# 곱하기_1 = lcm // b
# 곱하기_2 = lcm // d
# 분자 = a*곱하기_1 + c*곱하기_2
# print(분자, lcm)
##############################################
a,b = map(int,input().split())
c,d = map(int,input().split())

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수
result_gcd = gcd(b,d)  # 최대공약수
lcm = b*d // result_gcd # 최소공배수

# 분자 계산
분자 = a*(lcm//b) + c*(lcm//d)

# 핵심
g = gcd(분자, lcm)  #기약분수

print(분자//g, lcm//g)