# N과 M(1)
# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())

array = []
is_used = [0]*(n+1)

def make_permutation():
    if len(array) == m:
        ans = " ".join(map(str,array))
        print(ans)
        return

    for i in range(1,n+1):
        if is_used[i] == 0:
            is_used[i] = 1
            array.append(i)

            make_permutation()
            array.pop()
            is_used[i] = 0
make_permutation()
