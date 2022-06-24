# 단어 수학
# https://www.acmicpc.net/problem/1339

from collections import defaultdict

words_num = int(input())

words = []

for _ in range(words_num):
    words.append(input().rstrip())

alphabets = defaultdict(int)

for word in words:
    for i in range(len(word)):
        alphabets[word[i]] += 1*(10**(len(word)-(i+1)))

sorted_alphabets = sorted(alphabets.items(), key = lambda x:-x[1])
answer = 0

for idx, alpha in enumerate(sorted_alphabets):
    answer += alpha[1] * (9-idx)
print(answer)