# 카드2
# https://www.acmicpc.net/problem/2164

# 1. 제일 위에 있는 카드는 버린다.
# 1.1 그 다음 카드는 젤 뒤로 보낸다.
# 카드가 1장 남을 때 까지 반복한다.
# 카드의 번호는 1부터 N까지

from collections import deque

n = int(input())

cards = deque([i for i in range(1,n+1)])


while len(cards) > 1:
    # 카드 버리기
    cards.popleft()

    # 젤 위 카드 뒤로 보내기
    top_card = cards.popleft()
    cards.append(top_card)

print(cards[0])
