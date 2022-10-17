def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        result = compress(i,s)
        answer = min(answer, result)


    return answer

def compress(cut_num,s):
    tmp = 1
    flag = s[:cut_num]
    res = 0

    for i in range(cut_num, len(s), cut_num):

        if flag == s[i:i+cut_num]:
            tmp += 1

        else:
            if tmp == 1:
                res += cut_num

            else:
                res += len(str(tmp)) + cut_num

            tmp = 1
            flag = s[i:i+cut_num]

    if tmp > 1:
        res += len(str(tmp)) + cut_num
    else:
        res += len(flag)
    return res

solution("abcabcdeded")