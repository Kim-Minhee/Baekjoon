import sys
input = sys.stdin.readline

while True:
    N = int(input().strip())
    if N == 0:
        break
    H = list(map(int, input().split()))
    H += H
    peak = 0
    for i in range(N):
        if H[i - 1] < H[i] < H[i + 1] or H[i - 1] > H[i] > H[i + 1]:
            continue
        peak += 1
    print(peak)