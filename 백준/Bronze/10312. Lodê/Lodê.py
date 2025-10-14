import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    K = int(input().strip())
    r = []
    start = False
    for m in range(14, -1, -1):
        if 3 ** m <= K:
            cnt = K // (3 ** m)
            r.append(cnt)
            K -= 3 ** m * cnt
            start = True
        elif start:
            r.append(0)
    print(*r)