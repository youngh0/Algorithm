# 곱셈
# https://www.acmicpc.net/problem/1629

a,b,c = map(int, input().split())

def pow(b):
    if b == 1:
        return a % c

    res = pow(b//2)
    if b % 2 == 0:
        return res * res % c
    else:
        return (res * res * a % c)

print(pow(b))

