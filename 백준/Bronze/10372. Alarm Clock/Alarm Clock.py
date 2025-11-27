import sys
input = sys.stdin.readline

digits = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
N = int(input().strip())
chk = False
for h in range(24):
    h = str(h)
    if len(h) < 2:
        h = '0' + h
    for m in range(60):
        m = str(m)
        if len(m) < 2:
            m = '0' + m
        segm = digits[int(h[0])] + digits[int(h[1])] + digits[int(m[0])] + digits[int(m[1])]
        if segm == N:
            print(f'{h}:{m}')
            chk = True
            break
    if chk:
        break
if not chk:
    print('Impossible')