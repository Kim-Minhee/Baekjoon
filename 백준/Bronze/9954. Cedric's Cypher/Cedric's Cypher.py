import sys
input = sys.stdin.readline

up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
low = 'abcdefghijklmnopqrstuvwxyz'
while True:
    TEXT = input().strip()
    if TEXT == '#':
        break
    text = TEXT[:-1]
    s = up.index(TEXT[-1])
    r = ''
    for t in text:
        if t in up:
            r += up[up.index(t) - s]
        elif t in low:
            r += low[low.index(t) - s]
        else:
            r += t
    print(r)