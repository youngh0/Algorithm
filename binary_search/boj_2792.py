# 백준 보석상자 2792 이분탐색
# https://www.acmicpc.net/problem/2792

# 5 2
# 7
# 4

# print(7//2+1)

import sys
input = sys.stdin.readline

target, jewelry_num = map(int, input().split())

jewelries = []

for _ in range(jewelry_num):
    jewelries.append(int(input()))

start = 1
end = max(jewelries)

while start <= end:
    cnt = 0 # 보석을 나눠가진 사람 수
    mid = (start + end) // 2


    for jewelry in jewelries:
        if jewelry % mid > 0:
            cnt += (jewelry//mid) + 1
        else:
            cnt += jewelry // mid

    # 보석을 나눠가진 사람이 존재하는 사람 보다 적으면 범위를 좁혀서 더 최소화 시키는 범위 탐색
    if cnt <= target:
        end = mid - 1

    # 반대의 경우 나눠가지는 보석의 수를 늘리기
    else:
        start = mid + 1

print(start)