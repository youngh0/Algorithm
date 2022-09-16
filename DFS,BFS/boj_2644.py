# 촌수계산
# https://www.acmicpc.net/problem/2644

import sys
from collections import deque
input = sys.stdin.readline

people_num = int(input())
start, to = map(int, input().split())

relationships_num = int(input())

relationships = [[]for _ in range(people_num+1)]
visited = [0 for _ in range(people_num+1)]

for _ in range(relationships_num):
    s,t = map(int, input().split())
    relationships[s].append(t)
    relationships[t].append(s)

def bfs(start, to):
    q = deque()
    q.append((start,0))
    answer = -1

    while q:
        x,y = q.popleft()
        if x == to:

            return y

        for i in relationships[x]:
            if visited[i] == 0:
                q.append((i,y+1))
                visited[i] = 1
    return answer

ans = bfs(start,to)
print(ans)