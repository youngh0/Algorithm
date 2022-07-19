# 카드 구매하기
# https://www.acmicpc.net/problem/11052

n = int(input())
cards = list(map(int,input().split()))

dp = [0] * (n+1)


# 2개 팩으로 3장의 카드를 최대 값으로 살 수 있는 경우
# 1. 지금까지 계산된 1장의 카드를 최대 값으로 살 수 있는 경우 + 2팩 가격
# 2. 지금까지 계산된 3장의 카드를 최대 값으로 살 수 있는 경우
# dp[3] = max(1,2)
for i in range(n):
    for j in range(i+1, n+1):
        dp[j] = max(cards[i] + dp[j-i-1], dp[j])


print(dp[n])
