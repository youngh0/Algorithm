# 동전 2
# https://www.acmicpc.net/problem/2294

n,k = map(int, input().split())

coins = []
dp = [1e9] * (k+1)
dp[0] = 0
for _ in range(n):
    coins.append(int(input()))


# 5원 동전을 이용해 7원을 최소개수로 사용하는 경우
# -> 1. 기존 1원 동전을 이용해 2원을 만든거 + 1(5원 동전 하나),
#    2. 기존 1원으로 7원 만든 경우 : 7개
# min(1,2)

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
if dp[k] == 1e9: dp[k] = -1
print(dp[k])