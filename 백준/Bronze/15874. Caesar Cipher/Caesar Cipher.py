import sys
input = sys.stdin.readline

K, L = map(int, input().split())
S = input().rstrip()
r = []
for s in S:
    if not s.isalpha():
        r.append(s)
        continue
    s_upper = s.upper()
    k = (ord(s_upper) - ord('A') + K) % 26
    if s_upper == s:
        r.append(chr(ord('A') + k))
    else:
        r.append(chr(ord('a') + k))
print(''.join(r))