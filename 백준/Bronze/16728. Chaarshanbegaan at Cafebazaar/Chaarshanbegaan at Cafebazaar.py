import sys
input = sys.stdin.readline

scores = [(10, 10), (30, 9), (50, 8), (70, 7), (90, 6), (110, 5), (130, 4), (150, 3), (170, 2), (190, 1)]

r = 0
for _ in range(int(input().strip())):
    X, Y = map(int, input().split())
    d = (X * X + Y * Y) ** 0.5
    for s in scores:
        if d <= s[0]:
            r += s[1]
            break
print(r)