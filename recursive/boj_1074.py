# Z
# https://www.acmicpc.net/problem/1074

n,r,c = map(int, input().split())

# graph = [[0]* (2**n) for _ in range(2**n)]

num = 0

def search_z(length,r,c):
    global num

    if length == 2:
        # 탐색
        # print(length, r, c)
        if r == 0 and c == 0:
            print(num)
        elif r == 0 and c == 1:
            print(num+1)
        elif r == 1 and c == 0:
            print(num + 2)
        elif r == 1 and c == 1:
            print(num + 3)
        return
    half = length // 2

    # 1사분면


    # r,c가 2사분면
    if r < half and c >= half:

        c -= half
        num += half*half
    # 3사분면
    elif r >= half and c < half:

        r -= half
        num += 2 * half * half

    # 4사분면
    elif r >= half and c >= half:

        r -= half
        c -= half
        num += 3 * half * half
    search_z(half, r, c)



search_z(2**n,r,c)

