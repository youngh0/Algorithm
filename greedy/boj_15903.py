# 카드 합체 놀이
# https://www.acmicpc.net/problem/15903

import heapq

cards_num, m = map(int,input().split())

cards = list(map(int,input().split()))
heapq.heapify(cards)

for _ in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    sum_card = card1 + card2

    heapq.heappush(cards, sum_card)
    heapq.heappush(cards, sum_card)

print(sum(cards))