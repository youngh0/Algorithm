n = int(input())

array = list(map(int, input().split()))

dp = [0,array[0]]
dp.append(max(array[0], array[1]))

for i in range(3,n+1):
    max_val = max(dp[i-1], array[i-1]+dp[i-2])
    dp.append(max_val)

print(dp[n])
