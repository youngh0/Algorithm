# 000110000

arr = input()

count_0 = 0
count_1 = 0

flag = arr[0]

if flag == '0':count_0 += 1
else:count_1 += 1


for i in range(1,len(arr)):
    if arr[i] != flag:
        if flag == '0':
            flag = '1'
            count_1 += 1
        else:
            flag ='0'
            count_0 += 1

print(min(count_0, count_1))