# 공주님의 정원
# https://www.acmicpc.net/problem/2457

import sys
input = sys.stdin.readline
flowers = int(input())

day_info = []

for _ in range(flowers):
    tmp = list(map(int,input().split()))
    day_info.append([tmp[0]*100 + tmp[1], tmp[2]*100+tmp[3]])

day_info.sort()

end_date = -1
idx = -1

# 3월 이전에 펴서 최소 3.1이후에 지는 꽃이 있어야 조건에 맞음.
for i in range(flowers):

    start = day_info[i][0]
    end = day_info[i][1]

    if start <= 301 and end >= 301:
        end_date = max(end_date,end)
        idx = i
    else:
        break

if idx == -1:
    print(0)
    exit()

ans = 1

while end_date < 1201:
    next_flower = -1
    for i in range(idx,flowers):
        start = day_info[i][0]
        end = day_info[i][1]

        if end_date < start:
            break

        if end_date >= start and end > end_date:

            next_flower = max(next_flower, end)
            idx = i
    end_date = next_flower
    ans+=1
    if end_date == -1:
        print(0)
        exit()
print(ans)