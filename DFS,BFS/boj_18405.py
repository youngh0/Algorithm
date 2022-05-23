# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int,input().split())

graph = []
virus_info = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus_info.append((graph[i][j], 0, i, j))

s, end_x, end_y = map(int,input().split())

virus_info.sort()

q = deque(virus_info)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    virus_num, time, x, y = q.popleft()
    if time == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and ny >= 0 and ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = virus_num
            q.append((virus_num, time + 1, nx, ny))

print(graph[end_x-1][end_y-1])


