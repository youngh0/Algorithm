# https://www.acmicpc.net/problem/1449
# 수리공 항승

# start, end 포인터 사용
# end포인터가 배열 인덴스를 넘기기 전까지 반복
# 만약 end-start+1 이 테이프 길이랑 같으면 테이프 붙이고 start를 end+1로, end를 start로
# 만약 end-start+1 이 l보다 크면


n,l = map(int,input().split(" "))

water = list(map(int,input().split()))
water.sort()

start = 0
end = 1
answer = 0
idx = 0

if l == 1:
    print(n)

else:
    while end <= n-1:
        if water[end] - water[start] + 1 == l:
            answer += 1
            start = end + 1
            end += 1

        elif water[end] - water[start] +1 > l:
            answer += 1
            start = end
            end = start

        end += 1
    if start < n:
        answer += 1
    print(answer)


