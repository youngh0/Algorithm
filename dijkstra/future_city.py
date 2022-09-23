# 이코테 최단경로 연습문제 1

import heapq

vertexes, edges = map(int, input().split())

distance = [int(1e9)] * (vertexes+1)

graph = [[]  for _ in range(vertexes+1)]

for _ in range(edges):
    to, end = map(int, input().split())
    graph[to].append((end,1))
    graph[end].append((to,1))

x,k = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
answer = 0
# print(distance)
dijkstra(1)
answer += distance[k]
distance = [int(1e9)] * (vertexes+1)

dijkstra(k)
answer += distance[x]
print(answer)