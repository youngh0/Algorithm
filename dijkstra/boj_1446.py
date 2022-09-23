# 5 150
# 0 50 10
# 0 50 20
# 50 100 10
# 100 151 10
# 110 140 90

import sys
input = sys.stdin.readline

import heapq

n, d = map(int, input().split())

distance = [int(1e9)] * (d+1)
graph = [[(i+1,1)] for i in range(d+1)]
graph[d] = []
for _ in range(n):
    x,y,z = map(int, input().split())
    if y > d:
        # print(x,y,z)
        continue
    graph[x].append((y,z))
# print(graph)
q = []
heapq.heappush(q,(0,0))
distance[0] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = i[1] + distance[now]
        # print(i)
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost, i[0]))

print(distance[d])

