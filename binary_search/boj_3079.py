#2 6
#7
#10

import sys
input = sys.stdin.readline

n, people = map(int,input().split())

gateway = []

for _ in range(n):
    gateway.append(int(input()))

left = 0
right = max(gateway) * people

while left <= right:
    mid = (left + right) // 2

    tmp = 0
    for gate in gateway:
        tmp += mid // gate

    if tmp >= people:
        right = mid - 1
    else:
        left = mid + 1
print(left)
