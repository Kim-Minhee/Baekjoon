import sys
input = sys.stdin.readline

T1, T2 = map(int, input().split())
if T2 % 6 == 0:
    if T1 % 30 == 0.5 * (T2 // 6):
        print('O')
    else:
        print('X')
else:
    print('X')