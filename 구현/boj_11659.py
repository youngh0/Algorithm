# 구간합 구하기4
# https://www.acmicpc.net/problem/11659

# 2 ~ 5까지의 합은
# idx 5까지의 합 - idx (~2)까지의 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [0]
array = list(map(int, input().split()))
nums.extend(array)

dp = [0] * (n+1)

for i in range(1,n+1):
    dp[i] = nums[i] + dp[i-1]

# print(dp)

for _ in range(m):
    start, end = map(int, input().split())

    print(dp[end]-dp[start-1])