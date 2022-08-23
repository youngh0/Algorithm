# https://www.acmicpc.net/problem/1158
# 요세푸스 문제

n,k = map(int,input().split())

array = [i+1 for i in range(n)]

answer = []


idx = 0
for i in range(n):
    idx += k-1
    idx %= len(array)
    answer.append(str(array.pop(idx)))

print("<",', '.join(answer),">", sep="")



