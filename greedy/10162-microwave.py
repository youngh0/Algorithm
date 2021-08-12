total_time = int(input())

btn_time = [300,60,10]

if total_time % 10 != 0 : print(-1)
else :
    for i in range(3):
        print(total_time // btn_time[i], end=' ')
        total_time %= btn_time[i]