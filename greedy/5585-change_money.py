n = int(input())

change_money = 1000-n

count = 0

coin_kinds = [500,100,50,10,5,1]

for coin in coin_kinds:
    count += change_money//coin
    change_money %= coin

print(count)