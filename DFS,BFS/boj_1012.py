# https://www.acmicpc.net/problem/1012

# 밭의 최대 넓이는 50x50
# 밭의 모든 위치 탐색 말고 입력받은 배추 위치 저장하고 해당 위치만 탐색

import sys
from collections import deque
sys.setrecursionlimit(10000)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

# def dfs(x,y,maps):
#     global width, height
#
#     maps[x][y] = 0
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
        # if 0 <= nx < width and 0 <= ny < height:
        #     if maps[nx][ny] == 1:
        #         dfs(nx,ny,maps)
#

def bfs(x,y,maps):
    q = deque()
    q.append([x,y])

    while q:
        bi, bj = q.popleft()
        maps[bi][bj] = 0

        for i in range(4):
            nx = bi + dx[i]
            ny = bj + dy[i]
            if 0 <= nx < width and 0 <= ny < height:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    q.append([nx,ny])

testcase = int(input())
for _ in range(testcase):
    answer = 0
    width, height, baechu = map(int, input().split())
    maps = [[0 for _ in range(height)] for _ in range(width)]
    visited = [[0 for _ in range(height)] for _ in range(width)]
    baechu_location = []

    for _ in range(baechu):
        x, y = map(int, input().split())
        baechu_location.append([x,y])
        maps[x][y] = 1

    # for x,y in baechu_location:
    #     if maps[x][y] == 1:
    #         answer += 1
    #         dfs(x,y,maps)
    for x,y in baechu_location:
        if maps[x][y] == 1:
            bfs(x,y,maps)
            answer += 1



    print(answer)



