# N과 M (3)
# https://www.acmicpc.net/problem/15651

n, m = map(int, input().split())

is_used = [[0] * (n+1) for _ in range(n+1)]

tmp = []

def n_m_3(num):
    if num == m:
        print(" ".join(map(str,tmp)))
        return

    for i in range(1,n+1):
        if is_used[num][i] == 0:
            tmp.append(i)
            is_used[num][i] = 1

            n_m_3(num+1)

            tmp.pop()
            is_used[num][i] = 0

n_m_3(0)