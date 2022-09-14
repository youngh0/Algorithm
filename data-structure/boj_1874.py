# 스택 수열
# https://www.acmicpc.net/problem/1874
import sys
input = sys.stdin.readline

stack = []
ans = []

n = int(input())

num = 1
flag = True

for _ in range(n):
    target = int(input())

    while num <= target:
        stack.append(num)
        num += 1
        ans.append("+")
    # print(stack)
    if stack[-1] == target:
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        flag = False
        break

if flag:
    for a in ans:
        print(a)