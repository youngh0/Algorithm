# 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter


# course별로 order들의 조합을 구함.
# counter를 이용해 조합별 주문 빈도수를 구함.
# 가장 많이 나온 빈도수가 1초과라면 이후 해당 빈도수와 같은 조합은 answer에 추가

def solution(orders, courses):
    answer = []

    for course in courses:

        order_array = []
        for order in orders:
            combi = combinations(order, course)
            for i in combi:

                # ["XYZ", "XWY", "WXA"]
                # XY = 2번, WX = 2번
                # 만약 정렬을 안하면 XW, WX를 다른 조합으로 보게됨
                res = "".join(sorted(i))
                order_array.append(res)
        max_order = Counter(order_array).most_common()
        for menu_course, cnt in max_order:
            if cnt > 1 and cnt == max_order[0][1]:
                answer.append(menu_course)
    answer.sort()
    print(answer)
    return answer