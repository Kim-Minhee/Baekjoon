import sys
input = sys.stdin.readline

L, X = map(int, input().split())
cur_p = 0
r = 0
for _ in range(X):
    E, P = input().split()
    P = int(P)
    if E == 'leave':
        cur_p = max(0, cur_p - P)
    elif cur_p + P <= L:
        cur_p += P
    else:
        r += 1
print(r)