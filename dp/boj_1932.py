# 정수 삼각형
# https://www.acmicpc.net/problem/1932

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = array[0][0]

for i in range(1,n):
    dp[i][0] += (dp[i-1][0] + array[i][0])
    dp[i][i] += (dp[i-1][i-1] + array[i][i])

# 굿노트 보면 풀이 그림 있음
# (2,1)경로까지의 최대값을 구하려면 dp[1,1] + array[2,1]과 dp[1,0] + array[2,1]중에
# 큰 값으로 결정하는 식으로 하면 왼쪽 아래 대각선, 오른쪽 아래 대각선만 선택한 경로의 최대값 구할 수 있음
for i in range(2,n):
    for j in range(1, i):
        cur = array[i][j]
        dp[i][j] = max(dp[i-1][j-1] + cur, dp[i-1][j] + cur)

print(max(dp[n-1]))