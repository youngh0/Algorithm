import sys
input = sys.stdin.readline

from collections import deque

tc = int(input())

for _ in range(tc):
    commands = list(input())
    n = int(input())
    arr = input().rstrip()
    arr = deque(arr[1:-1].split(","))
    if n == 0:
        arr = deque()
    flag = True
    cnt = 0
    for command in commands:
        if command == 'R':
            cnt += 1
        elif command == 'D':
            if not arr:
                print('error')
                flag = False
                break
            else:
                if cnt % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
    if flag:
        if cnt % 2 == 1:
            arr.reverse()
        print("["+",".join(arr)+"]")

