# GPT 5.1
import sys
input = sys.stdin.readline

while True:
    n = int(input().strip())
    if n == 0:
        break

    scores = list(map(int, input().split()))
    scores.sort()

    min_diff = float('inf')
    for i in range(n - 1):
        diff = scores[i + 1] - scores[i]
        if diff < min_diff:
            min_diff = diff

    print(min_diff)