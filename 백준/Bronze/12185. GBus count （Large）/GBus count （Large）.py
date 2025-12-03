import sys

INPUT_DATA = sys.stdin.read().split()

data = iter(INPUT_DATA)

for t in range(1, int(next(data)) + 1):
    n = int(next(data))
    gbus = []
    for _ in range(n):
        a = int(next(data))
        b = int(next(data))
        gbus.append((a, b))
    
    p = int(next(data))
    r = []
    for _ in range(p):
        c = int(next(data))
        cnt = 0
        for a, b in gbus:
            if a <= c <= b:
                cnt += 1
        r.append(str(cnt))
    print(f'Case #{t}: {" ".join(r)}')