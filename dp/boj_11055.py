num = int(input())

sequence = (list(map(int,input().split())))
# sequence.insert(0,0)

dp = sequence[:]
ans = 0

for i in range(num):
    for j in range(i-1,-1,-1):
        if sequence[i] > sequence[j] and dp[j] + sequence[i] > dp[i]:
            dp[i] = dp[j] + sequence[i]
    ans = max(ans,dp[i])

# print(dp)

print(ans)


# print(max(dp[0][num], dp[1][num]))