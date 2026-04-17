import sys
input = sys.stdin.readline

N = int(input().strip())
rooms = [0] * (N + 1)
for _ in range(N):
    A = int(input().strip())
    if A <= N:
        rooms[A] = 1
print(sum(rooms))