import sys
input = sys.stdin.readline

N = int(input().strip())
N //= 52
k = 1
while True:
    x, mod = divmod((N - (21 * k)), 7)
    if x <= 100 and mod == 0:
        print(x)
        print(k)
        break
    k += 1