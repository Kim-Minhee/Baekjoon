import sys
input = sys.stdin.readline

C = input().strip()
P = 'PER' * (len(C) // 3)
cnt = sum(1 for c, p in zip(C, P) if c != p)
print(cnt)