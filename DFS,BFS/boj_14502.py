# 연구소

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

row, col = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
safe_zones = []
virus_zones = []

result = 0

for i in range(row):
    graph.append(list(map(int, input().split())))

# 벽을 3개 세울 때 중복되는 조합 없게 하기 위해 combination 사용
# ex) (1,1) (2,4) (3,5) 세우고 검사한 뒤 나중에 (2,4) (1,1) (3,5)를 방지하기 위해
for i in range(row):
    for j in range(col):
        if graph[i][j] == 0:
            safe_zones.append([i, j])
        if graph[i][j] == 2:
            virus_zones.append([i,j])

def bfs(tmp_graph):
    q = deque()
    for virus_location in virus_zones:
        q.append((virus_location[0], virus_location[1]))
    # for i in range(row):
    #     for j in range(col):
    #         if tmp_graph[i][j] == 2:
    #             q.append((i,j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    q.append((nx,ny))

    global result

    count = 0

    for i in range(row):
        for j in range(col):
            if tmp_graph[i][j] == 0:
                count += 1

    result = max(result, count)

def wall():
    safe_zones_combi = combinations(safe_zones, 3)

    for walls in safe_zones_combi:
        a, b, c = walls[0], walls[1], walls[2]

        graph[a[0]][a[1]] = 1
        graph[b[0]][b[1]] = 1
        graph[c[0]][c[1]] = 1

        tmp_graph = [item[:] for item in graph]

        bfs(tmp_graph)

        graph[a[0]][a[1]] = 0
        graph[b[0]][b[1]] = 0
        graph[c[0]][c[1]] = 0

wall()

print(result)

