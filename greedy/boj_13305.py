# 주유소
# https://www.acmicpc.net/problem/13305

n = int(input())
distances = list(map(int, input().split()))
oil_prices = list(map(int, input().split()))

# 첫 번째 도시에서 두 번째 도시까지 가기위한 비용
answer = oil_prices[0] * distances[0]

# 현재 까지 중 가장 싼 값의 기름 비용
oil_cost = oil_prices[0]
for i in range(1,n-1):
    # 만약 i번째 도시의 기름값이 지금까지 주유하던 비용보다 싸면 이제부터 i번째 도시에서 주유
    if oil_cost > oil_prices[i]:
        oil_cost = oil_prices[i]
    answer += distances[i] * oil_cost

print(answer)