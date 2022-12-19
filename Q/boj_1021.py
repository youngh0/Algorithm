from collections import deque
n,m = map(int,input().split())

q = deque([i for i in range(1,n+1)])

targets = deque(list(map(int, input().split())))
answer = 0

for i in range(len(targets)):
    target = targets[i]
    target_idx = q.index(target)
    print(target_idx)