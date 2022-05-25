# https://www.acmicpc.net/problem/7576
# 토마토

from collections import deque

def bfs(q,maps):

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    answer = 0
    while q:
        x, y, day = q.popleft()
        answer = day
        if maps[x][y] == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < height and 0 <= ny < width:
                    if maps[nx][ny] == 0:
                        maps[nx][ny] = 1
                        q.append([nx,ny,day+1])

    return answer

width, height = map(int, input().split())

maps = []
tomatos = []

for _ in range(height):
    tmp = list(map(int,input().split()))
    maps.append(tmp)

for i in range(height):
    for j in range(width):
        if maps[i][j] == 1:
            tomatos.append([i,j,0])
q = deque(tomatos)
answer = bfs(q,maps)

is_all = 1

for i in maps:
    if 0 in i:
        is_all = 0
        break
if is_all:
    print(answer)
else: print(-1)



