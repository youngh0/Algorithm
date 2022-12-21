# 좋은 단어



tc = int(input())

answer = 0
for _ in range(tc):
    word = input()
    st = []
    for letter in word:
        if len(st) == 0:
            st.append(letter)
        elif st[-1] == letter:
            st.pop()
        else: st.append(letter)

    if len(st) == 0:
        answer += 1

print(answer)