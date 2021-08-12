import sys

n = sys.stdin.readline
cycle = int(n())

rope_list = []

for i in range(cycle):
    rope = int(n())
    rope_list.append(rope)

rope_list.sort()

for i in range(cycle):
    rope_list[i] = rope_list[i] * (len(rope_list) - i)

print(max(rope_list))