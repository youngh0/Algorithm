from itertools import combinations

test = [3,6,1,4]

print(list(combinations(test,2)))
print("----------------")

tmp = []
is_used = [0] * len(test)

def make_combi(start):
    if len(tmp) == 2:
        print("("," ".join(map(str,tmp)),") ", end=" ")
        return

    for i in range(start, len(test)):
        if is_used[i] == 0:
            is_used[i] = 1
            tmp.append(test[i])

            make_combi(i+1)
            is_used[i] = 0
            tmp.pop()

make_combi(0)