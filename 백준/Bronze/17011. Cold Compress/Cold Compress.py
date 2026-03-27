import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    T = input().strip()
    r = []
    cur_t = T[0]
    cur_c = 1
    for t in T[1:]:
        if cur_t != t:
            r.append(str(cur_c))
            r.append(cur_t)
            cur_t = t
            cur_c = 1
        else:
            cur_c += 1
    r.append(str(cur_c))
    r.append(cur_t)
    print(' '.join(r))