# GPT 5
import sys

n = int(sys.stdin.readline())

k = n // 3

if k < 3:
    print(0)
else:
    print((k - 1) * (k - 2) // 2)