#https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, command):
    # prev, next, is_delete
    linked_list = {i: [i - 1, i + 1, 0] for i in range(n)}
    deleted = []

    curr = k

    for cmd in command:
        # print(cmd)
        if cmd[0] == 'U':
            move = int(cmd[2:])
            for i in range(move):
                curr = linked_list[curr][0]
            # print(curr, linked_list[curr][0], linked_list[curr][1])
        elif cmd[0] == 'D':
            move = int(cmd[2:])
            for i in range(move):
                curr = linked_list[curr][1]

        elif cmd[0] == 'C':
            prev, next, is_deleted = linked_list[curr]
            deleted.append([prev, next, curr])
            # 젤 위 요소 삭데
            if prev == -1:
                linked_list[next][0] = prev
                linked_list[curr][2] = 1
                curr = next

            #             # 젤 아래 요소 삭제
            elif next == n:
                linked_list[prev][1] = next
                linked_list[curr][2] = 1
                curr = prev
            # 중간 요소 삭제
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev
                linked_list[curr][2] = 1
                curr = next
            # print(linked_list)
        else:
            prev, next, origin = deleted.pop()
            # print(prev, next, origin)
            # print(linked_list)

            if prev == -1:
                linked_list[next][0] = origin
                linked_list[origin][2] = 0
            elif next == n:
                linked_list[prev][1] = origin
                linked_list[origin][2] = 0
            else:
                linked_list[prev][1] = origin
                linked_list[next][0] = origin
                linked_list[origin][2] = 0

    answer = ''

    for prev, next, is_deleted in linked_list.values():
        if is_deleted:
            answer += 'X'
        else:
            answer += 'O'
    return answer