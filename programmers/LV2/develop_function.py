# 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3

# 첫 번째에 있는 작업이 배포 완료까지 걸리는 시점 계산
# 남아 있는 작업에도 남은 일수 만큼 진도를 나가도록 progresses더해줌.
# 이후, 배포 가능한 작업 개수 카운트
# 위 작업을 q가 없을때 까지 반복

from collections import deque


def solution(progresses, speeds):
    answer = []

    q = deque()

    for i in range(len(progresses)):
        q.append([progresses[i], speeds[i]])

    while q:
        first_job = q[0][0]
        first_speed = q[0][1]

        fin_job_cnt = 0

        # 첫 번째 작업이 100이 아닌 경우
        if first_job < 100:

            # 배포 완료까지 걸리는 날짜 계산
            tmp = (100 - first_job) % first_speed
            need_day = 0

            if tmp:
                need_day += (100 - first_job) // first_speed + 1
            else:
                need_day += (100 - first_job) // first_speed

            # 첫 번째 작업 배포까지 필요한 일수 만큼 나머지 일들도 progress늘려주기
            for i in range(len(q)):
                q[i][0] += need_day * q[i][1]

            # progresses 100이상인 작업 q에서 제거
            for i in range(len(q)):
                if q[i][0] >= 100:
                    fin_job_cnt += 1
                else:
                    break

            for _ in range(fin_job_cnt):
                q.popleft()

        answer.append(fin_job_cnt)

    return answer