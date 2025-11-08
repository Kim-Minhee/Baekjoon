import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    A, B = map(int, input().split())
    S = input().strip()
    r = []
    for s in S:
        r.append(chr((A * (ord(s) - 65) + B) % 26 + 65))
    print(''.join(r))