import sys
input = sys.stdin.readline

while True:
    try:
        N = int(input().strip())
        X = [0] + list(map(int, input().split()))
        if N == 1:
            print(1)
            continue
        d = X[N] - X[N - 1]
        r = N - 1
        for i in range(N - 1, 1, -1):
            if X[i] - X[i - 1] == d:
                r = i - 1
                continue
            else:
                break
        print(r)
    except:
        break