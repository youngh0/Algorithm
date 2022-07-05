# https://www.acmicpc.net/problem/16234
# 백준 인구이동

from collections import deque
import math

n, l, r = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(ox, oy):
    q = deque()
    q.append((ox, oy))
    visited[ox][oy] = 1
    team_sum = maps[ox][oy]
    team_loc = [(ox,oy)]

    while q:
        x, y = q.popleft()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                diff = abs(maps[x][y] - maps[nx][ny])
                if visited[nx][ny] == 0 and l <= diff <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    team_sum += maps[nx][ny]
                    team_loc.append((nx, ny))
    for cx, cy in team_loc:
        maps[cx][cy] = math.floor(team_sum / len(team_loc))

    if len(team_loc) > 1:
        return True
    else:
        return False

answer = 0

while True:
    visited = [[0] * n for _ in range(n)]
    is_continue = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                is_team = bfs(i, j)
                # print(i,j,is_team)
                if is_team:
                    is_continue = True

    if not is_continue:
        break
    else:
        answer += 1
    # print(maps)
    # print("----------")

        # print(visited)

print(answer)