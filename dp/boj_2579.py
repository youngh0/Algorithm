# https://www.acmicpc.net/problem/2579
# 계단 오르기

# n이 3이상일 때
# 점화식 = max( score[i] + score[i-1] + dp[i-3],
#             score[i] + dp[i-2]
steps = int(input())

score = [0]
for i in range(steps):
    score.append(int(input()))

dp = [0] * 301

# print(score)
if steps == 1:
    print(score[1])
else:
    dp[1] = score[1]
    dp[2] = score[1] + score[2]
    for i in range(3,steps+1):
        # print(score[i] + score[i-1] + dp[i-3], score[i] + dp[i-2], i)
        dp[i] = max(score[i] + score[i-1] + dp[i-3], score[i] + dp[i-2])

    print(dp[steps])
