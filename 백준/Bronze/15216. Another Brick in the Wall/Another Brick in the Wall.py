import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
X = list(map(int, input().split()))
cur_w, done = 0, False
for x in X:
    cur_w += x
    if cur_w == W:
        cur_w = 0
        H -= 1
        if H == 0:
            done = True
            break
    elif cur_w > W:
        break

if done:
    print('YES')
else:
    print('NO')