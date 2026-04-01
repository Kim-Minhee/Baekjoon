import sys
input = sys.stdin.readline

T = input().strip()
key = ord(T[0]) ^ 67
r = []
for t in T:
    r.append(chr(ord(t) ^ key))
print(''.join(r))