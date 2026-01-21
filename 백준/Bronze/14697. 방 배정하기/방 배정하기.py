import sys
input = sys.stdin.readline

A, B, C, N = map(int, input().split())
r = 0
for a in range(N // A, -1, -1):
    remaining_after_a = N - (A * a)
    if remaining_after_a == 0:
        r = 1
        break
    for b in range(remaining_after_a // B, -1, -1):
        remaining_after_b = remaining_after_a - (B * b)
        if remaining_after_b == 0 or remaining_after_b % C == 0:
            r = 1
            break
print(r)