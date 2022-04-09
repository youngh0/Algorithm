import collections
import sys
input = sys.stdin.readline

n, loads_num, k, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(loads_num):
    a, b = map(int, input().split())

    graph[a].append(b)

distance = [-1] * (n+1)

queue = collections.deque()
queue.append(start)
distance[start] = 0

answer = []

while queue:
    v = queue.popleft()

    for node in graph[v]:
        if distance[node] == -1:
            distance[node] = distance[v] +1
            if distance[node] == k:
                answer.append(node)
            queue.append(node)

if answer:
    answer.sort()
    for i in answer:
        print(i, end=' ')
else:
    print(-1)


