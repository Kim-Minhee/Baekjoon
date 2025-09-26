import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    bi = bin(n)[2:].zfill(32)
    r = int(bi[::-1], 2)
    print(r)