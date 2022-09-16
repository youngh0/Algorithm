# 흙길 보수하기
# https://www.acmicpc.net/problem/1911

# 널빤지가 설치 완료된 끝 지점을 cur변수에 갱신하면서
# 다음 웅덩이 시작 지점이 cur보다 작으면 웅덩이 시작 지점을 cur로 옮겨서
# 설치해야하는 널빤지 개수 계산

import sys

input = sys.stdin.readline
pools, woods = map(int, input().split())

info = [list(map(int,input().split())) for _ in range(pools)]

info.sort()

answer = 0
cur = 0

for start, to in info:
    install_num = 0

    if start < cur:
        start = cur

    install_num += (to - start) // woods

    if (to - start) % woods:
        install_num += 1
    answer += install_num
    cur = start + woods * install_num

print(answer)