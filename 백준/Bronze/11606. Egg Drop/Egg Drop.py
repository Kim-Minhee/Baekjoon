import sys
input = sys.stdin.readline

N, K = map(int, input().split())
test = [input().split() for _ in range(N)]

min_floor, max_floor = 1, K
for f, r in test:
    if r == 'SAFE':
        min_floor = max(min_floor, int(f))
    else:
        max_floor = min(max_floor, int(f))
print(min_floor + 1, max_floor - 1)