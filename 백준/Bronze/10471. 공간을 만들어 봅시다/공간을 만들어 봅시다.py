import sys
input = sys.stdin.readline

W, P = map(int, input().split())
L = list(map(int, input().split()))
L = [0] + L + [W]
parts = [L[i] - L[i - 1] for i in range(1, len(L))]
r = set(parts)
for start in range(len(parts) - 1):
    for end in range(start + 1, len(parts)):
        r.add(sum(parts[start:end + 1]))
print(*sorted(r))