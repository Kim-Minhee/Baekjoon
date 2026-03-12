import sys
input = sys.stdin.readline

M = input().strip()
C = input().strip()
l = len(C)
cnt = 0
for i in range(0, len(M) - l + 1):
    crib_chk = True
    for m, c in zip(M[i:i + l], C):
        if m == c:
            crib_chk = False
            break
    if crib_chk:
        cnt += 1
print(cnt)