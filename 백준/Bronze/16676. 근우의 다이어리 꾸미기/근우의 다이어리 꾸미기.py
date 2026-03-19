import sys
input = sys.stdin.readline

N = int(input().strip())
i, r = 2, 1
while True:
    if N >= int('1' * i):
        r += 1
    else:
        print(r)
        break
    i += 1