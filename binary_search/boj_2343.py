# 백준 기타레슨 (이분탐색)
# https://www.acmicpc.net/problem/2343

n, target = map(int, input().split())

array = list(map(int, input().split()))

total = sum(array)

start = max(array)
end = total

result = 0

while start <= end:
    cnt = 0
    blueray = 0

    # 기준이 되는 블루레이 크기
    mid = (start + end) // 2

    for lesson in array:
        if blueray + lesson > mid:
            cnt += 1
            blueray = 0

        blueray += lesson

    if blueray:
        cnt += 1

    # 블루레이가 target보다 작거나 같으면 보다 작은 블루레이 크기 찾기 위해 end값 줄이기
    if cnt <= target:
        end = mid - 1
        result = mid

    # 블루레이가 target보다 크면 블루레이 크기를 키워서 나눠지는 수 줄이기
    else:
        start = mid + 1


print(result)