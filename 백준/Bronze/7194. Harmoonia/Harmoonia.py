import sys
input = sys.stdin.readline

N = int(input().strip())
ab = []
for i in range(N):
    A, B = map(int, input().split())
    ab.append((A, B, abs(A - B) % 12))

chk = False
for i in range(N - 1):
    if ab[i][0] != ab[i + 1][0] and ab[i][1] != ab[i + 1][1]:
        if ab[i][2] == ab[i + 1][2] == 7:
            chk = True
            print(i + 1)

if not chk:
    print('POLE')