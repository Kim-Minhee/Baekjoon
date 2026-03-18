import sys
input = sys.stdin.readline

T, S = input().split()
r = []
if T == 'E':
    cur_s, cur_c = S[0], 1
    for s in S[1:]:
        if s == cur_s:
            cur_c += 1
        else:
            r.append(cur_s + str(cur_c))
            cur_s = s
            cur_c = 1
    r.append(cur_s + str(cur_c))
else:
    for i in range(0, len(S), 2):
        t, c = S[i], int(S[i + 1])
        r.append(t * c)
print(''.join(r))