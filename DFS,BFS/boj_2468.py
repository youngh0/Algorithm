import sys
from collections import deque
input = sys.stdin.readline

num = int(input())

max_rain = 0

array = [list(map(int, input().split())) for _ in range(num)]


answer = 1

for a in array:
    t_rain = max(a)
    if t_rain > max_rain:
        max_rain = t_rain


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j,visited, region_graph):

    q = deque()
    q.append((i,j))
    visited[i][j] = 1

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < num and 0 <= ny < num:
                if visited[nx][ny] == 0 and region_graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))


for rain_amount in range(max_rain):
    visited = [[0] * num for _ in range(num)]
    tmp_ans = 0
    # 잠긴 지역 = 0, 아니면 1
    tmp = [[1] * num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            if array[i][j] <= rain_amount:
                tmp[i][j] = 0

    for i in range(num):
        for j in range(num):
            if visited[i][j] == 0 and tmp[i][j]:
                bfs(i,j,visited,tmp)
                tmp_ans += 1
    # print(rain_amount, tmp_ans)
    answer = max(answer, tmp_ans)

print(answer)

