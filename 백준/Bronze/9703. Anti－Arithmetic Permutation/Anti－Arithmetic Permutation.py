# GPT 5
import sys
input = sys.stdin.readline

for c in range(1, int(input()) + 1):
    N = int(input())
    P = list(map(int, input().split()))
    found = False
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            d = P[j] - P[i]
            for k in range(j + 1, N):
                if P[k] - P[j] == d:
                    found = True
                    break
            if found:
                break
        if found:
            break
    print(f'Case #{c}: {"NO" if found else "YES"}')