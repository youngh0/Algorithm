# N과 M(2)
# https://rexiann.github.io/2020/11/28/set-in-python.html

n,m = map(int, input().split())

visited = [0] * (n+1)
array = []

def make_combination(start):
    # print(start, array)
    if len(array) == m:
        print(" ".join(map(str,array)))
        return

    for i in range(start, n+1):
        if visited[i] == 0:
            visited[i] = 1
            array.append(i)

            make_combination(i+1)
            array.pop()
            visited[i] = 0



make_combination(1)

