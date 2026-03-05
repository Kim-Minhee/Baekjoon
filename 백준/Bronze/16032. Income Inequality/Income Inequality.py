# GPT 5
import sys

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break

    incomes = list(map(int, sys.stdin.readline().split()))
    avg = sum(incomes) / n

    count = sum(1 for x in incomes if x <= avg)
    print(count)