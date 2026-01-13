import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = 1
for _ in range(N):
    A = int(input().strip())
    if A != 0:
        d *= A
print(d % M)