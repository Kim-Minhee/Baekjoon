import sys
input = sys.stdin.readline

for t in range(1, int(input().strip()) + 1):
    N, K = map(int, input().split())
    robots = [tuple(map(int, input().split())) for _ in range(4)]
    cnt = 0
    for a in robots[0]:
        for b in robots[1]:
            for c in robots[2]:
                for d in robots[3]:
                    if a ^ b ^ c ^ d == K:
                        cnt += 1
    print(f'Case #{t}: {cnt}')