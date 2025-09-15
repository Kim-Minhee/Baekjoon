import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    P, T, M = map(int, input().split())
    score = P * 15 + T * 20 + M * 25
    needed = math.ceil((9000 - score) / 40)
    if 0 <= needed <= 100:
        print(needed)
    elif needed < 0:
        print(0)
    else:
        print('impossible')