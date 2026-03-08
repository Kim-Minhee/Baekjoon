# GPT 5
import sys
input = sys.stdin.readline

a, b, n, w = map(int, input().split())

ans = []

for x in range(1, n):
    y = n - x
    if a * x + b * y == w:
        ans.append((x, y))

if len(ans) == 1:
    print(ans[0][0], ans[0][1])
else:
    print(-1)