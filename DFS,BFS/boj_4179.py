# 불!
# https://www.acmicpc.net/problem/4179

# 4 4
# ####
# #JF#
# #..#
# #..#

# 5 4
# ####
# #...
# #.##
# #.J#
# ####

import sys
from collections import deque
input = sys.stdin.readline

def fire_bfs():
    q = deque()
    for fire in fires:

        q.append((fire[0], fire[1], 0))
        fire_visited[fire[0]][fire[1]] = 0

    while q:
        x,y,num = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:

                if fire_visited[nx][ny] == -1 and graph[nx][ny] != '#':
                    fire_visited[nx][ny] = fire_visited[x][y] + 1

                    q.append((nx,ny,num+1))

def jihoon_bfs():
    q = deque()
    q.append((jihoon))
    jihoon_visited[jihoon[0]][jihoon[1]] = 1

    while q:
        x,y,n = q.popleft()
        if x == 0 or x == r - 1 or y == 0 or y == c - 1:
            return n+1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if jihoon_visited[nx][ny] == 0 and (fire_visited[nx][ny] > n+1 or fire_visited[nx][ny] == -1) and graph[nx][ny] == ".":

                    q.append((nx,ny,n+1))
                    jihoon_visited[nx][ny] = 1

    return -1

r, c = map(int, input().split())
jihoon_visited = [[0] * c for _ in range(r)]
fire_visited = [[-1] * c for _ in range(r)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

fires = []
jihoon = None

graph = []
# fires_graph = [[0] * c for _ in range(r)]

for _ in range(r):
    graph.append(list(input().strip()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            fires.append((i,j))
        elif graph[i][j] == 'J':
            jihoon = (i,j,0)

fire_bfs()
# print(fire_visited)
ans = jihoon_bfs()

if ans == -1:
    print("IMPOSSIBLE")
else:
    print(ans)
# print(fires_graph)
