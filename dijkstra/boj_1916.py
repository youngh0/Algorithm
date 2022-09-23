# 최소비용 구하기
# https://www.acmicpc.net/problem/1916

import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

distance = [int(1e9)] * (n+1)
graph = [[] for _ in range(n+1)]

# 버스 정보
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

start, end = map(int, input().split())


q = []
heapq.heappush(q,(0,start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = i[1] + distance[now]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

print(distance[end])