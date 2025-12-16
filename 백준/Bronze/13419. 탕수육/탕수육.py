import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    W = input().strip()
    l = len(W)
    first, last = '', ''
    if l == 1:
        first += W
        last += W
    elif l % 2 == 0:
        for i, w in enumerate(W):
            if i % 2 == 0:
                first += w
            else:
                last += w
    else:
        for i, w in enumerate(W + W):
            if i % 2 == 0:
                first += w
            else:
                last += w
    print(first)
    print(last)