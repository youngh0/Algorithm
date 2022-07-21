# 아기상어
# https://www.acmicpc.net/problem/16236

# 1. bfs로 지나갈 수 있는 곳 탐색
#   1.1 탐색 중 현재 size보다 작아서 먹을 수 있는 물고기 위치 탐색
#       먹을 수 있는 위치 중 가장 가까운 곳으로 먹으러 가기
#       1.1.1 먹으면서 상어 위치 조절, 거리 측정, 먹은 개수 count해서 상어 크기 조절

from collections import deque

n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

shark_size = 2
shark_loc = [0,0]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            shark_loc[0] = i
            shark_loc[1] = j
            maps[i][j] = 0

def bfs(shark_x,shark_y,shark_size):
    q = deque()
    q.append((shark_x,shark_y,0))
    visited = [[0] * n for _ in range(n)]
    eats = []
    while q:
        x, y, dist = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 상어크기 보다 작은 공간은 지나갈 수 있다.
                if maps[nx][ny] <= shark_size:
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = 1
                    # 0이 아니고 상어크기 보다 작으면 먹을 수 있다.
                    if 0 < maps[nx][ny] < shark_size:
                        # print(nx, ny, maps[nx][ny])
                        eats.append((nx, ny, dist+1))
    return eats

answer = 0
eat_count = 0

while 1:
    is_eat = bfs(shark_loc[0], shark_loc[1],shark_size)

    # 먹을 수 있는 물고기가 없는 경우
    if not is_eat:
        break

    eat_count += 1
    if eat_count == shark_size:

        shark_size += 1
        eat_count = 0

    # deque가 아니기 때문에 pop을 위해 내림차순 정렬
    # 거리, y, x순으로 키를 설정해 정렬
    is_eat.sort(key= lambda x : (-x[2], -x[0], -x[1]))
    nx, ny, eat_dist = is_eat.pop()

    # 해당 구역의 물고기를 먹고 해당 위치 0으로 설정
    maps[nx][ny] = 0
    # 상어의 위치 변경
    shark_loc[0] = nx
    shark_loc[1] = ny
    answer += eat_dist

print(answer)
