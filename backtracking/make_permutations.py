from itertools import combinations, permutations

test = [1,3,5,4,9,1]

print(list(permutations(test,3)))
print("----------------")

tmp = []
is_used = [0] * len(test)

def permu():
    if len(tmp) == 3:

        print("("," ".join(map(str,tmp)),") ", end=" ")
        return

    for i in range(len(test)):
        if is_used[i] == 0:
            tmp.append(test[i])
            is_used[i] = 1

            permu()
            tmp.pop()
            is_used[i] = 0

permu()