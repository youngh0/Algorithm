# 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

n = int(input())

# 0,1,2,3,4,5,6,7,8,9 가 나타나는 빈도 수 테이블
dp = [[0,0,0,0,0,0,0,0,0,0] for _ in range(n+1)]

# 1자리 수 일 때는 0을 제외한 1~9까지 1번씩 나타남
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        # 0은 이전 자리수의 1에서만 0이 나올 수 있음
        if j == 0:
            dp[i][j] = dp[i-1][1]

        # 9역시 이전 자리수의 8에서만 나올 수 있음
        elif j == 9:
            dp[i][j] = dp[i-1][8]

        # 1 ~ 8은 이전 자리수 -1, +1에서 나올 수 있음
        else:
            dp[i][j] = dp[i - 1][j-1] + dp[i - 1][j+1]

print(sum(dp[n]) % 1000000000)