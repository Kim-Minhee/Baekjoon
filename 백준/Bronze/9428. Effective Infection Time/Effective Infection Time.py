import sys
input = sys.stdin.readline

N = int(input().strip())
for _ in range(N):
    IM, IY = map(int, input().split())
    AM, AY = map(int, input().split())

    eit = 0
    if IY == AY:
        eit += (0.5 / (12 - IM + 1)) * (AM - IM)
    else:
        eit += 0.5
        eit += AY - IY - 1
        eit += (1 / 12) * (AM - 1)

    print(f'{eit:.4f}')