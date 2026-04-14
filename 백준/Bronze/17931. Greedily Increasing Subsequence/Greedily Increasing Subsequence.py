# GPT 5
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

pos = [0] * (N + 1)
for i in range(N):
    pos[A[i]] = i

# suffix minimum
min_pos = [0] * (N + 2)
min_pos[N] = pos[N]

for i in range(N - 1, 0, -1):
    if pos[i] < min_pos[i + 1]:
        min_pos[i] = pos[i]
    else:
        min_pos[i] = min_pos[i + 1]

res = []
cur = A[0]
cur_pos = pos[cur]
res.append(cur)

while cur < N:
    # cur보다 큰 값들 중 가장 왼쪽 위치
    nxt_pos = min_pos[cur + 1]

    if nxt_pos <= cur_pos:
        break

    nxt_val = A[nxt_pos]
    res.append(nxt_val)

    cur = nxt_val
    cur_pos = nxt_pos

print(len(res))
print(*res)