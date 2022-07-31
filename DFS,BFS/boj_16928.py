from collections import deque

ladder, snake = map(int, input().split())

ladder_or_snake = [ 0 for _ in range(101)]

for _ in range(ladder + snake):
    src, dest = map(int, input().split())
    ladder_or_snake[src] = dest

# print(ladder_or_snake)

def bfs():
    q = deque()
    q.append(1)

    while q:
        cur = q.popleft()

        if cur == 100:
            # print(answer)
            print(answer[cur])
            return

        for i in range(1,7):
            dest = cur + i

            if dest <= 100 and visited[dest] == 0:

                if ladder_or_snake[dest] != 0:
                    dest = ladder_or_snake[dest]

                if visited[dest] == 0:
                    visited[dest] = 1
                    q.append(dest)
                    answer[dest] = answer[cur] + 1

visited = [0 for _ in range(101)]
visited[1] = 1

answer = [0 for _ in range(101)]
bfs()
# print(answer)
# print(answer[100]-1)