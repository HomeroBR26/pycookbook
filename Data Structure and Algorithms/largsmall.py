"""Make a list of the largest or smallest N items in a collection."""
import heapq
import re

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap, expensive)


lines = [
    "21/08/17 07:37:45	Compraste 0.00371747BCH por 0.00100000BTC",
    "18/08/17 14:06:22	Compraste 0.00844598BCH por 0.00500000BTC",
    "18/08/17 12:30:29	Compraste 0.00972539BCH por 0.00400000BTC",
    "17/08/17 10:56:04	Compraste 0.03750005BCH por 0.00300000BTC"]
print(heapq.nsmallest(2, lines, key=lambda s: re.findall("por (.+)BTC", s)[0]))
