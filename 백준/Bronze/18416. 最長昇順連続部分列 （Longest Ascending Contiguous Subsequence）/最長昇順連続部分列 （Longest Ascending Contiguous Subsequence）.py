import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

max_cnt, cnt = 0, 0
for i in range(N - 1):
    if A[i + 1] >= A[i]:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0
max_cnt = max(max_cnt, cnt)
print(max_cnt + 1)