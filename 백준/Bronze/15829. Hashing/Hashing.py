import sys
input = sys.stdin.readline

L = int(input().strip())
S = input().strip()
h = 0
for i, s in enumerate(S):
    h += (ord(s) - ord('a') + 1) * 31 ** i
    h %= 1234567891
print(h)