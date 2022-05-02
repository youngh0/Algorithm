# https://programmers.co.kr/learn/courses/30/lessons/67256

# for i in numbers
#
# 1,4,7,*은 무조건 L
#   -> 왼손 위치 변경
# 3,6,9,# 은 무조건 R
#   -> 오른손 위치 변경
# 2,5,8,0은 상하좌우 탐색
#   -> 주변에 오른손, 왼손 있는지 탐색
#   -> 오른손, 왼속 둘 다 있으면 answer += hand
#   -> 오른손만 있으면 R, 왼손은 L추가

def solution(numbers, hand):
    answer = ''
    key_position = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }
    cur_left = key_position['*']
    cur_right = key_position['#']

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in numbers:
        now = key_position[i]

        if i == 1 or i == 4 or i == 7 or i == '*':
            answer += 'L'
            cur_left = now
        elif i == 3 or i == 6 or i == 9 or i == '#':
            answer += 'R'
            cur_right = now
        else:
            left_dis = abs(cur_left[0] - now[0]) + abs(cur_left[1] - now[1])

            right_dis = abs(cur_right[0] - now[0]) + abs(cur_right[1] - now[1])

            if left_dis == right_dis:
                answer += hand[0].upper()
                if hand == 'right':
                    cur_right = now
                else:
                    cur_left = now
            elif left_dis < right_dis:
                answer += 'L'
                cur_left = now
            else:
                answer += 'R'
                cur_right = now

    return answer