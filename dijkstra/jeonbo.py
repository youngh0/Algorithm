# 이취코 실전문제
# 3 2 1
# 1 2 4
# 1 3 2
import heapq

city_num, edge_num, target = map(int, input().split())

distance = [int(1e9)] * (city_num + 1)
graph = [[] for _ in range(city_num + 1)]

for _ in range(edge_num):
    to, end, dist = map(int, input().split())

    graph[to].append((end, dist))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, vertex = heapq.heappop(q)

        if distance[vertex] < dist:
            continue

        for i in graph[vertex]:
            cost = distance[vertex] + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(target)

count = 0
max_dist = 0

for i in range(1,city_num+1):
    if distance[i] < int(1e9) and i != target:
        count += 1
        if max_dist < distance[i]:
            max_dist = distance[i]

print(count, max_dist)