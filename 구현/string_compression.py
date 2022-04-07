def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        standard = s[:step]
        # print(standard)
        count = 1

        result = ""

        for i in range(step, len(s), step):
            # print(i)
            # print(standard," ",s[i:i+step], " ", result )
            if standard == s[i:i + step]:
                count += 1
            else:
                if count >= 2:
                    result += str(count) + standard
                else:
                    result += standard
                count = 1
                standard = s[i:i + step]
            # print(standard, )
        if count >= 2:
            result += str(count) + standard
        else:
            result += standard
        # print(len(result), result)
        answer = min(answer, len(result))
    return answer