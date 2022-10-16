num = int(input())

sequence = list(map(int, input().split()))

dp = [1] * num

ans = 0

for i in range(num):
    for j in range(i-1,-1,-1):
        if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
    ans = max(ans,dp[i])

# print(dp)
# print(dp[num-1])
print(ans)
