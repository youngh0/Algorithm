# 스티커
# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

test_cases = int(input())

for _ in range(test_cases):
    stickers_num = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * stickers_num for _ in range(3)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    for n in range(1,stickers_num):
        # 0행의 n번 째 스티커 뜯은 경우
        dp[0][n] = max(dp[1][n-1], dp[2][n-1]) + stickers[0][n]

        # 1행의 n번 째 스티커 뜯은 경우
        dp[1][n] = max(dp[0][n - 1], dp[2][n - 1]) + stickers[1][n]

        # i번 째 열의 스티커를 뜯지 않은 경우
        dp[2][n] = max(dp[0][n-1], dp[1][n-1])

    answer = max(dp[0][-1], dp[1][-1])
    answer = max(answer, dp[2][-1])
    print(answer)