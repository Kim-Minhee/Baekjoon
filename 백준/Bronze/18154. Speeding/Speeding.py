import sys
input = sys.stdin.readline

cur_t, cur_d, max_s = 0, 0, 0
for i in range(int(input().strip())):
    T, D = map(int, input().split())
    if i == 0:
        continue
    t, d = T - cur_t, D - cur_d
    s = int(d / t)
    max_s = max(max_s, s)
    cur_t, cur_d = T, D
print(max_s)