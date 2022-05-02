#https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    bucket = []

    for move in moves:
        for i in range(len(board)):
            pick = board[i][move - 1]
            if pick == 0:
                pass
            else:
                bucket.append(pick)
                board[i][move - 1] = 0
                break

        if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
            bucket.pop()
            bucket.pop()
            answer += 2

    return answer