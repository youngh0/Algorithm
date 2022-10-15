from collections import deque
import sys

input = sys.stdin.readline

maps = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0

visited = [[False] * 6 for _ in range(12)]

for _ in range(12):
    maps.append(list(input().rstrip()))

def bfs(cx,cy):
    is_bomb = False

    tmp = []
    collect_y = set()
    q = deque()

    q.append((cx,cy))
    tmp.append((cx,cy))
    visited[cx][cy] = True
    collect_y.add(cy)

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and maps[nx][ny] == maps[cx][cy]:
                    tmp.append((nx,ny))
                    q.append((nx,ny))
                    collect_y.add(ny)
                    visited[nx][ny] = True

    if len(tmp) >= 4:
        is_bomb = True
        for tx,ty in tmp:
            maps[tx][ty] = '.'

    return is_bomb, collect_y

def down_block(x,y):
    if x == 11 or maps[x+1][y] != '.':
        return

    maps[x][y], maps[x+1][y] = maps[x+1][y], maps[x][y]
    down_block(x+1,y)


while True:
    # print('---------------------')
    flag = False

    for i in range(11, -1, -1):
        for j in range(6):
            if maps[i][j] != '.':
                visited = [[False] * 6 for _ in range(12)]
                result, y_collect = bfs(i, j)
                if result:
                    flag = True

    if flag:
        ans += 1
        for i in range(11, 0, -1):
            for j in range(6):
                if maps[i][j] == '.' and maps[i - 1][j] != '.':
                    # for a in maps:
                    #     print(a)
                    down_block(i - 1, j)
                    # print(i,j)

                    # print()
                    continue

    else:
        break
    # for a in maps:
    #     print(a)

print(ans)