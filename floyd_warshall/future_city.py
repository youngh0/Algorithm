# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 4 2
# 1 3
# 2 4
# 3 4

vertexes, edges = map(int, input().split())

graph = [[int(1e9)] * (vertexes+1) for _ in range(vertexes+1)]

for _ in range(edges):
    to, end = map(int, input().split())
    graph[to][end] = 1
    graph[end][to] = 1

for i in range(1,vertexes+1):
    graph[i][i] = 0

x, k = map(int, input().split())

for k in range(1, vertexes+1):
    for a in range(1, vertexes + 1):
        for b in range(1, vertexes + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph[1][k], graph[k][x])