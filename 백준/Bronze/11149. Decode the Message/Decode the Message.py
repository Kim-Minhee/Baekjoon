import sys
input = sys.stdin.readline

alp = 'abcdefghijklmnopqrstuvwxyz '

for _ in range(int(input().strip())):
    M = list(input().split())
    r = []
    for m in M:
        n = sum(alp.index(ch) for ch in m)
        r.append(alp[n % 27])
    print(''.join(r))