# 나이트의 이동
# https://www.acmicpc.net/problem/7562

from collections import deque

test_case = int(input())

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]


for _ in range(test_case):
    n = int(input())

    source = list(map(int, input().split()))
    dest = list(map(int, input().split()))

    visited = [[0] * n for _ in range(n)]
    visited[source[0]][source[1]] = 1

    q = deque()
    q.append((source[0],source[1],0))

    answer = 0

    while q:
        x,y,move = q.popleft()

        if x == dest[0] and y == dest[1]:
            answer = move
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny,move+1))
    print(answer)