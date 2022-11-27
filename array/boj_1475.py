from collections import Counter
import math

room_number = list(map(int, list(input())))


for number in range(len(room_number)):
    if room_number[number] == 9:
        room_number[number] = 6

counter = Counter(room_number)
if counter[6]:
    counter[6] =math.ceil(counter[6] / 2)

print(counter.most_common()[0][1])
