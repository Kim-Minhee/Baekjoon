import sys
input = sys.stdin.readline

N, M = map(int, input().split())
R = list(map(int, input().split()))
t = 0
if R[0] == N:
    t += 1
for i in range(1, M):
    if R[i - 1] <= R[i]:
        continue
    t += 1
print(t)