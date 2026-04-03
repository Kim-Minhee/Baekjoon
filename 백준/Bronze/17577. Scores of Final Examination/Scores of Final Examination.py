import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break

    scores = [0] * N
    for _ in range(M):
        for i, p in enumerate(map(int, input().split())):
            scores[i] += p
    print(max(scores))