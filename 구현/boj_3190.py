from collections import deque

n = int(input())

maps = [[0] * n for _ in range(n)]
maps[0][0] = 2
directions = deque()
snakes = deque()
snakes.append((0, 0))

# 방향정보
cur_direction = 0
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0

apple_num = int(input())

for _ in range(apple_num):
    x, y = map(int, input().split())
    maps[x - 1][y - 1] = 1

directions_num = int(input())

for _ in range(directions_num):
    change_time, direction = input().split()
    directions.append((int(change_time), direction))


def change_direction(direction, cur_direction):
    if direction == "L":
        return (cur_direction - 1) % 4
    else:
        return (cur_direction + 1) % 4


while True:
    last_x, last_y = snakes[-1]
    time += 1

    cur_x = last_x + dx[cur_direction]
    cur_y = last_y + dy[cur_direction]
    snakes.append((cur_x, cur_y))

    if cur_x >= n or cur_x < 0 or cur_y >=n or cur_y < 0 or maps[cur_x][cur_y] == 2:
        break

    if maps[cur_x][cur_y] == 0:
        # print(cur_x,cur_y)
        tail_x, tail_y = snakes[0]
        maps[tail_x][tail_y] = 0
        snakes.popleft()
        maps[cur_x][cur_y] = 2
    elif maps[cur_x][cur_y] == 1:
        maps[cur_x][cur_y] = 2
    # print(time, directions)
    if directions and time == directions[0][0]:
        cur_direction = change_direction(directions[0][1], cur_direction)
        directions.popleft()

print(time)
