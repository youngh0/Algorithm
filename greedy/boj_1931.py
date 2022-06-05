# https://www.acmicpc.net/problem/1931
# 회의실 배정

meeting_nums = int(input())
meetings = []

for _ in range(meeting_nums):
    meetings.append(list(map(int, input().split())))

meetings.sort(key = lambda x : (x[1], x[0]))
standard = meetings[0][1]

answer = 1
for i in range(1, len(meetings)):
    if meetings[i][0] >= standard:
        standard = meetings[i][1]
        answer += 1
print(answer)
