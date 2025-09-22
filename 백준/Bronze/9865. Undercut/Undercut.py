import sys
input = sys.stdin.readline

def undercut(a, b):
    if a == 2 and b == 1:
        return 6
    elif a - b == 1:
        return a + b
    else:
        return a

for t in range(1, int(input()) + 1):
    M = int(input())
    score_tessa, score_danny = 0, 0
    while M != 0:
        N = list(map(int, input().split()))
        n = len(N)
        M -= n // 2
        for i in range(0, n, 2):
            tessa = N[i]
            danny = N[i+1]
            if tessa == 2 and danny == 1:
                score_danny += 6
            elif tessa == 1 and danny == 2:
                score_tessa += 6
            elif tessa - danny == 1:
                score_danny += tessa + danny
            elif danny - tessa == 1:
                score_tessa += tessa + danny
            elif tessa > danny:
                score_tessa += tessa
            elif danny > tessa:
                score_danny += danny

    print(f'Game {t}: Tessa {score_tessa} Danny {score_danny}')