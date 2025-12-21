import sys
input = sys.stdin.readline

while True:
    D, N = input().split()
    if D == N == '0':
        break

    N = N.replace(D, '')
    if not N:
        print(0)
    else:
        print(int(N))