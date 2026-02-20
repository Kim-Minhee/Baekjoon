import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    N, M = map(int, input().split())
    print((min(N, M) - 1) * 2)