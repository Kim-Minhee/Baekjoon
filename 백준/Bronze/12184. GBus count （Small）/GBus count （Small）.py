import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    if t != 1:
        input()
    N = int(input().strip())
    AB = list(map(int, input().split()))
    gbus = {}
    for i in range(0, 2 * N, 2):
        a = AB[i]
        b = AB[i + 1]
        for num in range(a, b + 1):
            cnt = gbus.get(num, 0)
            gbus[num] = cnt + 1

    P = int(input().strip())
    C = [int(input().strip()) for _ in range(P)]
    r = []
    for c in C:
        r.append(str(gbus.get(c, 0)))
    print(f'Case #{t}: {" ".join(r)}')