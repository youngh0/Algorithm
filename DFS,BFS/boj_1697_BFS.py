# 숨바꼭질
# https://www.acmicpc.net/problem/1697
from collections import deque


def bfs():
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        if x == end:
            print(maps[x])
            break

        for nx in (x + 1, x - 1, x * 2):
            if 0 <= nx < 100001 and maps[nx] == 0:
                maps[nx] = maps[x] + 1
                q.append(nx)


start, end = map(int, input().split())
maps = [0] * 100001
bfs()
