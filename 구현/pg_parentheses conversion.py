# https://programmers.co.kr/learn/courses/30/lessons/60058

def divide(p):
    left = right = 0

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            return (p[:i + 1], p[i + 1:])


def check_string(u):
    stack = []
    for i in range(len(u)):
        if u[i] == '(':
            stack.append(u[i])
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    answer = ''

    if not p:
        return answer
    u, v = divide(p)
    if check_string(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        u = u[1:-1]

        for i in u:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer