# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(start_node):
    if visited[start_node] != 0:
        # print(start_node)
        return

    visited[start_node] = 1
    for i in edges[start_node]:
        if visited[i] == 0:
            dfs(i)


node, edge = map(int,input().split())

edges = [[] for _ in range(node+1)]
visited = [0 for _ in range(node+1)]

for _ in range(edge):
    start, end = map(int,input().split())
    edges[start].append(end)
    edges[end].append(start)

answer = 0

for i in range(1,node+1):
    if visited[i] == 0:
        if edges[i]: # 연결된 node가 있는 경우 dfs호출
            dfs(i)
            answer+=1
        else: # 연결된 node가 없는 경우 연결요소 +1
            answer += 1
            visited[i] = 1

print(answer)

