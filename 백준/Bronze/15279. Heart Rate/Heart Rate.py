import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    B, P = input().split()
    B, P = int(B), float(P)
    bpm = 60 * B / P
    min_abpm = 60 * (B - 1) / P
    max_abpm = 60 * (B + 1) / P
    print(f'{min_abpm:.4f} {bpm:.4f} {max_abpm:.4f}')