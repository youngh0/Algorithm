kinds, value = map(int,input().split(' '))

coins = []
for i in range(kinds):
    coins.append(int(input()))

coin_count = 0
coins.sort(reverse=True)

for i in coins:
    if value <= 0:
        break

    coin_count += value//i
    value %= i

print(coin_count)