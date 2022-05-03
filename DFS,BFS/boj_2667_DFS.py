#https://www.acmicpc.net/problem/2667

# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

import sys
input = sys.stdin.readline

map_size = int(input())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

town = 0
nums = 1
town_num = []
visited = [[False for _ in range(map_size)] for _ in range(map_size)]

maps = [[0 for _ in range(map_size)] for _ in range(map_size)]

for i in range(map_size):
    one_line = list(map(int, input().rstrip()))
    for j in range(map_size):
        maps[i][j] = one_line[j]


def dfs(x,y, maps,town):
    visited[x][y] = True
    global nums

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= map_size-1 and map_size - 1 >= ny >= 0 and maps[nx][ny] != 0 and visited[nx][ny] == False:
            nums += 1
            dfs(nx,ny,maps,town)


for i in range(map_size):
    for j in range(map_size):
        if maps[i][j] == 1 and visited[i][j] == False:
            town += 1

            dfs(i,j,maps,town)
            town_num.append(nums)
            nums = 1

town_num.sort()

print(town)

for i in range(town):
    print(town_num[i])


