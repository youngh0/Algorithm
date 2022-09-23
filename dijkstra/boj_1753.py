# 최단경로
# https://www.acmicpc.net/problem/1753

import sys
import heapq

input = sys.stdin.readline

v,e = map(int,input().split())

start = int(input())

distance = [int(1e9)] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

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

for i in range(1,v+1):
    if distance[i] >= int(1e9):
        print("INF")
    else:
        print(distance[i])