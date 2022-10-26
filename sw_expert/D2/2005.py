# 파스칼 삼각형 만들기

tc = int(input())

for t in range(1,tc+1):
    n = int(input())

    array = [[0] * n for _ in range(n)]

    for i in range(n):
        array[i][0] = 1

    for i in range(1,n):
        for j in range(1,i+1):
            array[i][j] = array[i-1][j] + array[i-1][j-1]

    print(f"#{t}")
    for i in range(n):
        for j in range(i+1):
            print(array[i][j], end=" ")
        print()