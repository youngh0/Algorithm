import sys

input = sys.stdin.readline

problem_num = int(input())

for problem_num in range(problem_num):

    recruit_num = int(input())

    result = []
    for i in range(recruit_num):

        recruit_result = input().split()
        result.append(tuple(map(int, recruit_result)))
    result = sorted(result, key=lambda x:x[0])
    pass_count = 1
    interview_rank = result[0][1]

    for document, interview in result[1:]:
        if interview_rank > interview:
            pass_count += 1
            interview_rank = interview

    print(pass_count)
