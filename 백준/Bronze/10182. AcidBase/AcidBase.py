import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    DATA = input().split()
    if DATA[0] == 'H':
        ph = - math.log10(float(DATA[-1]))
    else:
        ph = 14 + math.log10(float(DATA[-1]))
    print(f'{ph:.2f}')