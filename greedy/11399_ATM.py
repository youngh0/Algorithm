people = int(input())

time = list(map(int, input().split(' ')))
time.sort()

tmp = 0
sum = 0

for i in time:
    sum += tmp + i
    tmp += i

print(sum)