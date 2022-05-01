#https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq


def solution(food_times, k):
    # 음식을 다 못먹으면 -1 리턴해주기 위해 처음부터 -1로 할당
    answer = -1
    h = []

    for idx, value in enumerate(food_times):
        heapq.heappush(h, (value, idx + 1))

    pre_food = 0

    while h:
        current_food_val = h[0][0] - pre_food
        cycle_eat = current_food_val * len(h)

        if cycle_eat <= k:
            k -= cycle_eat
            pre_food = heapq.heappop(h)[0]
        else:
            h.sort(key=lambda x: x[1])
            idx = k % len(h)
            answer = h[idx][1]
            break

    return answer