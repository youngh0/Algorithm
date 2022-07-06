# https://www.acmicpc.net/problem/1744
# 수 묶기

import heapq

positive_num = []
negative_num = []
zeros = 0

n = int(input())

answer = 0

for _ in range(n):
    num = int(input())
    if num > 1: heapq.heappush(positive_num, -num)
    elif num == 0: zeros += 1
    elif num == 1: answer += 1
    elif num < 0: heapq.heappush(negative_num, num)

# print("pos",positive_num)
# print("neg",negative_num)
# print("zeros: ", zeros)
# print(answer)

while len(positive_num) > 1:
    a = -heapq.heappop(positive_num)
    b = -heapq.heappop(positive_num)

    answer += (a * b)

while len(negative_num) > 1:
    a = heapq.heappop(negative_num)
    b = heapq.heappop(negative_num)

    answer += (a * b)

if negative_num:
    if zeros == 0:
        answer += heapq.heappop(negative_num)

if positive_num:
    answer += -heapq.heappop(positive_num)

print(answer)