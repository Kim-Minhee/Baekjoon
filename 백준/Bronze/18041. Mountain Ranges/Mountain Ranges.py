import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

max_cnt = 1
cnt = 1
for i in range(N - 1):
    if A[i + 1] - A[i] <= X:
        cnt += 1
    else:
        max_cnt = max(cnt, max_cnt)
        cnt = 1
max_cnt = max(cnt, max_cnt)
print(max_cnt)