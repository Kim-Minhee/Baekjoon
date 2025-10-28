import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    apb = 'abcdefghijklmnopqrstuvwxyz'
    N = int(input().strip())
    A = tuple(map(int, input().split()))
    r = []
    for i in A:
        a = apb[i]
        r.append(a)
        apb = apb.replace(a, '')
        apb = a + apb
    print(''.join(r))