# https://www.acmicpc.net/problem/1655
# 가운데를 말해요

# TODO 풀이 방법
# 정렬을 이용하면 시간초과가 발생하기 때문에 2개의 우선순위 큐를 사용
# left는 maxheap, right는 minheap을 이용
# 2개의 heap크기가 같으면 maxheap(left)에 push
# 다르면 minheap(right)에 push
# 이후 left,right의 루트노드를 비교 후 right가 더 크면 left, right의 루트를 바꿔서 중간값을 유지
# 이렇게 되면 항상 left의 루트가 중간값이 됨

import heapq
import sys

input = sys.stdin.readline

left = []
right = []

n = int(input())

for _ in range(n):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left,-num)
    else:
        heapq.heappush(right,num)

    if right and -left[0] > right[0]:
        left_top = heapq.heappop(left)
        right_top = heapq.heappop(right)

        heapq.heappush(left, -right_top)
        heapq.heappush(right, -left_top)

    print(-left[0])

