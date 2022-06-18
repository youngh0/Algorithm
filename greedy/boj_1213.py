# 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213

# 팰린드롬이 되기 위해선 단어 길이가 짝수일 경우 홀수 개인 알파벳이 있으면 안됨.
# 단어가 홀수 길이면 홀수 개인 알파벳이 하나 있어도됨

from collections import Counter
import sys

word = input()
word_list = list(word)
word_list.sort()

word_count = Counter(word_list)

odd_alphabet_count = 0
odd_alphabet = ''
for alphabet in word_count:
    if word_count[alphabet] % 2 == 1:
        odd_alphabet_count += 1
        odd_alphabet += alphabet
    if odd_alphabet_count > 1:
        print("I'm Sorry Hansoo")
        sys.exit()

answer = ''

for i in range(0, len(word), 2):
    if word_count[word_list[i]] % 2 == 1:
        word_count[word_list[i]] -= 1
    else:
        answer += word_list[i]

tmp = answer[::-1]
answer += odd_alphabet
answer += tmp
print(answer)