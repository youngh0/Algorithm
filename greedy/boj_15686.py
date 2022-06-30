# https://www.acmicpc.net/problem/15686
# 치킨 배달
from collections import deque
from itertools import combinations

n, m = map(int, input().split())

maps = [list(map(int,input().split())) for _ in range(n)]

houses = []
chicken = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            houses.append((i,j))
        elif maps[i][j] == 2:
            chicken.append((i,j))


answer = 1e9
for combi in combinations(chicken,m):
    tmp = 0
    for house in houses:
        min_dis = 1e9
        for i in range(m):
            min_dis = min(min_dis, abs(house[0] - combi[i][0]) + abs(house[1] - combi[i][1]))
        tmp += min_dis
    answer = min(answer, tmp)

print(answer)