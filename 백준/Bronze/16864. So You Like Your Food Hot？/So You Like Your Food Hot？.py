import sys
input = sys.stdin.readline

PT, P1, P2 = map(float, input().split())
PT = int(round(PT * 100))
P1 = int(round(P1 * 100))
P2 = int(round(P2 * 100))

chk = False
for i in range(int(PT / P1) + 1):
    p = PT - (P1 * i)
    if p % P2 == 0:
        print(i, int(p // P2))
        chk = True

if not chk:
    print('none')