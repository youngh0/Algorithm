# 주식
# https://www.acmicpc.net/problem/11501
import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    days = int(input())
    stocks = list(map(int, input().split()))

    stocks.reverse()
    max_stock = 0
    benefit = 0
    for stock in stocks:
        # 오늘 주가가 최대 주가 보다 높다면 최대 주가 업데이트
        if stock > max_stock:
            max_stock = stock
        # 오늘 주가가 최대 주가보다 낮다면 구매해서 이익 내기
        else:
            benefit += max_stock - stock

    print(benefit)
