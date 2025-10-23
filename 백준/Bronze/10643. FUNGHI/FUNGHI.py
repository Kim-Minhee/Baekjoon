import sys
input = sys.stdin.readline

M = [int(input().strip()) for _ in range(8)]
M += M[:3]

max_mus = 0
for i in range(8):
    max_mus = max(max_mus, sum(M[i:i+4]))
print(max_mus)