score = input()


right = 0
left = 0
for i in range(len(score)//2):
    right += int(score[i])
    left += int(score[i+len(score)//2])

if left == right:
    print('LUCKY')
else:
    print("READY")