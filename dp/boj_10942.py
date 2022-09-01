import sys
input = sys.stdin.readline

n = int(input())
array = list(input().split())
m = int(input())
dp = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if array[i] == array[i+1]:
        dp[i][i+1] = 1

# 팰린드롬 조건
# ex) 0~3 번째 수열
# 0, 3번째 글자가 같고, 1~2가 팰린드롬이면 0~3도 팰린드롬
for i in range(2,n):
    for j in range(n-i):
        if array[j] == array[j+i] and dp[j+1][j+i-1] == 1:
            dp[j][j+i] = 1


for _ in range(m):
    s,e = map(int, input().split())

    print(dp[s-1][e-1])
