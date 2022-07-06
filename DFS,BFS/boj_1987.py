# 알파벳
# https://www.acmicpc.net/problem/1987

# 한 위치에서 4방향 모두 탐색 끝나면 이전 알파벳으로 돌아가기 때문에
# 현재 위치 알파벳 방문처리 취소하고, 지금까지 탐색한 거리가 최대 인지 max()로 비교

row, col = map(int, input().split())

maps = [list(input()) for _ in range(row)]
visited = [0] * 26

first_idx = ord(maps[0][0]) - 65
visited[first_idx] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y, tmp_answer):
    global answer
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < row and 0 <= ny < col:
            alpha_idx = ord(maps[nx][ny]) - 65
            if visited[alpha_idx] == 0:
                # print(x,y,tmp_answer, visited[alpha_idx], maps[x][y],maps[nx][ny])
                visited[alpha_idx] = 1
                dfs(nx,ny, tmp_answer+1)

    ori_alpha_idx = ord(maps[x][y]) - 65
    visited[ori_alpha_idx] = 0
    answer = max(answer, tmp_answer)
    return



answer = 1
dfs(0,0,1)

print(answer)