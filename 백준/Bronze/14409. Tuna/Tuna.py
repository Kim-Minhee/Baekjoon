import sys
input = sys.stdin.readline

N = int(input().strip())
X = int(input().strip())
total_value = 0
for _ in range(N):
    P1, P2 = map(int, input().split())
    if abs(P1 - P2) <= X:
        total_value += max(P1, P2)
    else:
        total_value += int(input().strip())
print(total_value)