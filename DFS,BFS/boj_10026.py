# https://www.acmicpc.net/problem/10026
# 적록색약

import sys
sys.setrecursionlimit(10**6)

n = int(input())

maps = [list(input())for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y, flag):
    if visited[x][y] == 1:
        return

    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            # 적록색약
            if flag:
                if maps[x][y] == maps[nx][ny]:
                    dfs(nx, ny,1)
                elif maps[x][y] == 'R' or maps[x][y] == 'G':
                    if maps[nx][ny] == 'R' or maps[nx][ny] == 'G':
                        dfs(nx, ny, 1)
            # 적록색약 아닌 경우
            else:
                if maps[x][y] == maps[nx][ny]:
                    dfs(nx, ny, 0)


normal = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            normal += 1
            dfs(i,j,0)

visited = [[0] * n for _ in range(n)]

green_equal_red = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            green_equal_red += 1
            dfs(i,j,1)
print(normal, green_equal_red)