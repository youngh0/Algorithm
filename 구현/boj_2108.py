# 산술평균 : N개의 수들의 합을 N으로 나눈 값 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N(1 ≤ N ≤ 500,000)
# 예외 -> n이 1일 때는 최빈값은 들어온 값 그 자체임

from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())

nums = []

average = 0
medium = 0
max_frequency = 0
num_range = 0

for _ in range(n):
    nums.append(int(input()))

list_sum = sum(nums)
nums.sort()
max_frequency = Counter(nums).most_common()
print(round(list_sum/n))
print(nums[n//2])

if len(max_frequency) > 1:

    if max_frequency[0][1] == max_frequency[1][1]:
        max_frequency = max_frequency[1][0]
    else:
        max_frequency = max_frequency[0][0]

    print(max_frequency)
    print(nums[-1] - nums[0])
else:
    print(max_frequency[0][0])
    print(0)




