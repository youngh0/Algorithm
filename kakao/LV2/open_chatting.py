#https://programmers.co.kr/learn/courses/30/lessons/42888 2019 KAKAO BLIND RECRUITMENT

def solution(record):
    uid_name = {}
    answer = []

    # 최종 변경된 유저의 이름이 uid:name형태로 저장
    for i in record:
        if i[:5] != 'Leave':
            behave, uid, name = i.split(" ")
            uid_name[uid] = name

    for i in record:
        if i[:5] == 'Enter':
            behave, uid, name = i.split(" ")
            answer.append(uid_name[uid] + "님이 들어왔습니다.")
        elif i[:5] == 'Leave':
            behave, uid = i.split(" ")
            answer.append(uid_name[uid] + "님이 나갔습니다.")

    return answer