# 숫자들을 정렬 후 '-' 개수만큼 상위 숫자들을 나머지 숫자에서 뺀다.

n = input()

n = n.split('-')

final_num_list = []

for i in n:
    num_list = i.split('+')
    num_list = list(map(int,num_list))

    final_num_list.append(sum(num_list))

print(final_num_list[0] - (sum(final_num_list[1:])))

# num_list = sorted(list(map(int,n)))
#
# plus = sum(num_list[minus_num:])
# minus = sum(num_list[:minus_num])
#
#
# print(num_list)
# print(plus_num)
# print(minus_num)
# print(plus)
# print(minus)
# print(minus-plus)