import sys
input = sys.stdin.readline

d, r = False, 1
for _ in range(int(input().strip())):
    A, B, T = map(int, input().split())
    r *= B / A
    if T:
        d = not d
print(int(d), int(r))