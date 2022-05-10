# https://programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    zeros = lottos.count(0)

    # 내가 고른 번호를 전부 모르는 경우
    if zeros == 6:
        return [1, 6]

    # 내가 고른 번호를 전부 알 경우
    if zeros == 0:
        lottos.sort()
        win_nums.sort()
        count = 0
        for i in range(6):
            if lottos[i] == win_nums[i]:
                count += 1
        return [rank[count], rank[count]]

    # 위 두 가지 경우를 제외한 경우
    lottos.sort(reverse=True)

    count = 0

    for i in range(6 - zeros):
        if lottos[i] in win_nums:
            count += 1
    best = 6 if count + zeros > 6 else count + zeros
    answer = [rank[best], rank[count]]
    return answer