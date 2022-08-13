# 그림
# https://www.acmicpc.net/problem/1926

from collections import deque

def bfs(i,j):
    total = 1

    q = deque()
    q.append((i,j))
    visited[i][j] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:

                if visited[nx][ny] == 0 and array[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    total += 1

    return total


dx = [0,0,1,-1]
dy = [1,-1,0,0]

row, col = map(int,input().split())

array = []
visited = [[0] * col for _ in range(row)]

for _ in range(row):
    array.append(list(map(int,input().split())))


picture_cnt = 0
picture_size = 0
for i in range(row):
    for j in range(col):

        if visited[i][j] == 0 and array[i][j] == 1:
            size = bfs(i,j)

            picture_cnt += 1
            if size > picture_size:
                picture_size = size

print(picture_cnt)
print(picture_size)


