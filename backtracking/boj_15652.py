# N과 M(4)
# https://www.acmicpc.net/problem/15652

n, m = map(int, input().split())

tmp = []

def n_m_4(start):
    if len(tmp) == m:
        print(" ".join(map(str,tmp)))
        return

    for i in range(start,n+1):
        tmp.append(i)
        n_m_4(i)
        tmp.pop()

n_m_4(1)