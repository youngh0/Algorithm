n = int(input())
towers = list(map(int, input().split()))
stack = []
answer = [0 for _ in range(n)]

for i in range(n):
    source_tower = towers[i]
    while stack:
        last_height = stack[-1][1]
        last_index = stack[-1][0]
        if last_height > source_tower:
            answer[i] = last_index + 1
            break
        else:
            stack.pop()
    stack.append([i,source_tower])

print(" ".join(map(str,answer)))