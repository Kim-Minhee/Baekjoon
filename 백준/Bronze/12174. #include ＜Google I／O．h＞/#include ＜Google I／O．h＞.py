import sys, re
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    B = int(input().strip())
    S = input().strip()
    S = S.replace(' ', '')
    S = S.replace('I', '1')
    S = S.replace('O', '0')
    r = []
    for i in range(B):
        r.append(chr(int('0b' + S[8 * i: 8 * (i + 1)], 2)))
    print(f'Case #{t}: {"".join(r)}')