import sys
input = sys.stdin.readline

while True:
    N = int(input().strip())
    if N == 0:
        break
    S = list(map(int, input().split()))
    S.sort()
    sub = abs(S[0] - S[1])
    for i in range(1, len(S) - 1):
        sub = min(sub, abs(S[i] - S[i + 1]))
    print(sub)