# DFS와 BFS

import sys
from collections import deque

input = sys.stdin.readline
# 노드의 개수, 간선의 개수, 시작 노드 번호
n, m, v = map(int,input().split())

graph = [[] for _ in range(n+1)]
dfs_visited = [0 for _ in range(n+1)]
bfs_visited = [0 for _ in range(n+1)]

for i in range(m):
    start, end = map(int,input().split())
    # 양방향
    graph[start].append(end)
    graph[end].append(start)
for i in range(1,n+1):
    graph[i].sort()

def dfs(start):
    dfs_visited[start] = 1
    print(start, end=" ")
    for node in graph[start]:
        if not dfs_visited[node]:
            dfs(node)

def bfs(start):
    q = deque()
    q.append(start)
    bfs_visited[start] = 1

    while q:
        v = q.popleft()
        print(v, end=" ")

        for node in graph[v]:
            if not bfs_visited[node]:
                q.append(node)
                bfs_visited[node] = 1

dfs(v)
print()
bfs(v)