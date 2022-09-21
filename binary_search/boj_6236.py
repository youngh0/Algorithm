# 용돈관리
# https://www.acmicpc.net/problem/6236

# start = min(지출예정)
# end = sum(지출예정)

pay_num, withdraw_num = map(int, input().split())

pay_info = []




for _ in range(pay_num):
    pay = int(input())
    pay_info.append(pay)
    # right += pay

left = min(pay_info)
right = sum(pay_info)
max_day = max(pay_info)
mid = 0

while left <= right:

    count = 1
    mid = (left + right) // 2
    cur_money = mid

    for money in pay_info:
        if money > cur_money:
            count += 1
            cur_money = mid

        cur_money -= money
    # print(left, right,count)
    # if count <= withdraw_num:
    #     right = mid - 1
    if count > withdraw_num or mid < max_day:
        left = mid + 1
    else:
        right = mid - 1

print(left)

