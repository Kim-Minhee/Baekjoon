import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    N, P, Q = map(int, input().split())
    W = list(map(int, input().split()))
    W.sort()
    
    cnt = 0
    for i in range(N):
        weights = sum(W[:i + 1])
        if weights > Q:
            break
        cnt += 1

    print(f'Case {t}: {min(P, cnt)}')