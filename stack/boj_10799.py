array = list(input())
answer = 0
st = []
for i in range(len(array)):
    if array[i] == '(':
        st.append('(')
    else:
        st.pop()
        if array[i-1] == '(':
            answer += len(st)
        else:
            answer += 1


print(answer)