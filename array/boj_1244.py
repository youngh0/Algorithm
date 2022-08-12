# 스위치 켜고 끄기

# 8
# 0 1 0 1 0 0 0 1
# 2
# 1 3
# 2 3

switch_num = int(input())

switches = list(map(int, input().split()))

student_num = int(input())


def turn_on_off(idx):
    if switches[idx] == 0: switches[idx] = 1
    else: switches[idx] = 0


for _ in range(student_num):
    sex, num = map(int, input().split())

    # 남학생
    if sex == 1:
        mul_idx = switch_num // num

        for i in range(mul_idx):
            turn_on_off((num + (i * num))-1)
    # print(switches)
    # 여학생
    elif sex == 2:
        turn_on_off(num-1)
        left = num - 2
        right = num

        while left >= 0 and right < switch_num:
            if switches[left] == switches[right]:
                turn_on_off(left)
                turn_on_off(right)

                left -= 1
                right += 1
            else:
                break

for i in range(len(switches)):
    print(switches[i], end=" ")
    if i % 20 == 19:
        print()


