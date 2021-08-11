conference_num = int(input())

start_time = []
end_time = []

count = 1

for i in range(conference_num):
    start, end = map(int,input().split())
    start_time.append(start)
    end_time.append(end)

tmp_list = list(zip(end_time,start_time))
tmp_list.sort()

start_time.clear()
end_time.clear()

for end, start in tmp_list:
    start_time.append(start)
    end_time.append(end)

standard_conference = end_time[0]

for i in range(1,conference_num):

    if standard_conference <= start_time[i]:
        count += 1
        standard_conference = end_time[i]

print(count)
