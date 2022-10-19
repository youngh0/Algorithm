n,m = map(int, input().split())

balls = list(map(int, input().split()))
weights = [0] * (m+1)

ans = 0

for ball in balls:
    weights[ball] += 1

for i in range(1,m+1):
    n -= weights[i]
    ans +=  weights[i] * n
print(ans)


### 완전탐색
# visited = [[False] * n for _ in range(n)]
# weights = [False] * (m+1)
#
# ans = 0
# tmp = []
#
# def search(start):
#     global ans,n
#     if len(tmp) == 2:
#         print(tmp)
#         print(weights)
#         for a in visited:
#             print(a)
#         print()
#         ans += 1
#         return
#
#     for i in range(start, n):
#         if not visited[start][i] and not weights[balls[i]]:
#             visited[start][i] = True
#             weights[balls[i]] = True
#             tmp.append(balls[i])
#
#             search(i+1)
#
#             visited[start][i] = False
#             weights[balls[i]] = False
#             tmp.pop()
#
# search(0)
# print(ans)