# 동전 1
# https://www.acmicpc.net/problem/2293

# 1,2,5 원 동전이 있는 상태에서 2원으로 4원을 만들려면
# 2원을 만들 수 있는 경우의 수에 기존에 4원을 만들 수 있는 경우의 수 를 더하면됨.
# 기존 1원을 가지고 4를 만드는 경우 -> 1,1,1,1 로 한 개.
# 2원을 가지고 만드려면 2원을 만드는 경우의수 -> 1,1 & 2 이렇게 2가지 에서 2만 더하면 되기 때문에
# dp[4] = dp[4] + dp[4-coin]

n,k = map(int, input().split())

dp = [0] * 10001
dp[0] = 1
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()

for coin in coins:
    for i in range(coin,k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[k])