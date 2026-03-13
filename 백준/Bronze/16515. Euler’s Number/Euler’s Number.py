# GPT 5
import sys

n = int(sys.stdin.readline())

e = 1.0
term = 1.0  # 1/0!

for i in range(1, n + 1):
    term /= i
    e += term

print("{:.15f}".format(e))