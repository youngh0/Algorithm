# https://www.acmicpc.net/problem/9375
# 패션왕 신혜빈

from collections import defaultdict

test_num = int(input())

for _ in range(test_num):
    n = int(input())
    answer = 1
    clothes = defaultdict(int)
    for _ in range(n):
        name, category = input().split()
        clothes[category] += 1

    for key, value in clothes.items():
        answer *= clothes[key] + 1


    print(answer-1)