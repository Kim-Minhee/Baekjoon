import sys
input = sys.stdin.readline

r = ''
PUZZLE = ''.join([''.join(input().split()) for _ in range(int(input().strip()))])
for ch in PUZZLE:
    if ch not in r:
        r += ch
    if len(r) == 26:
        break
print(r)