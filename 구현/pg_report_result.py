#https://programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    reports = set(report)

    reporting = defaultdict(set)
    reported = defaultdict(set)
    for report_info in reports:
        to, end = report_info.split()
        reporting[to].add(end)
        reported[end].add(to)

    for idx, id in enumerate(id_list):
        for reporting_id in reporting[id]:
            if len(reported[reporting_id]) >= k:
                answer[idx] += 1

    return answer