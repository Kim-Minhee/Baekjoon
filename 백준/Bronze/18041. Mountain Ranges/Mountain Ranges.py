# GPT 5
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

max_len = 1
cur_len = 1

for i in range(1, N):
    if A[i] - A[i - 1] <= X:
        cur_len += 1
    else:
        max_len = max(max_len, cur_len)
        cur_len = 1

max_len = max(max_len, cur_len)

print(max_len)