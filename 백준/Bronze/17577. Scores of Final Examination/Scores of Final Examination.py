# GPT 5
import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    total = [0] * n  # 각 학생 총점

    for _ in range(m):
        scores = list(map(int, input().split()))
        for i in range(n):
            total[i] += scores[i]

    print(max(total))