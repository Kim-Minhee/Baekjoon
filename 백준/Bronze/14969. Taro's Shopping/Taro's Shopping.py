# GPT 5.1
import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    prices = list(map(int, input().split()))
    prices.sort()

    left, right = 0, n - 1
    best = -1

    while left < right:
        s = prices[left] + prices[right]

        if s <= m:
            if s > best:
                best = s
            left += 1
        else:
            right -= 1

    if best == -1:
        print("NONE")
    else:
        print(best)