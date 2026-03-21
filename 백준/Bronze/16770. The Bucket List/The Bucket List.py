import sys
input = sys.stdin.readline

N = int(input().strip())
time = [0] * 1001
for _ in range(N):
    S, T, B = map(int, input().split())
    for i in range(S, T + 1):
        time[i] += B
print(max(time))