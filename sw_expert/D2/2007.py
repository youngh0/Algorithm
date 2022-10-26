# 패턴 마디의 길이

n = int(input())

for t in range(1,n+1):
    input_string = input()
    flag = False
    for i in range(1,30):
        if flag:
            break
        if input_string[0:i] == input_string[i:i+i]:
            print(f"#{t} {i}")
            flag = True
