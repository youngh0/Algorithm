num, length = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

visited = [False] * len(arr)

tmp = []
res = set()
def n_m(idx):
    if len(tmp) == length:
        res.add(tuple(tmp))
        return

    for i in range(idx,len(arr)):
        if not visited[i]:
            tmp.append(arr[i])
            visited[i] = True

            n_m(i+1)
            tmp.pop()
            visited[i] = False
n_m(0)

print_res = list(res)
print_res.sort()

for a in print_res:
    print(" ".join(map(str,a)))