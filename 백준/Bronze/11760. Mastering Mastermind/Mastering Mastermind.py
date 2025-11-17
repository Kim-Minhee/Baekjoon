import sys
input = sys.stdin.readline

N, C, P = input().split()
r, diff_code, diff_pred = 0, [], []
for i in range(int(N)):
    if C[i] == P[i]:
        r += 1
    else:
        diff_code.append(C[i])
        diff_pred.append(P[i])
s = 0
for ch in set(diff_code):
    s += min(diff_code.count(ch), diff_pred.count(ch))
print(r, s)