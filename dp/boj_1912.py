# 연속합
# https://www.acmicpc.net/problem/1912
n = int(input())

array = list(map(int, input().split()))
dp = [0] * n

dp[0] = array[0]
res = array[0]

# 지금까지의 합에 자기 자신을 더한거랑
# 자기 자신 중 자기 자신이 더 크면 이전까지의 연속합은 버려
for i in range(1,n):
    dp[i] = max(array[i], dp[i-1] + array[i])
    res = max(dp[i], res)

print(res)
