import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
target_num = int(input())
arr.sort()

answer = 0
left = 0
right = n-1

while left < right:
    tmp = arr[left] + arr[right]
    if tmp == target_num:
        answer += 1
    if tmp < target_num:
        left += 1
    else:
        right -= 1


print(answer)