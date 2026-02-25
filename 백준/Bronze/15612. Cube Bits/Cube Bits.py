# GPT 5
import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input().strip())

for _ in range(n):
    v = int(input().strip())

    if v == 0:
        write("0\n")
        continue

    digits = []
    while v > 0:
        digits.append(str(v % 3))
        v //= 3

    write("".join(reversed(digits)) + "\n")