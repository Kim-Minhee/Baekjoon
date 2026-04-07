import sys
input = sys.stdin.readline

cases = [list(map(int, input().split())) for _ in range(int(input().strip()))]

max_score = 0
for first in range(1, 4):
    score = 0
    cur = first
    for a, b, g in cases:
        if cur == a:
            cur = b
        elif cur == b:
            cur = a
        if cur == g:
            score += 1
    max_score = max(max_score, score)
print(max_score)