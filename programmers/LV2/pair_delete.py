# 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = 0

    array = []
    array.append(s[0])

    for i in range(1, len(s)):

        letter = s[i]

        # 제거하다 보면 stack에 아무것도 없는 상태에서 array[-1]하면 index에러 발생하기 때문에
        # 이를 방지
        if not array:
            array.append(letter)
            continue
        if letter == array[-1]:
            array.pop()
        else:
            array.append(letter)

    if not array:
        answer = 1

    return answer